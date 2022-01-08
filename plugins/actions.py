import heroku3 
from config import Tellybots, ACCESS_CHANNEL
from telethon import events , Button
from decouple import config

from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telegraph import upload_file
from telethon.errors.rpcerrorlist import FloodWaitError

def mention(name, id):
    return f'[{name}](tg://user?id={id})'

async def LOG_START(event, ps_name):
    LOG_ID = config("LOG_ID", default=None)
    chat = LOG_ID
    if not str(LOG_ID).startswith("-100"):
        chat = int("-100" + str(LOG_ID))
    Tag = mention(event.sender.first_name, event.sender_id)
    text = f'{ps_name}\n\nUSER: {Tag}'
    xx = await event.client.send_message(int(chat), text, link_preview=False)
    return xx

async def LOG_END(event, ps_name):
    LOG_ID = config("LOG_ID", default=None)
    chat = LOG_ID
    if not str(LOG_ID).startswith("-100"):
        chat = int("-100" + str(LOG_ID))
    await event.client.send_message(int(chat), f'{ps_name}', link_preview=False)
