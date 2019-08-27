
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import settings

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s', 
                    level = logging.INFO, 
                    filename = 'bot.log'
                    )
#
def greet_user(bot, update):
    text = 'вызван /start'
    #print(text) # вывод текста в консоль
    update.message.reply_text(text) # Отправка текста ботом
    logging.info(text)

def talk_to_me(bot, update):
    user_text = update.message.text # считывание текста от пользователя
    #update.message.reply_text(user_text)
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    #print(user_text)
    update.message.reply_text(user_text)
    logging.info(user_text)

def main():
    mybot = Updater(settings.API_KEY) # API 
    
    logging.info('бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    #
<<<<<<< HEAD
    
=======
    #
>>>>>>> a9a382bb386ff11b8c79d2d8eb20adc4d8d8e301
    dp.add_handler(MessageHandler(Filters.text , talk_to_me))

    mybot.start_polling()
    mybot.idle()
    
main()


