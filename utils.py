from telebot import types

import config
from SQLighter import SQLighter
from menu import *
from bot import session


def generate_reply_markup(menu):
    """
    Создаем кастомную клавиатуру для выбора ответа
    :param right_answer: Правильный ответ
    :param wrong_answers: Набор неправильных ответов
    :return: Объект кастомной клавиатуры
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in menu:
        markup.add(item)
    return markup


def generate_inline_markup(menu):
    markup = types.InlineKeyboardMarkup()
    for item in menu:
        if len(item) > 1:
            markup.row(*item)
        else:
            markup.add(item[0])
    return markup


def main_logic(bot, callback_query: types.CallbackQuery):
    name_data = callback_query.data
    if name_data in callback_data_table:
        db_worker = SQLighter(config.database_name)
        row = db_worker.get_picture(name_data)
        db_worker.close()
        photo = row[1]
        decription = row[3]
        bot.send_photo(callback_query.message.chat.id, photo, caption=decription)
    elif name_data in callback_data_formulas_and_theorems:
        db_worker = SQLighter(config.database_name)
        row = db_worker.get_formula(name_data)
        db_worker.close()
        url = row[2]
        decription = row[3]
        text_url = f'[Теоремы, свойства и формулы]({url})'
        bot.send_message(callback_query.message.chat.id, decription+text_url, parse_mode='MarkdownV2')
    elif name_data in callback_data_solve_the_task.keys():
        choice = callback_data_solve_the_task[name_data][2]
        if choice:
            inline_keyboard = generate_inline_markup(callback_data_solve_the_task[name_data][2])
        else:
            inline_keyboard = None
        msg = bot.send_message(callback_query.message.chat.id, callback_data_solve_the_task[name_data][0],
                               reply_markup=inline_keyboard)
        session.list_session[callback_query.message.chat.id] = name_data
    elif name_data in callback_data_solve_the_task_inside.keys():
        msg = bot.send_message(callback_query.message.chat.id, callback_data_solve_the_task_inside[name_data][0])
        session.list_session[callback_query.message.chat.id] = name_data
    elif name_data in callback_data_calculator.keys():
        choice = callback_data_calculator[name_data][2]
        if choice:
            inline_keyboard = generate_inline_markup(callback_data_calculator[name_data][2])
        else:
            inline_keyboard = None
        msg = bot.send_message(callback_query.message.chat.id, callback_data_calculator[name_data][0],
                               reply_markup=inline_keyboard)
        session.list_session[callback_query.message.chat.id] = name_data
    elif name_data in callback_data_calculator_inside.keys():
        msg = bot.send_message(callback_query.message.chat.id, callback_data_calculator_inside[name_data][0])
        session.list_session[callback_query.message.chat.id] = name_data




