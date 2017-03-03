#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sweb support team"
__copyright__ = "Copyright (C) 2016 Spaceweb"
__license__ = "Public Domain"
__version__ = "1.0"

import re, os, sys, time

class Searcher:
    def __init__(self):

        ###  Конфигурируем   ###
        self.paternfile = 'patterns.txt'
        self.paternfile_position = os.path.join(os.getcwd(), self.paternfile)
        self.names_file = 'names.txt'
        ########################

        self.regexes = []
        self.names_list =[]
        self.patterns_creator()
        self.console_runner()

    def patterns_creator(self):
        try:
            self.paternfile_discriptor = open(self.paternfile)
            self.namesfile_discriptor = open(self.names_file)
        except Exception as e:
            print(u'Не удалось открыть файл шаблонов. Убедитесь, что файл {} существует Трассировка:'.format(self.paternfile_discriptor))
            print(e)
            sys.exit(-1)
        try:
            for line in self.paternfile_discriptor:
                self.regexes.append(str(line).rstrip())
            for line in self.namesfile_discriptor:
                self.names_list.append(str(line).rstrip())
        except Exception as e:
            print(u"При создании группы шаблонов произошла ошибка. Трассировка:")
            print(e)
            sys.exit(-1)
        finally:
            self.paternfile_discriptor.close()
        try:
            # Гнилой код часть 1 - нужно думать как продолжить создании шаблонов при наличии некорректной регулярки.
            # Возможно лучше создавать в цикле
            self.combined = "(" + ")|(".join(self.regexes) + ")"
            self.pattern = re.compile(self.combined)
        except Exception as e:
            print(u'При компиляции регулярных выражений произошла ошибка. Трассировка:')
            print(e)
            sys.exit(-1)
    def console_runner(self):
        # Гнилой код часть 2 - 4 вложенных цикла...зачем ходил в шарагу - не понятно.
        # Нужно внедрять map и lambda
        for (root_directory_name, dirs_in_root_dir, files_name) in os.walk(os.getcwd()):
            for filename in files_name:
                pathname = os.path.join(root_directory_name, filename)
                # Гнилой код часть 3 - Ну тут вообще без комментов - пиздец.
                # Нужно придумать как корректно исключить файл с шаблонами из поиска
                if pathname == self.paternfile_position:
                    continue
                if filename in self.names_list:
                    print("Обратите внимание на файл " + pathname)
                try:
                    # Тут норм
                    scannig_file = open(pathname)
                    for line_num, line_content in enumerate(scannig_file):
                        for match in re.finditer(self.pattern, line_content):
                            # Наверно лучше писать в таблицу с помощью CVS
                            print(u'ВНИМАНИЕ! Найден зашквар! Файл: {} Строка: {}: Шаблон габонской гадюки: {}'
                                  .format(pathname, line_num + 1, match.group()))
                            mtime, atime, ctime = os.stat(pathname)[-1:-4:-1]
                            # Для второй версии:
                            # Возможно будет корретно при нахождении зараженного файла сгруппировать список фалов измененных в тот же день?
                            print('Статистика зараженного файла:')
                            print(time.ctime(mtime))
                            print(time.ctime(atime))
                            print(time.ctime(ctime))
                except Exception as e:
                    print(u'При сканировании файла произошла ошибка. Трассировка:')
                    print(e)
                finally:
                    scannig_file.close()

if __name__ == '__main__':
    Searcher()
