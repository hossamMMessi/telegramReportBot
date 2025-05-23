import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# گرفتن توکن از متغیر محیطی
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("❌ متغیر محیطی 'TOKEN' تنظیم نشده. لطفاً آن را در Render تعریف کن.")

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! لینک یا آی‌دی کانال مورد نظر رو بفرست تا متن گزارش آماده کنم."
    )

# دریافت پیام‌های متنی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()

    if user_input.startswith("http") or user_input.startswith("@"):
        report_text = (
            f"🔗 لینک یا آی‌دی گزارش‌شده: {user_input}\n\n"
            "**📝 متن پیشنهادی برای گزارش در تلگرام:**\n"
            "This channel shares private or harmful content including minors. Please investigate and remove it.\n\n"
            "**✉️ متن پیشنهادی برای ایمیل به abuse@telegram.org:**\n"
            "Subject: Urgent Report - Illegal Channel on Telegram\n\n"
            "Dear Telegram Support,\n\n"
            "I would like to report a Telegram channel that is sharing illegal or harmful content involving innocent people or children.\n\n"
            f"Channel link or username: {user_input}\n\n"
            "Please take appropriate action.\n\n"
            "Thank you."
        )
        await update.message.reply_text(report_text)
    else:
        await update.message.reply_text("لطفاً لینک یا آی‌دی معتبر وارد کن (مثلاً t.me/xxx یا @xxx)")

# اجرای اصلی برنامه
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
