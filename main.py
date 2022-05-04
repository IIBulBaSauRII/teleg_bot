from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from tests import active_test, attentive_test, sociable_test
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

    conv_handler_active = ConversationHandler(
        entry_points=[CommandHandler('active_test', active_test.active_test)],
        states={active_test.SECOND: [MessageHandler(Filters.regex('^(Да|Нет)$'), active_test.second)],
                active_test.THIRD: [MessageHandler(Filters.regex('^(Да|Нет)$'), active_test.third)],
                active_test.FOURTH: [MessageHandler(Filters.regex(
                    '^(реализация практических задач|деятельность, направленная на '
                    'защиту человеческого достоинства и прав сограждан)$'),
                                        active_test.fourth)],
                active_test.FIFTH: [MessageHandler(Filters.regex(
                    '^(религиозными положениями|идеями прекрасного|материальными '
                    'соображениями|всеобщим благосостоянием)$'), active_test.fifth)],
                active_test.SIXTH: [MessageHandler(Filters.regex(
                    '^(человека предприимчивого, работящего, наделенного практическим '
                    'умом|человека думающего, мечтательного, оторванного от '
                    'действительности|человека со способностями руководителя и '
                    'организатора)$'), active_test.sixth)],
                active_test.SEVENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), active_test.seventh)],
                active_test.EIGHTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), active_test.eighth)],
                active_test.NINETH: [MessageHandler(Filters.regex('^(Да|Нет)$'), active_test.nineth)],
                active_test.TENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), active_test.tenth)],
                active_test.ELEVENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), active_test.eleventh)],
                active_test.TWELVETH: [MessageHandler(Filters.regex('^(Да|Нет)$'), active_test.twelveth)],
                active_test.END: [MessageHandler(Filters.regex('^(Да|Нет)$'), active_test.end)],
                },
        fallbacks=[CommandHandler('cancel', active_test.cancel)])
    conv_handler_attentive = ConversationHandler(
        entry_points=[CommandHandler('attentive_test', attentive_test.attentive_test)],
        states={attentive_test.SECOND: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.second)],
                attentive_test.THIRD: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.third)],
                attentive_test.FOURTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.fourth)],
                attentive_test.FIFTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.fifth)],
                attentive_test.SIXTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.sixth)],
                attentive_test.SEVENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.seventh)],
                attentive_test.EIGHTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.eighth)],
                attentive_test.NINETH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.nineth)],
                attentive_test.TENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.tenth)],
                attentive_test.ELEVENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.eleventh)],
                attentive_test.TWELVETH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.twelveth)],
                attentive_test.THIRTEENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.thirteenth)],
                attentive_test.FOURTEENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.fourteenth)],
                attentive_test.FIFTEENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.fourteenth)],
                attentive_test.END: [MessageHandler(Filters.regex('^(Да|Нет)$'), attentive_test.end)],
                },
        fallbacks=[CommandHandler('cancel', attentive_test.cancel)])
    conv_handler_sociable = ConversationHandler(
        entry_points=[CommandHandler('sociable_test', sociable_test.sociable_test)],
        states={sociable_test.SECOND: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.second)],
                sociable_test.THIRD: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.third)],
                sociable_test.FOURTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.fourth)],
                sociable_test.FIFTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.fifth)],
                sociable_test.SIXTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.sixth)],
                sociable_test.SEVENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.seventh)],
                sociable_test.EIGHTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.eighth)],
                sociable_test.NINETH: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.nineth)],
                sociable_test.TENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.tenth)],
                sociable_test.ELEVENTH: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.eleventh)],
                sociable_test.END: [MessageHandler(Filters.regex('^(Да|Нет)$'), sociable_test.end)],
                },
        fallbacks=[CommandHandler('cancel', sociable_test.cancel)])
    dp.add_handler(conv_handler_active)
    dp.add_handler(conv_handler_attentive)
    dp.add_handler(conv_handler_sociable)

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
        "Введите команду /active_test")


def start_active_test(update, context):
    return active_test


def start_attentive_test(update, context):
    return attentive_test


def start_sociable_test(update, context):
    return sociable_test


if __name__ == '__main__':
    main()