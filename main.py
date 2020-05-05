from Bot import Bot, UpdateHandler


def message_handler(bot, update):
    
    msg_reply = {
        "hi": "hello",
        "how are you?": "I am good"
    }
    
    username = update['message']['from']['username']
    text = update['message']['text']
    chat_id = update['message']['chat']['id']
    
    print(f'New message from {username}: {text}')
    
    reply = msg_reply.get(text.lower(), "I don't know what to say!")
    bot.send_message(chat_id=chat_id, text=reply)


def update_handler(bot, update):
    
    if 'message' in update:
        message_handler(bot, update)
    
  
bot = Bot(token="1173786457:AAF_1DO1vdhq9RiQp5hh3NnsVmLcTtsCjRo")
updater = UpdateHandler(bot, timeout=3)
updater.register(update_handler)
updater.start_polling()


