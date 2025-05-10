from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form
from typing import Annotated
from services.chatbot import get_chatbot_response
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory='app/templates')

@app.get('/', response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("layout.html",{"request": request})

@app.post('/')
async def chat(user_input: Annotated[str, Form()]):
    bot_response = get_chatbot_response(user_input)
    return {'response': bot_response}