import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from telethon import TelegramClient, events
from telethon import functions, types
import sys

# Remember to use your own values from my.telegram.org!
api_id = 9851114
api_hash = 'ef8902ccfbacbfac6a1600342ecf66db'
client = TelegramClient('anon', api_id, api_hash)

mensaje = ""

#Si hago esto dentro de main tira error
#local variable referenced before assignment
if len(sys.argv) > 1:
    for i in range(len(sys.argv)-1):
        mensaje += sys.argv[i+1] + ' '
else:
    print('No se puede enviar un mensaje vacio.')

async def main():

    # Getting information about yourself
    me = await client.get_me()
    # You can send messages to yourself...

    if len(sys.argv) > 1:
        message = await client.send_message('me', mensaje)
        print(me.username + ': ' + message.raw_text)

    @client.on(events.NewMessage)

    async def my_event_handler(event):
        if 'hello' in event.raw_text:
            await event.reply('hi!')
    # You can reply to messages directly if you have a message object
    #await message.reply('Cool!')

    # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # You can print the message history of any chat:
    #async for message in client.iter_messages('me'):
        #print(message.id, message.text)

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        #if message.photo:
            #path = await message.download_media()
            #print('File saved to', path)  # printed after download is done

with client:
    client.loop.run_until_complete(main())