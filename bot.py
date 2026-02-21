from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8035523857:AAGxAwtGFqS_2WdQxYDijFG4Pxcc42lfvqU"

app = Flask(__name__)
application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛍 Welcome to Kaviya Store Bot!\nUse /menu")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 Diamond Pack - Rs.1000\n📦 Elite Pack - Rs.2000")

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("menu", menu))

@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "ok"

@app.route("/")
def home():
    return "Bot Running!"

if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url="https://YOUR_RENDER_URL/" + TOKEN
    )
