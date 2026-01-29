import telebot 

TOKEN = " "

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "it works")
    
    
bot.polling()