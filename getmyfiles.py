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
        def callback(current, total):
            print('Downloaded', current, 'out of', total,
                'bytes: {:.2%}'.format(current / total))

        path = await client.download_media(message, progress_callback=callback)
        print('SAVED FILE: ', path)

with client:
    client.loop.run_until_complete(main())