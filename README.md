# Daniel.Asistentbot
from telegram.ext import ApplicationBuilder, CommandHandler
import asyncio
import os

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Привет, я твой бот!")

async def help_command(update, context):
    await update.message.reply_text("Команды: /start, /help")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
