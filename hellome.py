from telethon import TelegramClient

#Use your own values from my.telegram.org
api_id = 9851114
api_hash = 'ef8902ccfbacbfac6a1600342ecf66db'

#The first parameter is the .session file name (absolute path allowed)

with TelegramClient('anon', api_id, api_hash) as client:
	client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))
