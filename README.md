# InstaSniper — Instagram Video Downloader Bot

**English** | [Español](README.es.md)

A Telegram bot that downloads videos from Instagram (Reels, posts, IGTV) using yt-dlp and sends them back to the user.

## How it works

1. User sends an Instagram video URL to the bot
2. Bot validates the URL format
3. yt-dlp downloads the video (best quality MP4)
4. Bot checks file size (Telegram bot limit: 50 MB)
5. Bot sends the video back to the user
6. Temporary file is deleted

## Technologies

- **Python 3.10+**
- **pyTelegramBotAPI** (telebot) — Telegram Bot API wrapper
- **yt-dlp** — video downloader (supports Instagram and many other sites)
- **python-dotenv** — environment variable loading

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/segamania90-crypto/instagram-bot.git
cd instagram-bot

# 2. Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env and add your TELEGRAM_BOT_TOKEN

# 5. Run the bot
python bot.py
```

## Notes

- **Cookies are optional**; for private accounts or when errors occur, place an exported `cookies.txt` (Netscape format) next to `bot.py` named `instagram_cookies.txt`; the file is in `.gitignore` and must not be committed.
- If downloads fail, first update yt-dlp:
  ```bash
  pip install -U yt-dlp
  ```
- **Status**: `Code updated in November 2026 (dependencies, token via .env), not re-tested after the update. Instagram changes often; the bot may need cookies or a newer yt-dlp.`
- **Disclaimer**: Educational project, built with LLM assistance, for personal use only. Respect Instagram's Terms of Service and copyright laws. The author is not responsible for misuse.