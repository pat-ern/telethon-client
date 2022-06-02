from telethon import TelegramClient, utils
import sys

# Remember to use your own values from my.telegram.org!
api_id = 9851114
api_hash = 'ef8902ccfbacbfac6a1600342ecf66db'
client = TelegramClient('anon', api_id, api_hash)

origen = sys.argv[1]

async def main():

    me = await client.get_me()

    dest = await client.get_entity(sys.argv[1])

    async for message in reversed(client.iter_messages(dest)):
        #print(message.date, message.peer_id.user_id, message.text)
        if message.from_id == None:
            id = message.peer_id.user_id
        else:
            id = me.id
        print(id, message.text)

with client:
    client.loop.run_until_complete(main())
