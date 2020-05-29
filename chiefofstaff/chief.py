import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
import oxford_dict_helper
import slack
import os
from textwrap import dedent

def post_to_slack(title, value):
    attachments = []
    data = {}
    data['title'] = title
    data['text'] = value
    data['color'] = "#44974e"
    attachments.append(data)

    slack_client.chat_postMessage(
        channel="chiefofstaff",
        attachments=attachments
    )

slack_token = os.getenv('CHIEF_OF_STAFF_SLACKBOT')
slack_client = slack.WebClient(token=slack_token)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("ChiefOfStaff").sheet1

data = sheet.get_all_records()

numRows = sheet.row_count
val = sheet.cell(6, 2).value

values = sheet.get_all_values()
random_num = random.randint(1, len(values))

print(values[random_num])

word = values[random_num]
title = ""
value = ""
if word[1] == "":
    res = oxford_dict_helper.get_def_and_examp(word[0].lower())
    if res is not None:
        title ='<https://www.dictionary.com/browse/{word}|{word}>'.format(word=word[0].lower())
        defs = res[0]
        examples = res[1]
        for i in range(len(defs)):
            value += str(dedent('''*: {definition}* \n'''.format(definition=defs[i][0])))
            if examples[i] is not "":
                value += str(dedent('''// {example}\n'''.format(example=examples[i])))
        post_to_slack(title, value)
    else:
        print("Oopsie doopsie, can't find that word")
else:
    title = word[0]
    value = word[1]





