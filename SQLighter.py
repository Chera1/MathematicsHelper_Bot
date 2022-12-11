# -*- coding: utf-8 -*-
import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM music').fetchall()

    def get_picture(self, name):
        """ Получаем одну строку с по имени картинки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM data_pictures WHERE picture_name = ?', (name,)).fetchall()[0]

    def get_formula(self, name):
        """ Получаем одну строку с по имени картинки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM formulas_and_theorems WHERE name = ?', (name,)).fetchall()[0]

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM music').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
