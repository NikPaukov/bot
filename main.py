from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import logging
import config
import os

PORT = int(os.environ.get('PORT', 5000))
TOKEN = config.TOKEN
userDB = dict()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def help(update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.username

    if user_id not in userDB.keys():
        userDB.update({user_id: username})
    if 'vm.tiktok.com' in update.message.text:
        rand_user = str(random.randint(0, len(userDB)) - 1)
        update.message.reply_text("[Згоден, " + userDB[rand_user] + "?" + rand_user + "](tg://user?id=" + rand_user + ")",
                                  parse_mode="Markdown")


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(MessageHandler(Filters.text, help))

    # on noncommand i.e message - echo the message on Telegram

    # log all errors

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://tt-vanya-bot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

# import telebot
# import random
# import config

# import os
# PORT = int(os.environ.get('PORT', 5000))
#
# bot = telebot.TeleBot(config.TOKEN)
#
# @bot.message_handler(content_types=['text'])
# def getId(message):
#     user_id= message.from_user.id
#     isBot = message.from_user.is_bot
#     with open(str(message.chat.id)+'.txt', 'a') as f:
#         pass
#     with open(str(message.chat.id)+'.txt') as f:
#         lines = f.readline()
#         lines_split = lines.split(" ");
#         if str(user_id) not in lines:
#             with open(str(message.chat.id)+'.txt', "a") as f1:
#                 if not isBot:
#                     f1.write(' '+str(user_id))
#     if'vm.tiktok.com' in message.text:
#         rand_user_id = str(lines_split[random.randint(1, len(lines_split))-1])
#         user = bot.get_chat_member(int(rand_user_id), int(rand_user_id)).user.first_name
#         bot.send_message(message.chat.id,
#             "[Згоден, "+ user+"?](tg://user?id="+rand_user_id+")",
#             parse_mode="Markdown")
#
#
# bot.polling(none_stop=True)
#
