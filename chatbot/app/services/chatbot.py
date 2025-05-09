from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPEN_AI_KEY')

client =  OpenAI(api_key= api_key)

chat_log = []

while True:
    user_input = input("How may I help you today? or type 'quit' to leave chat.")
    
    if user_input.casefold() == 'quit':
        break
    
    chat_log.append({'role': 'user', 'content': user_input})

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=chat_log,
        temperature=0.8
    )
    bot_response = response.choices[0].message.content
    chat_log.append({'role': 'assistant', 'content': bot_response})
    print(bot_response)
    
