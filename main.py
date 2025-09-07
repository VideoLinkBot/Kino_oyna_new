from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username if user.username else user.first_name
    await update.message.reply_text(
        f"Assalomu alaykum {username}!\n"
        "Bizning Kino_Oyna botimizga xush kelibsiz 🎬\n\n"
        "📌 Kino olish uchun kodni yozing."
    )

# Foydalanuvchi kod kiritganda
async def get_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text
    await update.message.reply_text(f"Siz kiritgan kod: {code}\n🔍 Tez orada kino yuklanadi...")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_code))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
