from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

ATTENTIVE_TEST, SECOND, THIRD, FOURTH, FIFTH, SIXTH, SEVENTH, EIGHTH, NINETH, TENTH, ELEVENTH, END = range(12)
tests_keyboard = [['/back', '/active_test', '/attentive_test', '/sociable_test']]
tests_markup = ReplyKeyboardMarkup(tests_keyboard, one_time_keyboard=False)


def sociable_test(update, context):
    global points
    points = 0
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Вы любите больше слушать, чем говорить?',
        reply_markup=markup_key)
    return SECOND


def second(update, context):
    global points
    if update.message.text == 'Нет':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Вы всегда можете найти тему для разговора даже с незнакомым человеком?',
        reply_markup=markup_key)
    return THIRD


def third(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Вы всегда внимательно слушаете собеседника?',
        reply_markup=markup_key)
    return FOURTH


def fourth(update, context):
    global points
    if update.message.text == 'реализация практических задач':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Любите ли вы давать советы?',
        reply_markup=markup_key)
    return FIFTH


def fifth(update, context):
    global points
    if update.message.text == 'всеобщим благосостоянием':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Если тема разговора вам неинтересна, станете ли показывать это собеседнику?',
        reply_markup=markup_key)
    return SIXTH


def sixth(update, context):
    global points
    if update.message.text == 'человека думающего, мечтательного, оторванного от действительности':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Раздражаетесь, когда вас не слушают?',
        reply_markup=markup_key)
    return SEVENTH


def seventh(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'У вас есть собственное мнение по каждому вопросу?',
        reply_markup=markup_key)
    return EIGHTH


def eighth(update, context):
    global points
    if update.message.text == 'Нет':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Если тема разговора вам незнакома, станете ли ее развивать?',
        reply_markup=markup_key)
    return NINETH


def nineth(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Вы любите быть центром внимания?',
        reply_markup=markup_key)
    return TENTH


def tenth(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Есть ли хотя бы три предмета, по которым вы обладаете достаточно прочными знаниями?',
        reply_markup=markup_key)
    return ELEVENTH


def eleventh(update, context):
    global points
    if update.message.text == 'Нет':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Вы хороший оратор?',
        reply_markup=markup_key)
    return END


def cancel(update, context):
    global points
    points = 0
    update.message.reply_text(
        'Вы закрыли тест',
        reply_markup=tests_markup)
    return ConversationHandler.END


def end(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    if points < 4:
        update.message.reply_text(
            'Трудно сказать, то ли вы молчун, из которого не вытянешь ни слова, то ли настолько общительны, что вас '
            'стараются избегать, но факт остается фактом: общаться с вами далеко не всегда приятно, но всегда крайне '
            'тяжело. Вам следовало бы над этим задуматься.', reply_markup=tests_markup)
    elif points < 10:
        update.message.reply_text(
            'Вы, может быть, и не слишком общительный человек, но почти всегда внимательный и приятный собеседник, '
            'хотя можете быть и весьма рассеянным, когда не в духе, но вы не требуете в такие минуты особого внимания '
            'к вашей персоне от окружающих.', reply_markup=tests_markup)
    else:
        update.message.reply_text(
            'Вы, наверное, один из самых приятных в общении людей. Вряд ли друзья могут без вас обойтись. '
            'Это прекрасно. Возникает только один вопрос: вам действительно приятна все время ваша роль или иногда вам '
            'приходится играть, как на сцене?..', reply_markup=tests_markup)
    points = 0

    return ConversationHandler.END
