# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
import time
mas = [random.randint(10, 1000000) for i in range (10000000)]

start = time.time()
min = 1000000


for i in mas:
    if min > i:
        min = i



end = time.time()
print(end - start, min)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
