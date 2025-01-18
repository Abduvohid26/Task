from telethon import TelegramClient
from environs import env 
env.read_env()
api_id = env.int('API_ID')
api_hash = env.str('API_HASH')
phone = env.str('PHONE')

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone)

    me = await client.get_me()
    print(f"Foydalanuvchi: {me.username}")
    print(f"Ism: {me.first_name}")
    print(f"ID: {me.id}")
    print(f"Telefon: {me.phone}")

with client:
    client.loop.run_until_complete(main())
