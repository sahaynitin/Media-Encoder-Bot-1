#Logging events on tg---------------------------------------------------------------------------------------------

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
