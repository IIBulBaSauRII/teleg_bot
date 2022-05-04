from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

ATTENTIVE_TEST, SECOND, THIRD, FOURTH, FIFTH, SIXTH, SEVENTH, EIGHTH, NINETH, TENTH, ELEVENTH, TWELVETH, \
THIRTEENTH, FOURTEENTH, FIFTEENTH, END = range(16)
tests_keyboard = [['/back', '/active_test', '/attentive_test', '/sociable_test']]
tests_markup = ReplyKeyboardMarkup(tests_keyboard, one_time_keyboard=False)


def attentive_test(update, context):
    global points
    points = 0
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Часто ли вы проигрываете из-за невнимания?',
        reply_markup=markup_key)
    return SECOND


def second(update, context):
    global points
    if update.message.text == 'Нет':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Разыгрывают ли вас друзья и знакомые?',
        reply_markup=markup_key)
    return THIRD


def third(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Умеете ли вы заниматься каким-либо делом и одновременно слушать то, о чем говорят вокруг вас?',
        reply_markup=markup_key)
    return FOURTH


def fourth(update, context):
    global points
    if update.message.text == 'реализация практических задач':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Находили ли вы когда-нибудь на улице деньги или ключи?',
        reply_markup=markup_key)
    return FIFTH


def fifth(update, context):
    global points
    if update.message.text == 'всеобщим благосостоянием':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Смотрите ли внимательно по сторонам, когда переходите улицу?',
        reply_markup=markup_key)
    return SIXTH


def sixth(update, context):
    global points
    if update.message.text == 'человека думающего, мечтательного, оторванного от действительности':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Способны ли вспомнить в деталях фильм, который посмотрели два дня назад?',
        reply_markup=markup_key)
    return SEVENTH


def seventh(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Раздражает ли вас, когда кто-то отрывает вас от чтения книги, газеты, просмотра телевизора или '
        'какого-либо иного занятия?',
        reply_markup=markup_key)
    return EIGHTH


def eighth(update, context):
    global points
    if update.message.text == 'Нет':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Проверяете ли сдачу в магазине сразу у кассы?',
        reply_markup=markup_key)
    return NINETH


def nineth(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Быстро ли находите в квартире нужную вещь?',
        reply_markup=markup_key)
    return TENTH


def tenth(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Вздрагиваете ли, если вас внезапно кто-то окликнет на улице?',
        reply_markup=markup_key)
    return ELEVENTH


def eleventh(update, context):
    global points
    if update.message.text == 'Нет':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Бывает ли, что вы одного человека принимаете за другого?',
        reply_markup=markup_key)
    return TWELVETH


def twelveth(update, context):
    global points
    if update.message.text == 'Нет':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Увлекшись беседой, можете ли пропустить нужную вам остановку?',
        reply_markup=markup_key)
    return END


def thirteenth(update, context):
    global points
    if update.message.text == 'Нет':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Можете ли вы, не мешкая назвать даты рождения ваших близких?',
        reply_markup=markup_key)
    return END


def fourteenth(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Легко ли вы пробуждаетесь ото сна?',
        reply_markup=markup_key)
    return END


def fifteenth(update, context):
    global points
    if update.message.text == 'Да':
        points += 1
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Найдете ли вы в большом городе без посторонней помощи то место (музей, кинотеатр, магазин, учреждение), '
        'где побывали единожды в прошлом году?',
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
    if points < 5:
        update.message.reply_text(
            'Вы очень рассеянны, и это является причиной многих неприятностей в вашей жизни. Когда вас в этом '
            'упрекают, вы, бывает, отвечаете с улыбкой, что просто мечтательны и не придаете значения всяким '
            '«пустякам». Пустякам ли? Ведь из-за вашей невнимательности неприятности терпят и окружающие - что '
            'значит, например, забыть завернуть водопроводный кран или потерять взятую у кого-то редкую книгу? '
            'Бывает, что люди даже бравируют своей рассеянностью, хотя, если разобраться, это качество отрицательное. '
            'Конечно, нередко - скажем, для людей престарелого возраста - оно не подвластно нам. Но в зрелые годы и '
            'особенно в молодые каждому под силу перебороть свою невнимательность, воспитать собранность и постоянно '
            'тренировать память.', reply_markup=tests_markup)
    elif points < 11:
        update.message.reply_text(
            'Вы достаточно внимательны, не забываете ничего важного. Однако, как говорится, и на старуху бывает '
            'проруха - кое-что можете запамятовать, иногда проявляете рассеянность, что оборачивается досадными '
            'недоразумениями. И все же вы способны в ответственный момент сосредоточиться и не допустить какой-либо '
            'промашки.', reply_markup=tests_markup)
    else:
        update.message.reply_text(
            'Вы удивительно внимательны и проницательны. Такой памяти и такой внимательности остается только '
            'позавидовать - это дано не каждому.', reply_markup=tests_markup)
    points = 0

    return ConversationHandler.END
