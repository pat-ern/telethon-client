from telethon import TelegramClient
from telethon import utils


import sys

# Remember to use your own values from my.telegram.org!
api_id = 9851114
api_hash = 'ef8902ccfbacbfac6a1600342ecf66db'
client = TelegramClient('anon', api_id, api_hash)

async def main():

    me = await client.get_me()
    print('**************************************************')
    print(utils.get_display_name(me))
    print('**************************************************')
    async for message in reversed(client.iter_messages('me')):
        if message.text:
            print(message.date, message.text)

with client:
    client.loop.run_until_complete(main())



