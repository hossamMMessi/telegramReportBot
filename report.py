from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7564698406:AAFm_EnJ89arMkbjgJ6xGt5SMJGlXO4Z7iU"

# پیام شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "سلام! 👋 من بهت کمک می‌کنم یک کانال غیرقانونی رو به تلگرام و پلیس فتا گزارش بدی.\n\n"
        "لطفاً لینک یا آی‌دی کانال مورد نظر رو بفرست 👇"
    )

# پیام کاربر = لینک کانال → تولید متن ریپورت
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text.strip()
    
    if user_input.startswith("http") or user_input.startswith("@"):
        # تولید پیام ایمیل و ریپورت
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
        await update.message.reply_text("لطفاً یک لینک یا آی‌دی معتبر وارد کن (مثلاً t.me/xxxx یا @xxxx)")

# اجرای برنامه
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
