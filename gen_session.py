import asyncio
from pyrogram import Client

api_id = 28676867
api_hash = "2b4f65094245f2fe409c8c0a240fe5e2"


async def main():
    async with Client("authorization", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())