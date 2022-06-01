import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from telethon import TelegramClient, events

api_id = 9851114
api_hash = 'ef8902ccfbacbfac6a1600342ecf66db'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):

    print(event.date)
    print(event.raw_text)
    print(event.id)
    print(event.from_id)
    print(event.peer_id.user_id)
    if 'hello' in event.raw_text:
        await event.reply('hi!')

client.start()
client.run_until_disconnected()