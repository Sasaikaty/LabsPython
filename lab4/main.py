# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import os.path


class Row:
    pkey = 0

    def __init__(self, pkey: int):
        self.pkey = pkey

    def get_pkey(self):
        return self.pkey

    def set_pkey(self, value):
        self.pkey = value


class RowModel(Row):
    pkey = 0
    name = ""
    typean = ""
    age = 0

    def __init__(self, pkey: int, name: str, typean: str, age: int):
        super().__init__(pkey)
        self.name = name
        self.typean = typean
        self.age = age

    def __str__(self):
        return f"Запись №{self.pkey}, {self.name}, {self.typean}, {self.age}"

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value


class Data:
    path = ""
    data = []
    pnter = 0

    def __init__(self, fpath: str):
        self.path = fpath
        self.data = self.parse(self.path)

    def __str__(self):
        d_str = '\n'.join([str(rm) for rm in self.data])
        return f"\n{d_str}"

    def __repr__(self):
        return f"Data({[repr(rm) for rm in self.data]})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.pnter >= len(self.data):
            self.pnter = 0
            raise StopIteration
        else:
            zn = self.data[self.pnter]
            self.pnter += 1
            return zn

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом.")

        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс.")

    def generator(self):
        self.pnter = 0
        while self.pnter < len(self.data):
            yield self.data[self.pnter]
            self.pnter += 1

    def namesrt(self):
        return list(sorted(self.data, key=lambda f: f.name))

    def agesrt(self):
        return list(sorted(self.data, key=lambda f: f.age))

    def elem_prnt(self, number):
        return [rm for rm in self.data if int(rm.age) > number]

    def adding(self, name, typean, age):
        if len(self.data) == 0:
            self.data.append(RowModel(1, name, typean, age))
        else:
            self.data.append(RowModel(self.data[len(self.data) - 1].pkey + 1, name, typean, age))
        self.save(self.path, self.data)

    @staticmethod
    def output(mas):
        for i in mas:
            print(f"Запись №{i.pkey}, {i.name}, {i.typean}, {i.age}")

    @staticmethod
    def parse(fpath):
        datafunc = []
        with open(fpath, "r", encoding='utf-8') as raw_csv:
            for line in raw_csv:
                (pkey, name, typean, age) = line.replace("\n", "").split(",")
                datafunc.append(RowModel(int(pkey), name, typean, age))
        return datafunc

    @staticmethod
    def save(fpath, new_data):
        with open(fpath, "w", encoding='utf-8') as f:
            for rm in new_data:
                f.write(f"{rm.pkey},{rm.name},{rm.typean},{rm.age}\n")


def directory_count():
    folder_name = input("Название папки:")
    (loc, dirs, files) = next(os.walk(folder_name))
    print("Количество файлов в папке:")
    print(len(files))


data = Data('data.csv')

print("Выбор режима: 0 - просмотр кол-ва файлов в папке\n"
      "1 - Просмотр таблицы, 2 и более - запись в таблицу")
z = int(input())
if z == 0:
    directory_count()
elif z == 1:
    print("Введите режим отображения: 0 - Без сортировки \n"
          "1 - Итератор, 2 - Генератор, 3 - Сортировка по кличкам\n"
          "4 - Сортировка по возрасту, 5 - Вывод тех кто старше n возраста\n"
          "6 и более - Выбор по индексу")
    x = int(input())
    if x == 0:
        print(str(data))
    elif x == 1:
        for i in iter(data):
            print(i)
    elif x == 2:
        for i in data.generator():
            print(i)
    elif x == 3:
        data.output(data.namesrt())
    elif x == 4:
        data.output(data.agesrt())
    elif x == 5:
        a = int(input("Введите возраст: "))
        data.output(data.elem_prnt(a))
    else:
        pkey = int(input("Индекс: "))
        print(f"\n{data[pkey]}")
else:
    print("Введите кличку:")
    a1 = str(input())
    print("Введите породу:")
    a2 = str(input())
    print("Введите возраст:")
    a3 = int(input())
    data.adding(a1, a2, a3)