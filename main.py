from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from tests.active_test import *
from data2 import token

start_keyboard = [['/help', '/tests']]
tests_keyboard = [['/back', '/active_test']]
start_markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=False)
tests_markup = ReplyKeyboardMarkup(tests_keyboard, one_time_keyboard=False)


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("back", back))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("tests", tests))
    dp.add_handler(CommandHandler("active_test", first))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('first', first)],
        states={SECOND: [MessageHandler(Filters.regex('^(Да|Нет)$'), second)],
                THIRD: [MessageHandler(Filters.regex('^(Да|Нет)$'), third)],
                FOURTH: [MessageHandler(Filters.regex('^(реализация практических задач|деятельность, направленная на '
                                                      'защиту человеческого достоинства и прав сограждан)$'), fourth)],
                FIFTH: [MessageHandler(Filters.regex('^(религиозными положениями|идеями прекрасного|материальными '
                                                     'соображениями|всеобщим благосостоянием)$'), fifth)],
                SIXTH: [MessageHandler(Filters.regex('^(человека предприимчивого, работящего, наделенного практическим '
                                                     'умом|человека думающего, мечтательного, оторванного от '
                                                     'действительности|человека со способностями руководителя и '
                                                     'организатора)$'), sixth)],
                SEVENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), seventh)],
                EIGHTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), eighth)],
                NINETH: [MessageHandler(Filters.regex('^(Да|Нет)$'), nineth)],
                TENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), tenth)],
                ELEVENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), eleventh)],
                TWELVETH: [MessageHandler(Filters.regex('^(Да|Нет)$'), twelveth)],
                END: [MessageHandler(Filters.regex('^(Да|Нет)$'), end)],
                },
        fallbacks=[CommandHandler('cancel', cancel)])
    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


def start(update, context):
    update.message.reply_text(
        "Привет! Я тестер-бот. Попробуйте пройти пару тестов!",
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
        "Я пока не умею помогать...")


def active_test(update, context):
    pass


if __name__ == '__main__':
    main()
