import telebot
import yt_dlp
import os
import re

BOT_TOKEN = "8404096353:AAGYRD3678ZmC2MobbwldR9JfvFYVdM23TI"

bot = telebot.TeleBot(BOT_TOKEN)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def is_instagram_url(url):
    pattern = r"(https?://)?(www\.)?instagram\.com/(p|reel|tv)/[\w-]+"
    return bool(re.search(pattern, url))

def download_video(url):
    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s",
        "format": "best[ext=mp4]/best",
        "quiet": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            if os.path.exists(filename):
                return filename
            base = os.path.splitext(filename)[0]
            for ext in ["mp4", "mkv", "webm"]:
                alt = f"{base}.{ext}"
                if os.path.exists(alt):
                    return alt
    except Exception as e:
        print(f"Ошибка: {e}")
    return None

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message,
        "👋 Привет! Я InstaSniper 🎯\n\n"
        "Отправь мне ссылку на видео из Instagram:\n"
        "• Reels\n• Пост с видео\n• IGTV\n\n"
        "⚠️ Только публичные аккаунты!"
    )

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    url = message.text.strip()
    if not is_instagram_url(url):
        bot.reply_to(message, "❌ Пришли ссылку на Instagram видео!")
        return
    status = bot.reply_to(message, "⏳ Скачиваю...")
    filepath = download_video(url)
    if not filepath:
        bot.edit_message_text("❌ Не удалось скачать. Аккаунт приватный?",
            chat_id=status.chat.id, message_id=status.message_id)
        return
    with open(filepath, "rb") as f:
        bot.send_video(message.chat.id, f, caption="✅ Готово!")
    bot.delete_message(status.chat.id, status.message_id)
    os.remove(filepath)

print("🚀 InstaSniper запущен!")
bot.infinity_polling()