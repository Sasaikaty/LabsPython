# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy


"""Функция поиска индекса столбца с наибольшей суммой его значений"""


def findindexmaxcolumn(a):
    """Поиск максимальной суммы значений столбца"""
    sums = numpy.sum(a, 0)
    c = max(sums)
    """Поиск индекса столбца с максимальной суммой"""
    d, = numpy.where(numpy.isclose(sums, c))
    """Выводы в консоль для контроля"""
    print(sums)
    print(d)
    return d

"""Функция записи значений в файл"""



def filewrite(a):
    """Вывод массива в консоль для контроля"""
    print(a)
    """Запись исходных данных в файл"""
    numpy.savetxt('output.txt', a, fmt='%f')
    """Добавление записи о результате в файл"""
    f = open('output.txt', 'a')
    """Запись минимального значения преобразованного в строку минимального значения столбца"""
    f.write(str(numpy.min(a[:, findindexmaxcolumn(a)])))
    f.close()


"""Ввод кол-ва строк и столбцов массива"""
x = int(input())
y = int(input())
"""Создание рандомно заполненного массива с помощью библиотеки numpy"""
a = numpy.random.uniform(0, 9, (x, y))
"""Вызов функции записи в файл"""
filewrite(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
