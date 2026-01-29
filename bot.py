import telebot 

TOKEN = "8164503096:AAFOvXg--PQsK2x1WXo19r1zR86ThPcOuFA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "it works")
    
    
bot.polling()