from fastapi import FastAPI, Form
from typing import Annotated
from services.chatbot import get_chatbot_response

app = FastAPI()

@app.post('/')
async def chat(user_input: Annotated[str, Form()]):
    bot_response = get_chatbot_response(user_input)
    return {'response': bot_response}