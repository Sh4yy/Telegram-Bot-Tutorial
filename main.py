from Bot import Bot


bot = Bot(token="1173786457:AAF_1DO1vdhq9RiQp5hh3NnsVmLcTtsCjRo")
result = bot.get_me()
print(f'this is {result["username"]}')


# bot.send_message(
#     chat_id="832404526",
#     text="Hey there, how are you?"
# )

def process_update(update):
    if 'message' not in update:
        print('not a message update')
        return
    
    first_name = update['message']['from']['first_name']
    username = update['message']['from']['username']
    text = update['message']['text']
    
    print(f'New message from {username}: {text}')
    

result = bot.get_updates()
for update in result:
    process_update(update)