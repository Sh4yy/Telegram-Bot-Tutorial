from Bot import Bot


bot = Bot(token="1173786457:AAF_1DO1vdhq9RiQp5hh3NnsVmLcTtsCjRo")
result = bot.get_me()
print(f'this is {result["username"]}')


bot.send_message(
    chat_id="832404526",
    text="Hey there, how are you?"
)