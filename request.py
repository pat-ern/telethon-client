import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from telethon import TelegramClient, events, utils

api_id = 9851114
api_hash = 'ef8902ccfbacbfac6a1600342ecf66db'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):

    dest = await client.get_entity(event.from_id.user_id)
    nombre = utils.get_display_name(dest)

    print(f"{nombre}: {event.raw_text}")
    #print(f"{event.date} {event.from_id.user_id} {event.raw_text}")
    if 'hello' in event.raw_text:
        await event.reply('hi!')

client.start()
client.run_until_disconnected()