from openai import OpenAI, OpenAIError
import wikipedia
from dotenv import load_dotenv
import os


load_dotenv()
OPEN_API_KEY= os.getenv('OPEN_API_KEY')


# pass the api key
client = OpenAI(api_key=OPEN_API_KEY)

# get the user input
title = input('title of the page: ')

# get the wikipedia content
page = wikipedia.page(title=title, auto_suggest=False)

# define the prompt
prompt = 'Write a summary of the following article: ' + page.content[:10000]
messages = []
# system provides details about the role the ai is supposed to fulfil
messages.append({'role': 'system', 'content': "you are a CTO mentoring developers, don't only provide answers also ask guiding questions"})
messages.append({'name': "Bob",'role': 'user', 'content': prompt})
# make an api
try: 
    response = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)
    print(response.choices[0].message.content)

    # print the response

    # print(response.choices[0].message.content)
except OpenAIError as e:
    error_message = e.response.json()['error']['message']
    print(f"Authentication failed: {error_message}")