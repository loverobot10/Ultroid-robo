from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("sensei ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("EVERyBOdy")
        await asyncio.sleep(0.3)
        await event.edit("iZ")
        await asyncio.sleep(0.2)
        await event.edit("SeNSei")
        await asyncio.sleep(0.5)
        await event.edit("UNtIL ")
        await asyncio.sleep(0.2)
        await event.edit("BAJRANG KE LAUNDE")
        await asyncio.sleep(0.3)
        await event.edit("ArRivE")
        await asyncio.sleep(0.3)
        await event.edit("🔥🔥🔥")
        await asyncio.sleep(0.3)
        await event.edit("EVERyBOdy iZ SEnsEi UNtIL BajRANG ke LAunde ArRivE 🔥🔥🔥")
