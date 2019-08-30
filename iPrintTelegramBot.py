
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
import logging
from telegram import ReplyKeyboardMarkup

import os

import settings

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s', 
                    level = logging.INFO, 
                    filename = 'bot.log'
                    )
#
def greet_user(bot, update, user_data):
    text = 'вызван /start'
    #print(text) # вывод текста в консоль
    #update.message.reply_text(text) # Отправка текста ботом
    my_keyboard = ReplyKeyboardMarkup([['Прислать документы', 'привет']])
    update.message.reply_text(text, reply_markup = my_keyboard)
    #logging.info(text)

def talk_to_me(bot, update):
    user_text = update.message.text # считывание текста от пользователя
    #update.message.reply_text(user_text)
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    #print(user_text)
    update.message.reply_text(user_text)
    #logging.info(user_text)

def send_documents(bot, update, user_data):
    update.message.reply_text(settings.Send_Document_Text)
    os.makedirs('downloads', exist_ok = True)   
    newFile = bot.get_file(update.message.document.file_id) # пытался взять формат файла 
    print(newFile)
    format_file = str(newFile)
    format_file = format_file.split('.')
    format_file = format_file[-1]
    format_file = str(format_file)
    format_file = format_file[:-2] 
    update.message.reply_text('файл с расшерением .{}'.format(format_file))
    document_file = bot.getFile(update.message.document.file_id)
    filename_document = os.path.join('downloads', '{}.{}'.format(document_file.file_id, format_file))
    print(filename_document)
    document_file.download(filename_document)
    update.message.reply_text("файл сохранен")

def send_photo(bot, update, user_data):  # возможно можно удалить 
    os.makedirs('downloads_photo', exist_ok = True)
    photo_file = bot.getFile(update.message.photo[-1].file_id)
    filename_photo = os.path.join('downloads_photo', '{}.jpg'.format(photo_file.file_id))
    photo_file.download(filename_photo)
    update.message.reply_text("фото сохранено")
    
def main():
    mybot = Updater(settings.API_KEY) # API 
    
    #logging.info('бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(RegexHandler('^(Прислать документы)$',greet_user, pass_user_data=True)) # начало строки^   конец$
    dp.add_handler(RegexHandler('^(привет)$',send_documents, pass_user_data=True)) 
    dp.add_handler(MessageHandler(Filters.document,send_documents,pass_user_data=True)) 
    dp.add_handler(MessageHandler(Filters.photo,send_photo,pass_user_data=True))
#gg
    dp.add_handler(MessageHandler(Filters.text , talk_to_me))

    mybot.start_polling()
    mybot.idle()
    
main()


