from openai import OpenAI, OpenAIError

client = OpenAI(api_key="need to load key in using dotenv like in app4")


# pass the api key
# define the prompt

messages = []
# system provides details about the role the ai is supposed to fulfil
messages.append({'role': 'system', 'content': "you are a CTO mentoring developers, don't only provide answers also ask guiding questions"})
messages.append({'name': "Bob",'role': 'user', 'content': "why is my website down?"})
# make an api
try: 
    response = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)
    response.raise_for_status()

    # print the response

    # print(response.choices[0].message.content)
except OpenAIError as e:
    error_message = e.response.json()['error']['message']
    print(f"Authentication failed: {error_message}")