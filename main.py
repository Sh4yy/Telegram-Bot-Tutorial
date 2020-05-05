from Bot import Bot, UpdateHandler


bot = Bot(token="1173786457:AAF_1DO1vdhq9RiQp5hh3NnsVmLcTtsCjRo")
result = bot.get_me()


# def process_update(update):
#     if 'message' not in update:
#         print('not a message update')
#         return
    
#     username = update['message']['from']['username']
#     text = update['message']['text']
    
#     print(f'New message from {username}: {text}')
    

# result = bot.get_updates()
# for update in result:
#     process_update(update)

def message_handler(update):
    
    if 'message' not in update:
        print('not a message update')
        return
    
    username = update['message']['from']['username']
    text = update['message']['text']
    
    print(f'New message from {username}: {text}')
    
    
updater = UpdateHandler(bot, timeout=3)
updater.register(message_handler)
updater.start_polling()


