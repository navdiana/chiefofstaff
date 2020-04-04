import os
import slack
import merriam_webster_helper as mr

SLACK_CHANNEL = 'chiefofstaff'
slack_token = os.environ.get('CHIEF_OF_STAFF_SLACKBOT')

client = slack.WebClient(token=slack_token)

word = 'sardonic'

definition = mr.get_definition(word)
example = mr.get_example(word)

attachments = []
title ='<https://www.merriam-webster.com/dictionary/{word}|{word}>'.format(word=word)
data = {}
data['title'] = title
data['text'] = "*" + definition.replace("{bc}", ": ") + "*" + "\n// " + example
data['color'] = "#44974e"
attachments.append(data)

client.chat_postMessage(
        channel=SLACK_CHANNEL,
        attachments=attachments
)
