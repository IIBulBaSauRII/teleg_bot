from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler


FIRST, SECOND, THIRD, FOURTH, FIFTH, SIXTH, SEVENTH, EIGHTH, NINETH, TENTH, ELEVENTH, TWELVETH, END = range(13)


def first(update, context):
    global points
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Убеждены ли вы в позитивном значении школы жизни для развития человека и для достижения '
        'определенных позиций в обществе?',
        reply_markup=markup_key)
    return SECOND


def second(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Хорошо ли вы себя чувствуете в атмосфере борьбы, соревнования, достижения замыслов?',
        reply_markup=markup_key)
    return THIRD


def third(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    reply_keyboard = [['реализация практических задач',
                       'деятельность, направленная на защиту человеческого достоинства и прав сограждан']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Какую из функций современных политических лидеров вы считаете наиболее важной:',
        reply_markup=markup_key)
    return FOURTH


def fourth(update, context):
    global points
    if update.message.text == 'реализация практических задач':
        points += 5
    reply_keyboard = [['религиозными положениями', 'идеями прекрасного',
                       'материальными соображениями', 'всеобщим благосостоянием']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Наша деятельность должна быть регламентирована:',
        reply_markup=markup_key)
    return FIFTH


def fifth(update, context):
    global points
    if update.message.text == 'всеобщим благосостоянием':
        points += 5
    reply_keyboard = [['человека предприимчивого, работящего, наделенного практическим умом',
                       'человека думающего, мечтательного, оторванного от действительности',
                       'человека со способностями руководителя и организатора']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Себе в друзья вы бы выбрали:',
        reply_markup=markup_key)
    return SIXTH


def sixth(update, context):
    global points
    if update.message.text == 'человека думающего, мечтательного, оторванного от действительности':
        points += 5
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Достаточно ли бывает у вас энергии, чтобы преодолеть встречающиеся на пути трудности?',
        reply_markup=markup_key)
    return SEVENTH


def seventh(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Можем ли мы радоваться, что живем в такое активное время?',
        reply_markup=markup_key)
    return EIGHTH


def eighth(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Любите ли вы смотреть на огонь?',
        reply_markup=markup_key)
    return NINETH


def nineth(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Родились ли вы под одним из названных знаков зодиака: Овен, Лев, Стрелец?',
        reply_markup=markup_key)
    return TENTH


def tenth(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Легко ли вы переносите отказ, даже если знаете, что вашу просьбу выполнить невозможно?',
        reply_markup=markup_key)
    return ELEVENTH


def eleventh(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Разговорчивы ли вы?',
        reply_markup=markup_key)
    return TWELVETH


def twelveth(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    reply_keyboard = [['Да', 'Нет']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Живете ли вы по принципу, что каждая дорога ведет к цели?',
        reply_markup=markup_key)
    return END


def cancel(update, context):
    return ConversationHandler.END


def end(update, context):
    global points
    if update.message.text == 'Да':
        points += 5
    if points < 45:
        update.message.reply_text(
            'К сожалению, ваша энергия не является наиболее сильным вашим качеством. Вы быстро устаете, неохотно берете'
            ' на себя ответственность. Свое мнение держите скорее при себе. Слишком много в вас равнодушия и '
            'осторожности в отношениях с окружающими. Вы с большим трудом принимаете решения. Ваша энергия, а также '
            'способность к действиям зависят от вашего воображения и не всегда обоснованного страха. '
            'Попытайтесь открыться!')
    else:
        update.message.reply_text(
            'Вы отличаетесь веселым характером, легко и в согласии живете с людьми. У вас есть определенные черты '
            'характера руководителя. Вы энергичны и деятельны. Не очень хорошо переносите зависимость от других людей '
            '(например, начальников). Вы склонны считать, что все, что вы знаете в жизни, - это результат ваших '
            'собственных изысканий, ибо вы в состоянии эффективно работать и распространять свои взгляды на окружающих.'
            ' Вы превосходите окружающих энергичностью и быстротой принятия решений, умеете брать на себя '
            'ответственность. В своем окружении вы желаемы и любимы, прежде всего за свою динамичность и необычайную '
            'активность.')

    return ConversationHandler.END