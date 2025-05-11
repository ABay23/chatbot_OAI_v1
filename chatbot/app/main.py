from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form, WebSocket
from typing import Annotated
from services.chatbot import get_chatbot_response, activate_websocket
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory='app/templates')

@app.get('/', response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html",{"request": request})

'''Web socket'''
@app.websocket("/ws")
async def chat(websocket: WebSocket):
    await activate_websocket(websocket)

@app.post('/', response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
    bot_response = get_chatbot_response(request, user_input)
    return bot_response