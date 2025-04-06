
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7535665268:AAFTBdOjciCRWNiDfLP0LSXDVon18JoJs38"
CHANNEL_LINK = "https://t.me/+63phcsesEjZmNjBi"

logging.basicConfig(level=logging.INFO)
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Так", callback_data="age_yes")],
        [InlineKeyboardButton("Ні", callback_data="age_no")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "На каналі контент 18+. Підтвердіть свій вік для вашої ж відповідальності:",
        reply_markup=reply_markup
    )

async def age_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "age_yes":
        user_data[query.from_user.id] = True
        await query.edit_message_text("Дякуємо за підтвердження. Ласкаво просимо!")
        await context.bot.send_message(chat_id=query.from_user.id, text=f"Ось посилання на канал: {CHANNEL_LINK}")
    else:
        await query.edit_message_text("Доступ заборонено.")

async def age_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("age", age_command))
    app.add_handler(CallbackQueryHandler(age_callback))
    print("Бот запущено...")
    app.run_polling()
