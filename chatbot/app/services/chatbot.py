from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPEN_AI_KEY')



client =  OpenAI(api_key= api_key)

response  = client.responses.create(
    model='gpt-4o-mini',
    # instructions='Talk like a pirate', #* You can leave this one out and work on roles using input
    input=[
        {
            'role': 'developer',
            'content': 'talks like Yoda from Star Wars'
        },
        {
            'role': 'user',
            'content': 'Are nested dictionaries efficient?',          
        }
    ]
)

print(response.output_text)