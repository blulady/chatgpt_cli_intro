from openai import OpenAI

client = OpenAI(api_key="need to load key in using dotenv like in app4")

# pass the api key
# define the prompt

messages = []
# system provides details about the role the ai is supposed to fulfil
messages.append({'role': 'system', 'content': "you are a CTO mentoring developers, don't only provide answers also ask guiding questions"})
messages.append({'name': "Bob",'role': 'user', 'content': "why is my website down?"})
# make an api
response = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)

# print the response
print(response)
print(response.choices[0].message.content)
