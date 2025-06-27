from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = "8175659413:AAHrlBsfPXGrZg-rFYmw7JELpS27mijBqR8"
ADMIN_ID = 6018364152  # آیدی عددی تلگرام خودت (با @userinfobot می‌تونی پیدا کنی)

# دکمه درخواست موقعیت مکانی
location_button = KeyboardButton(text="📍 ارسال موقعیت مکانی", request_location=True)
location_keyboard = ReplyKeyboardMarkup([[location_button]], resize_keyboard=True, one_time_keyboard=True)

# مرحله اول: کاربر /start می‌زنه
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! لطفاً روی دکمه‌ی زیر بزن تا موقعیتت رو ارسال کنی 📡",
        reply_markup=location_keyboard
    )

# مرحله دوم: موقعیت مکانی دریافت می‌شه
async def location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location = update.message.location
    if location:
        lat = location.latitude
        lon = location.longitude

        # ارسال به مدیر
        text = f"📍 لوکیشن جدید دریافت شد:\n👤 کاربر: @{update.effective_user.username}\n🌐 عرض: {lat}\n🌐 طول: {lon}"
        await context.bot.send_message(chat_id=ADMIN_ID, text=text)

        await update.message.reply_text("✅ موقعیت مکانی با موفقیت ارسال شد. ممنون از همکاری‌ات 🙏")

# راه‌اندازی اپ
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.LOCATION, location_handler))

    print("🤖 ربات فعال شد و منتظر /start و لوکیشن کاربران است.")
    app.run_polling()

if __name__ == "__main__":
    main()