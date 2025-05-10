from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPEN_AI_KEY')

client =  OpenAI(api_key= api_key)

chat_log = [{'role': 'system', 'content': 'You are a python tutr AI, completely dedicated to teach'\
        'users how to learn python from scrath, providing clear instructions on Python concepts, best practices.'\
        'Helping create in real life a path of learning for users to be able to master Python and create aplications'
        }]

def get_chatbot_response(user_input : str)-> str:    
    chat_log.append({'role': 'user', 'content': user_input})

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=chat_log,
        temperature=0.6
    )
    bot_response = response.choices[0].message.content
    chat_log.append({'role': 'assistant', 'content': bot_response})
    return bot_response
    
