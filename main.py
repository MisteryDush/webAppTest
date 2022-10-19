from telebot import TeleBot

TOKEN = "5741444917:AAEet4PlxH7klZNDYv1ZKuEqSDIEjPoY2j8"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def display_welcome_message(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'This is a test')


bot.polling(none_stop=True)
