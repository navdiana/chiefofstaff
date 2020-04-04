import requests
import os

dictonary_token = os.environ.get('DICTIONARY_API_KEY')

def request(word):
    dictionary_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={dict_token}'.format(
        word=word, dict_token=dictonary_token)
    payload = requests.post(dictionary_url)
    json_payload = payload.json()

    return json_payload

def get_definition(word):
    """
    Gets definition of word from merriam webster dictionary API
    :param word: string
    :return: definition string
    """
    payload = request(word)
    definition = payload[0]['def'][0]['sseq'][0][0][1]['dt'][0][1]
    definition = definition.replace("{bc}", ": ")

    return definition

def get_example(word):
    """
    Gets word in a sentence from merriam webster dictionary API
    :param word: string
    :return: example string
    """
    payload = request(word)
    example = payload[0]['def'][0]['sseq'][0][0][1]["dt"][1][1][0]['t']
    example = example.replace("{wi}", "").replace("{/wi}", "")

    return example

