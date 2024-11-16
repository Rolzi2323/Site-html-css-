from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

# Обработчик команды /start
async def start(update, context):
    # Создаем кнопку с типом web_app для открытия сайта в Telegram Mini App
    keyboard = [
        [InlineKeyboardButton("Перейти на сайт", web_app={'url': "https://rolzi2323.github.io/html-web/"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с кнопкой
    await update.message.reply_text("Привет! Нажми на кнопку ниже, чтобы перейти на сайт.", reply_markup=reply_markup)

# Настройка бота
def main():
    application = Application.builder().token("8191506761:AAEDkwSZ4fqtdTIAH5ux7mtgYFmC14GUPy0").build()
    
    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
