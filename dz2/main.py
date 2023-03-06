# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import calendar
import time

year = 1970
per = 2
monthc = 1
monthdays = 31
current_GMT = time.gmtime()

time_stamp = calendar.timegm(current_GMT)

secs = time_stamp % 60
m_time_stamp = time_stamp // 60
mints = m_time_stamp % 60
h_time_stamp = m_time_stamp // 60
hours = h_time_stamp % 24
d_time_stamp = h_time_stamp // 24

while d_time_stamp > 365 + (per // 4):
    if per != 4:
        d_time_stamp -= 365
        per += 1
    else:
        d_time_stamp -= 366
        per = 1
    year += 1


while d_time_stamp >= monthdays:
    if monthc % 2 == 1 | monthc == 8:
        monthdays = 31
        d_time_stamp -= 31
    elif monthc == 2:
        if per != 4:
            monthdays = 28
            d_time_stamp -= 28
        else:
            monthdays = 29
            d_time_stamp -= 29
    else:
        monthdays = 30
        d_time_stamp -= 30
    monthc += 1


print("Current time:", year, monthc, d_time_stamp, hours, mints, secs)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
