from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import openai
import os

openai.api_key = os.getenv(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)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши мне что-нибудь, и я отвечу.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_text}]
        )
        bot_reply = response['choices'][0]['message']['content']
    except Exception as e:
        bot_reply = "Произошла ошибка при обращении к OpenAI API."

    await update.message.reply_text(bot_reply)

if __name__ == '__main__':
    TELEGRAM_TOKEN = os.getenv("7973342368:AAEBm9dLA2wlVgyELu_pe01TWjVMwNa4nlc")
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    application.run_polling()
