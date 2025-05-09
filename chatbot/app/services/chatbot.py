from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPEN_AI_KEY')



client =  OpenAI(api_key= api_key)

response  = client.responses.create(
    model='gpt-4o-mini',
    instructions='Talk like a pirate',
    input='Do you need brackets in python?',
)

print(response.output_text)