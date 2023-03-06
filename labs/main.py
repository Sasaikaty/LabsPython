# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
"""Замена функции len"""
def mylen(temp):
    count = 0
    for i in temp:
        count +=1
    return count

"""Функция ручного ввода"""

def mode0(a, n):
    for i in range(0, n):
        a.append(int(input('')))

"""Функция рандомного заполнения"""


def mode1(a, n):
    a = [random.randint(0, 9) for i in range(n)]
    for i in range(0, len(a)):
        print(a[i])

def mainstand():
    """Ввод"""
    a = []
    print('Введите режим(0 - заполнение вручную, 1 и более - автозаполнение)')
    try:
        mode = int(input())
    except Exception:
        print('Ошибка')
        exit();

    print('Введите кол-во элементов массива')

    try:
        n = int(input())
    except Exception:
        print('Ошибка')
        exit();
    count = 0
    print('Элементы массива (через Enter)')

    if mode == 0:
        try:
            mode0(a, n)
        except Exception:
            print('Ошибка')
            exit()

    else:
        mode1(a, n)
    """Основной алгоритм"""
    i = 0
    while i < len(a):
        """Проверка на четность"""
        if a[i] % 2 != 0:
            count += 1
            """Проверка на конечный элемент"""
            if i == len(a) - 1 and count < 3:
                """Удаление лишних элементов в конце массива"""
                for j in range(0, count):
                    a.pop(i - (count - 1))
        else:
            """Удаление лишних элементов при прерывании цепочки меньше 3"""
            if count < 3 and count != 0:
                for j in range(0, count):
                    a.pop(i - 1)
                    i -= 1
            count = 0
        i += 1

    print('Вывод')
    for i in range(0, len(a)):
        print(a[i])

def mainmine():
    """Ввод"""
    a = []
    print('Введите режим(0 - заполнение вручную, 1 и более - автозаполнение)')
    try:
        mode = int(input())
    except Exception:
        print('Ошибка')
        exit();

    print('Введите кол-во элементов массива')

    try:
        n = int(input())
    except Exception:
        print('Ошибка')
        exit();
    count = 0
    print('Элементы массива (через Enter)')

    if mode == 0:
        try:
            mode0(a, n)
        except Exception:
            print('Ошибка')
            exit()

    else:
        mode1(a, n)
    """Основной алгоритм"""
    i = 0
    while i < mylen(a):
        """Проверка на четность"""
        if a[i] % 2 != 0:
            count += 1
            """Проверка на конечный элемент"""
            if i == mylen(a) - 1 and count < 3:
                """Удаление лишних элементов в конце массива"""
                for j in range(0, count):
                    a.pop(i - (count - 1))
        else:
            """Удаление лишних элементов при прерывании цепочки меньше 3"""
            if count < 3 and count != 0:
                for j in range(0, count):
                    a.pop(i - 1)
                    i -= 1
            count = 0
        i += 1

    print('Вывод')
    for i in range(0, mylen(a)):
        print(a[i])

"""Выбор метода"""
print('0 - стандартные функции, 1 и более - свои')
z = int(input())
if z == 0:
    """Используя стандартные функции"""
    mainstand()
else:
    """Используя свои функции"""
    mainmine()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
