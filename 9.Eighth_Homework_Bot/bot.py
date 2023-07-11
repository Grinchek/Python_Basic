
import telebot
import yt_dlp
# Встановити токен вашого телеграм-бота
bot_token = 'YOUR_BOT_TOKEN'

# Створити екземпляр телеграм-бота
bot = telebot.TeleBot('6394570120:AAHwDpG6jMy0pUMmVr-C3oR2zKpBZQmhUWg')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Відправити привітання при команді /start
    bot.reply_to(message, "Привіт! Відправте посилання на відео з YouTube.")


@bot.message_handler(func=lambda message: True)
def download_video_or_audio(message):
    video_url = message.text

    # Створити об'єкт для завантаження відео з YouTube
    ydl_opts = {
        'format': '139',
        'outtmpl': '%(title)s.%(ext)s',  # Назва файлу
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get('title', None)

        if video_title:
            markup = telebot.types.InlineKeyboardMarkup()
            video_button = telebot.types.InlineKeyboardButton(
                text='Відео', callback_data='video')
            audio_button = telebot.types.InlineKeyboardButton(
                text='Аудіо', callback_data='audio')
            markup.add(video_button, audio_button)

            bot.reply_to(
                message, f"{message.text}", reply_markup=markup)
        else:
            bot.reply_to(message, "Не вдалося отримати інформацію про відео.")


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'video':
        download_format = 'bestvideo+bestaudio/best'
    elif call.data == 'audio':
        download_format = 'bestaudio/best'
    else:
        return

    # Отримати посилання на відео з повідомлення
    video_url = call.message.text.split('\n')[0]

    # Завантажити відео або аудіо
    with yt_dlp.YoutubeDL({'format': download_format}) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)

    bot.answer_callback_query(call.id, text="Завантаження завершено!")


# Запустити телеграм-бота
bot.polling()
