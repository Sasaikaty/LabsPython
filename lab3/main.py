# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import os.path


def parse_csv():
    data = {}
    with open("data.csv", "r", encoding='utf-8') as raw_scv:
        for line in raw_scv:
            (pkey, name, typean, age) = line.replace("\n", "").split(",")
            data.update({int(pkey): {"NAME": name, "TYPEAN": typean, "AGE": int(age)}})
    return data


def namesrt(d):
    return dict(sorted(d.items(), key=lambda f: f[1]["NAME"]))


def agesrt(d):
    return dict(sorted(d.items(), key=lambda f: f[1]["AGE"]))


def elem_prnt(d, number):
    return dict((i, j) for i, j in d.items() if j["AGE"] > number)


def output(mas):
    for i, j in mas.items():
        print(f"№{i}\nКличка: {j['NAME']}\nПорода: {j['TYPEAN']}\nВозраст: {j['AGE']}\n")
    print('\n\n\n')


def directory_count():
    folder_name = input("Название папки:")
    (loc, dirs, files) = next(os.walk(folder_name))
    print("Количество файлов в папке:")
    print(len(files))


def adding(d, name, typean, age):
    with open("data.csv", "w", encoding='utf-8') as f:
        for i, j in d.items():
            f.write(f"{i},{j['NAME']},{j['TYPEAN']},{j['AGE']}\n")
        f.write(f"{len(d) + 1},{name},{typean},{age}\n")
    data.update({len(d) + 1: {"NAME": name, "TYPEAN": typean, "AGE": age}})


data = parse_csv()
print("Выбор режима: 0 - просмотр кол-ва файлов в папке\n"
      "1 - Просмотр таблицы, 2 и более - запись в таблицу")
z = int(input())
if z == 0:
    directory_count()
elif z == 1:
    print("Введите режим отображения: 0 - сортировка по имени \n"
          "1 - сортировка по возрасту, 2 и более - тех кто старше n возраста")
    x = int(input())
    if x == 0:
        output(namesrt(data))
    elif x == 1:
        output(agesrt(data))
    else:
        print("Введите возраст:")
        y = int(input())
        output(elem_prnt(data, y))
else:
    print("Введите кличку:")
    a1 = str(input())
    print("Введите породу:")
    a2 = str(input())
    print("Введите возраст:")
    a3 = int(input())
    adding(data, a1, a2, a3)
