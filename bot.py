from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("سلام! ربات فعال است ✅")

def main():
    TOKEN = "7394948605:AAEeyxjHN9D7sEzfBYTE-px6sV_ireaBusA"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
