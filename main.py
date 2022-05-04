from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import conv_handlers
from data2 import token

start_keyboard = [['/help', '/tests']]
tests_keyboard = [['/back', '/active_test', '/attentive_test', '/sociable_test']]
start_markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=False)
tests_markup = ReplyKeyboardMarkup(tests_keyboard, one_time_keyboard=False)
points = 0


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("back", back))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("tests", tests))
    dp.add_handler(conv_handlers.conv_handler_active)
    dp.add_handler(conv_handlers.conv_handler_attentive)
    dp.add_handler(conv_handlers.conv_handler_sociable)

    updater.start_polling()
    updater.idle()


def start(update, context):
    update.message.reply_text(
        "Привет! Я бот Евлампий. Если хочешь узнать что нибудь новое о себе, то ты по адрессу! "
        "Ты ответишь на несколько моих вопросов, а я вынесу вердикт о тебе!",
        reply_markup=start_markup)


def back(update, context):
    update.message.reply_text(
        "Вы вернулись назад",
        reply_markup=start_markup)


def tests(update, context):
    update.message.reply_text(
        "Выбери тест который хочешь пройти.",
        reply_markup=tests_markup)


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def help(update, context):
    update.message.reply_text(
        "Введи команду /tests, после выберете желаемый тест. "
        "Виды тестов: "
        "/active_test - тест насколько вы активный человек "
        "/attentive_test - тест наксолько вы внимательный "
        "/sociable_test - тест насколько вы общительный "
        "Новые тесты будут появляться с обновлениями! "
        "Версия бота 1.0")


if __name__ == '__main__':
    main()
