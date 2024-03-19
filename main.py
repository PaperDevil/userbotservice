import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from pyrogram import Client
from pyrogram.enums.parse_mode import ParseMode

app = FastAPI()


@app.get('/chats/{chat_id}')
async def get_chat(chat_id: int | str):
    async with Client('authorization') as app:
        chat = await app.get_chat(chat_id)
        print(chat)
        return JSONResponse({}, status_code=200)


@app.post('/chats/{chat_id}/send_message')
async def send_message(chat_id: int | str, message: str):
    async with Client('authorization') as app:
        await app.get_chat(chat_id)
        await app.send_message(chat_id, message, parse_mode=ParseMode.HTML)
        return JSONResponse({'status': 'OK'}, status_code=200)


@app.get('/chats')
async def get_chats():
    async with Client('authorization') as app:
        chats = {}
        async for dialog in app.get_dialogs():
            if dialog.chat.title:
                chats[dialog.chat.id] = {
                    'id': dialog.chat.id,
                    'title': dialog.chat.title,
                    'members': dialog.chat.members_count,
                    'can_send_message': dialog.chat.permissions.can_send_messages
                }

        return JSONResponse(chats, status_code=200)


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8001, log_level="info")
