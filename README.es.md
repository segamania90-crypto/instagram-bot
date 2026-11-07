# InstaSniper — Bot Descargador de Videos de Instagram

[English](README.md) | **Español**

Un bot de Telegram que descarga videos de Instagram (Reels, publicaciones, IGTV) usando yt-dlp y los envía al usuario.

## Cómo funciona

1. El usuario envía una URL de video de Instagram al bot
2. El bot valida el formato de la URL
3. yt-dlp descarga el video (mejor calidad MP4)
4. El bot verifica el tamaño del archivo (límite de bot de Telegram: 50 MB)
5. El bot envía el video de vuelta al usuario
6. El archivo temporal se elimina

## Tecnologías

- **Python 3.10+**
- **pyTelegramBotAPI** (telebot) — wrapper de la API de Telegram Bot
- **yt-dlp** — descargador de videos (soporta Instagram y muchos otros sitios)
- **python-dotenv** — carga de variables de entorno

## Inicio Rápido

```bash
# 1. Clonar el repositorio
git clone https://github.com/segamania90-crypto/instagram-bot.git
cd instagram-bot

# 2. Crear y activar entorno virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar entorno
cp .env.example .env
# Editar .env y añadir tu TELEGRAM_BOT_TOKEN

# 5. Ejecutar el bot
python bot.py
```

## Notas

- **Las cookies son opcionales**; para cuentas privadas o cuando ocurran errores, coloca un archivo `cookies.txt` exportado (formato Netscape) junto a `bot.py` con el nombre `instagram_cookies.txt`; el archivo está en `.gitignore` y no debe ser committeado.
- Si las descargas fallan, primero actualiza yt-dlp:
  ```bash
  pip install -U yt-dlp
  ```
- **Estado**: `Code updated in November 2026 (dependencies, token via .env), not re-tested after the update. Instagram changes often; the bot may need cookies or a newer yt-dlp.` (Código actualizado en noviembre 2026 (dependencias, token vía .env), no vuelto a probar tras la actualización. Instagram cambia a menudo; el bot puede necesitar cookies o un yt-dlp más reciente.)
- **Descargo de responsabilidad**: Proyecto educativo, creado con ayuda de LLM, solo para uso personal. Respeta los Términos de Servicio de Instagram y las leyes de derechos de autor. El autor no se hace responsable del mal uso.