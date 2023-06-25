from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup


menu = [["Add ball"], ["Get all balls", "Add user"]]

reply_markup = ReplyKeyboardMarkup(menu)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}', reply_markup=reply_markup)


app = ApplicationBuilder().token("5921682655:AAFIpED0TZUCMfzWKTypHD2JGqAtngdrqB4").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(menu, pattern='main'))

app.run_polling()