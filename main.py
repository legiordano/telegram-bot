import logging
from telegram.ext import Updater, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = 'TOKEN_DEL_BOT'

def greeting_answer(update, context):
    update.message.reply_text('¡Hola! Soy un bot de prueba.')

def main():
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, greeting_answer))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
