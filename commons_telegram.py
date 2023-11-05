import telegram
# from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from commons import *


# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     await update.message.reply_html(
#         rf"Hi {user.mention_html()}!",
#         reply_markup=ForceReply(selective=True),
#     )
#
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /help is issued."""
#     await update.message.reply_text("Help!")
#
# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Echo the user message."""
#     await update.message.reply_text(update.message.text)
#

def get_telegram_token():
    return settings.TelegramBotToken


def get_telegram_chat_id():
    return settings.TelegramChatId


def initialize_telegram():
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(settings.TelegramBotToken).connect_timeout(30).read_timeout(
        30).write_timeout(30).build()

    # # on different commands - answer in Telegram
    # application.add_handler(CommandHandler("start", start_command))
    # application.add_handler(CommandHandler("help", help_command))
    #
    # # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    #
    # # Run the bot until the user presses Ctrl-C
    # application.run_polling(allowed_updates=Update.ALL_TYPES)

    settings.TelegramBot = application.bot


def get_telegram_bot():
    return settings.TelegramBot


async def log_with_bot(level, message):
    UserId = 'ALGO'
    # UserId = str(settings.DataUserId)
    UserId = str(UserId) + ' @ ' + str(datetime.datetime.now().replace(microsecond=0))

    func_name = get_calling_function_name()
    message = str(func_name) + ' : ' + str(message)

    log(level, message)

    chat_id = get_telegram_chat_id()
    try:
        if level == 'e':
            await settings.TelegramBot.send_message(chat_id=chat_id,
                                                    text=str("`" + level + " : " + UserId + " : " + message + "`"),
                                                    parse_mode='Markdown')

        elif level == 'w':
            await settings.TelegramBot.send_message(chat_id=chat_id,
                                                    text=str("<u>" + level + " : " + UserId + " : " + message + "</u>"),
                                                    parse_mode='HTML')

        else:
            await settings.TelegramBot.send_message(chat_id=chat_id,
                                                    text=str(level + " : " + UserId + " : " + message))

    except Exception as e:
        log('e', e)
