from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from flask import Flask, request

TOKEN = "7832991702:AAFuyiAe9_twJk_MncmRNo2mU3O6qTpEWQM"
BOT_USERNAME = "DanielAsistentBot"  # без @
WEBHOOK_URL = f"https://daniel-asistentbot-1.onrender.com/webhook"

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", lambda update, ctx: update.message.reply_text("Привет! Я твой ассистент.")))

# Запускаем Flask-сервер
flask_app = Flask(__name__)

@flask_app.route('/webhook', methods=['POST'])
async def webhook():
    await app.update_queue.put(Update.de_json(request.json, app.bot))
    return "OK"

@flask_app.route('/', methods=['GET'])
def healthcheck():
    return "Bot is running"

if __name__ == '__main__':
    import asyncio
    asyncio.run(app.initialize())
    await app.bot.set_webhook(WEBHOOK_URL)
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
