from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask, request
import asyncio
import os

TOKEN = "7832991702:AAFuyiAe9_twJk_MncmRNo2mU3O6qTpEWQM"
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://daniel-asistentbot-1.onrender.com{WEBHOOK_PATH}"

# Создание Telegram-приложения
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", lambda update, context: update.message.reply_text("Привет! Я твой ассистент.")))

# Flask-приложение
flask_app = Flask(__name__)

@flask_app.route(WEBHOOK_PATH, methods=["POST"])
async def webhook():
    update = Update.de_json(request.json, application.bot)
    await application.update_queue.put(update)
    return "ok"

@flask_app.route("/", methods=["GET"])
def index():
    return "Бот работает!"

async def main():
    await application.initialize()
    await application.bot.set_webhook(url=WEBHOOK_URL)
    await application.start()

if __name__ == "__main__":
    # Запуск Telegram части
    asyncio.run(main())
    
    # Запуск Flask-сервера
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
