from telebot import types
from telebot.types import InlineKeyboardButton

from functions import *

start_menu = [types.KeyboardButton("📊 Таблицы"), types.KeyboardButton("📕 Формулы и теоремы"),
              types.KeyboardButton("📝 Решить задачу"), types.KeyboardButton("⚖ Калькулятор")]
table_menu = [
    (InlineKeyboardButton('Таблица степеней', callback_data='table of degrees'),),
    (InlineKeyboardButton('Таблица квадратов', callback_data='table of squares'),),
    (InlineKeyboardButton('Таблица кубов', callback_data='table of cubes'),),
    (InlineKeyboardButton('Таблица формул сокращенного умножения',
                          callback_data='table of abbreviated multiplication formulas'),)
]
callback_data_table = ['table of degrees', 'table of squares', 'table of cubes',
                       'table of abbreviated multiplication formulas']
formulas_and_theorems_menu = [
    (InlineKeyboardButton('Квадрат', callback_data='square'), InlineKeyboardButton('Куб', callback_data='cube')),
    (InlineKeyboardButton('Ромб', callback_data='rhomb'), InlineKeyboardButton('Пирамида', callback_data='pyramid')),
    (InlineKeyboardButton('Треугольник', callback_data='triangle'),
     InlineKeyboardButton('Параллелограмм', callback_data='parallelogram')),
    (InlineKeyboardButton('Трапеция', callback_data='trapezoid'), InlineKeyboardButton('Конус', callback_data='cone')),
    (InlineKeyboardButton('Окружность', callback_data='circle'), InlineKeyboardButton('Сфера', callback_data='sphere')),
    (InlineKeyboardButton('Прямоугольник', callback_data='rectangle'),
     InlineKeyboardButton('Параллелепипед', callback_data='parallelepiped')),
    (InlineKeyboardButton('Основные тригонометрические тождества', callback_data='basic trigonometric identities'),)
]
callback_data_formulas_and_theorems = ['square', 'cube', 'rhomb', 'pyramid', 'triangle', 'parallelogram', 'trapezoid',
                                       'cone', 'circle', 'sphere', 'rectangle', 'parallelepiped', 'basic trigonometric '
                                                                                                  'identities']
solve_the_task_menu = [
    (InlineKeyboardButton('Площадь квадрата', callback_data='square area'),
     InlineKeyboardButton('Площадь прямоугольника', callback_data='rectangle area')),
    (InlineKeyboardButton('Площадь пирамиды', callback_data='pyramid area'),
     InlineKeyboardButton('Площадь трапеции', callback_data='trapezoid area')),
    (InlineKeyboardButton('Площадь ромба', callback_data='rhomb area'),
     InlineKeyboardButton('Площадь круга', callback_data='circle area')),
    (InlineKeyboardButton('Площадь прямоугольного треугольника', callback_data='area of a right triangle'),),
    (InlineKeyboardButton('Площадь параллелограмма', callback_data='parallelogram area'),),
    (InlineKeyboardButton('Площадь конуса', callback_data='area of the cone'),
     InlineKeyboardButton('Площадь цилиндра', callback_data='cylinder area')),
    (InlineKeyboardButton('Построение параболы', callback_data='building a parabola'),)
]
callback_data_solve_the_task = {'square area': ['Площадь квадрата. \n\nФормула: S = a^2, где\na - сторона квадрата.'
                                                '\n\nОтправьте длину стороны квадрата. Для нецелых чисел используйте '
                                                'точку.', square_area, False],
                                'rectangle area': ['Площадь прямоугольника.\n\nФормула: S = a*b, где\na '
                                                   '- длина прямоугольника\nb - ширина прямоугольника\n\n'
                                                   'Отправьте длину и ширину прямоугольника через запятую. Для нецелых '
                                                   'чисел используйте точку.', rectangle_area, False],
                                'pyramid area': '',
                                'trapezoid area': ['Площадь трапеции.\n\nФормулы:\nS = (a+b)/2*h\n'
                                                   'S = (a+b)/2*√(c^2-(((a-b)^2+c^2-d^2)/2*(a-b))^2)\n'
                                                   'a - верхнее основание\nb - нижнее основание\nc и d - боковые стороны'
                                                   '\nh - высота непосредственно подающая с верхнего основания на нижнее.'
                                                   '\n\nВыберите формулу, по которой мы решим задачу.', '', [
                                                       (InlineKeyboardButton('S = (a+b)/2*h',
                                                                             callback_data='trapezoid area_1'),
                                                        InlineKeyboardButton(
                                                            'S = (a+b)/2*√(c^2-(((a-b)^2+c^2-d^2)/2*(a-b))^2)',
                                                            callback_data='trapezoid area_2')),
                                                   ]],
                                'rhomb area': ['Площадь ромба.\nФормулы:\nS = 1/2*d1*d2\nS = ah\nd1 и d2 - диагонали '
                                               'ромба\nh - высота ромба\na - сторона ромба.\n'
                                               'Выберите формулу, по которой мы решим задачу.',
                                               '', [
                                                   (InlineKeyboardButton('S = 1/2*d1*d2',
                                                                         callback_data='rhomb area_1'),
                                                    InlineKeyboardButton(
                                                        'S = ah',
                                                        callback_data='rhomb area_2')),
                                               ]
                                               ],
                                'circle area': ['Площадь круга.\n\nФормула: S = π*r^2\nπ - 3,14\nr - радиус круга\n\n'
                                                'Отправьте радиус круга.', circle_area],
                                'area of a right triangle': '',
                                'parallelogram area': '',
                                'area of the cone': '',
                                'cylinder area': '',
                                'building a parabola': ''}
callback_data_solve_the_task_inside = {
    "trapezoid area_1": [
        'a - верхнее основание\nb - нижнее основание\nh - высота непосредственно подающая с верхнего основания на нижнее.'
        '\n\nОтправьте верхнее, нижнее основание и высоту через запятую. Для нецелых '
        'чисел используйте точку.', trapezoid_area_1],
    "trapezoid area_2": [
        'a - верхнее основание\nb - нижнее основание\nc и d - боковые стороны.\n\n'
        'Отправьте верхнее, нижнее основание и боковые стороны через запятую. Для нецелых'
        'чисел используйте точку.', trapezoid_area_2],
    "rhomb area_1": [
        'd1 и d2 - диагонали ромба.'
        '\n\nОтправьте диагонали ромба через запятую. Для нецелых '
        'чисел используйте точку.', rhomb_area_1],
    "rhomb area_2": [
        'h - высота ромба\na - сторона ромба.\n\n'
        'Отправьте высоту и сторону ромба через запятую. Для нецелых'
        'чисел используйте точку.', rhomb_area_2]
}
calculator_menu = [
    (InlineKeyboardButton('Возведение в степень', callback_data='square'),),
    (InlineKeyboardButton('Логарифм', callback_data='cube'),
     InlineKeyboardButton('Извлечение корня', callback_data='square'),),
    (InlineKeyboardButton('Найти НОК', callback_data='cube'),
     InlineKeyboardButton('Найти НОД', callback_data='square'),),
    (InlineKeyboardButton('Факториал', callback_data='cube'),
     InlineKeyboardButton('Проценты', callback_data='square'),)
]
