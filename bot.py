# -*- coding: utf-8 -*-

import telebot
import config
from utils import *
from menu import *
from session import Session

bot = telebot.TeleBot(config.token)
session = Session


@bot.message_handler(commands=['start'])
def start_handler(message):
    keyboard = generate_reply_markup(start_menu)
    bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=keyboard)
    # bot.register_next_step_handler(msg, askSource)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    chat_id = message.chat.id
    text = message.text
    if text == start_menu[0].text:  # Таблицы
        inline_keyboard = generate_inline_markup(table_menu)
        msg = bot.send_message(chat_id, 'Таблицы:', reply_markup=inline_keyboard)
    elif text == start_menu[1].text:  # Формулы и теоремы
        inline_keyboard = generate_inline_markup(formulas_and_theorems_menu)
        msg = bot.send_message(chat_id, 'Выберите фигуру:', reply_markup=inline_keyboard)
    elif text == start_menu[2].text:  # Решить задачу
        inline_keyboard = generate_inline_markup(solve_the_task_menu, )
        msg = bot.send_message(chat_id, 'Что вам нужно найти?', reply_markup=inline_keyboard)
    elif text == start_menu[3].text:  # Калькулятор
        inline_keyboard = generate_inline_markup(calculator_menu)
        msg = bot.send_message(chat_id, 'Что вы хотите вычислить?', reply_markup=inline_keyboard)
    else:
        if chat_id in session.list_session.keys():
            if session.list_session[chat_id] in callback_data_solve_the_task.keys():
                value = callback_data_solve_the_task[session.list_session[chat_id]][1](text)
                if value != -1:
                    bot.send_message(chat_id,
                                     "Результат: " + value)
                else:
                    bot.send_message(chat_id,
                                     "Введены некорректные значения, повторите попытку")
            elif session.list_session[chat_id] in callback_data_solve_the_task_inside.keys():
                value = callback_data_solve_the_task_inside[session.list_session[chat_id]][1](text)
                if value != -1:
                    bot.send_message(chat_id,
                                     "Результат: " + value)
                else:
                    bot.send_message(chat_id,
                                     "Введены некорректные значения, повторите попытку")


@bot.callback_query_handler(func=lambda click: True)
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    main_logic(bot, callback_query)


if __name__ == "__main__":
    bot.infinity_polling()

