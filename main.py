import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логгирования (записывает ошибки в консоль)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Все команды PostgreSQL, которые знает бот
SQL_COMMANDS = {
    'SELECT': "SELECT * FROM table_name; — выбрать все данные из таблицы",
    'INSERT': "INSERT INTO table (column) VALUES ('value'); — добавить запись",
    'UPDATE': "UPDATE table SET column='value' WHERE id=1; — изменить запись",
    'DELETE': "DELETE FROM table WHERE id=1; — удалить запись",
    # Можно добавить свои команды!
}

# Кнопки для быстрого выбора команд
keyboard = [["SELECT", "INSERT"], ["UPDATE", "DELETE"]]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот-помощник по SQL.\nВыбери команду:",
        reply_markup=reply_markup
    )

# Обработчик текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.upper()
    if text in SQL_COMMANDS:
        await update.message.reply_text(SQL_COMMANDS[text])
    else:
        await update.message.reply_text("Не знаю такой команды 😢")

# Главная функция
def main():
    # Создаем бота и указываем токен
    application = Application.builder().token("YOUR_TOKEN").build()
    
    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    print("Бот запущен! Для остановки нажмите Ctrl+C")
    main()