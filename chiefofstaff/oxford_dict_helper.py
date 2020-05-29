import requests
import os

app_id = os.environ.get('Oxford_App_ID')
app_key = os.environ.get('Oxford_App_Key')
language = "en-gb"

def get_def_and_examp(word_id):
    language = 'en-gb'
    fields = 'definitions%2Cexamples'
    strictMatch = 'false'

    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    if r.status_code != 200:
        return None
    def_dict = r.json()
    defs_list = []
    defs_examples = []
    for thing in def_dict:
        if thing == 'results':
            results = def_dict['results'][0]
            lex_ents = results['lexicalEntries'][0]['entries'][0]
            senses = lex_ents['senses']
            for sense in senses:
                definition = sense['definitions']
                example = ""
                if 'examples' in sense:
                    example = sense['examples'][0]['text']
                defs_list.append(definition)
                defs_examples.append(example)
                print("Definition = ", definition)
                print("Examples = ", example)
                print("-------")

    return defs_list, defs_examples


