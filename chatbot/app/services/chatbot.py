from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPEN_AI_KEY')

client =  OpenAI(api_key= api_key)



response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[{
        'role': 'system',
        'content': 'You are a helpful assistant'
    },{
        'role': 'user',
        'content': 'Write me a 4 lines bio'
    }],
    temperature=0.8
)

print(response.choices[0].message.content)