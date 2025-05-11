from openai import OpenAI
from fastapi.templating import Jinja2Templates
import asyncio

from dotenv import load_dotenv
import os

templates = Jinja2Templates(directory='app/templates')


load_dotenv()

api_key = os.getenv('OPEN_AI_KEY')

client =  OpenAI(api_key= api_key)

chat_log = [{'role': 'system', 'content': 'You are a python tutr AI, completely dedicated to teach'\
        'users how to learn python from scrath, providing clear instructions on Python concepts, best practices.'\
        'Helping create in real life a path of learning for users to be able to master Python and create aplications'
        }]
chat_responses = []

async def activate_websocket(websocket):
    await websocket.accept()
    while True:
        try:
            user_input = await websocket.receive_text()
            # await websocket.send_text(user_input)
            response_stream = stream_openai_response(user_input)
            
            full_reply = ""
            for chunk in response_stream:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    token = delta.content
                    full_reply += token
                    await websocket.send_text(token)
                    await asyncio.sleep(0.02)
                    
            chat_log.append({'role': 'assistant', 'content': full_reply})

        except Exception as e:
            print(f"WebSocket closed: {e}")
            break

def get_chatbot_response(request, user_input : str)-> str:    
    chat_log.append({'role': 'user', 'content': user_input})
    chat_responses.append(user_input)

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=chat_log,
        temperature=0.6,
    )
    bot_response = response.choices[0].message.content
    chat_log.append({'role': 'assistant', 'content': bot_response})
    chat_responses.append(bot_response)
    return templates.TemplateResponse("home.html", {'request': request, "chat_responses": chat_responses})

def stream_openai_response(user_input: str):
    chat_log.append({'role': 'user', 'content': user_input})
    
    response_stream = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=chat_log,
        temperature=0.6,
        stream=True
    )
    return response_stream
    
