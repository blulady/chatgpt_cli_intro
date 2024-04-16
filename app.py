from openai import OpenAI

client = OpenAI(api_key="need to load key in using dotenv like in app4")

# pass the api key
# define the prompt
message = {'role': 'user', 'content': "what is the meaning of life?"}
messages = []
messages.append(message)
# make an api
response = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)

# print the response
print(response)
print(response.choices[0].message.content)