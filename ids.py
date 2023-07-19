from telethon.sync import TelegramClient

api_id = 'api id'
api_hash = 'hash'

phone = '+55number'
session_file = 'session'

client = TelegramClient(session_file, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

groups = []
for dialog in client.iter_dialogs():
    if dialog.is_group:
        groups.append(dialog)

with open('ids.txt', 'w', encoding='utf-8') as file:
    for group in groups:
        file.write(f"ID do Grupo: {group.id}, Título: {group.title}\n")

client.disconnect()
