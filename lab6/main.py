# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
import string

import cherrypy as cherrypy
from peewee import *
import datetime

db = SqliteDatabase('data.db')


def parseToHtmlTable(strings):
    stringi = ""
    for x in strings:
        stringi += "<tr>"
        for y in x:
            stringi += "<th style='color: white; border-collapse: separate; " \
                       "background: #990000; padding: 20px; text-align:center; font-size: 20px'> "
            stringi += str(y)
            stringi += "</th>"
        stringi += "</tr>"
    return stringi


class BaseModel(Model):
    class Meta:
        database = db


class APPLab(BaseModel):
    class Meta:
        db_table = 'lab6'

    idx = PrimaryKeyField(unique=True)
    # number = IntegerField()
    fio = IntegerField()
    dateTime = DateTimeField()
    text = IntegerField()

    def Update(self, sid, name, typean, age):
        appLab = APPLab.get(idx=sid)
        appLab.name = name
        appLab.typean = typean
        appLab.age = age
        appLab.save()

    def Add(self, name, typean, age):
        APPLab(
            name=name,
            typean=typean,
            age=age
        ).save()

    def getColumn(self):
        cursor = db.cursor()

        cursor.execute('PRAGMA table_info("lab6")')
        column_names = [i[1] for i in cursor.fetchall()]

        return column_names

    def getStrings(self):
        cursor = db.cursor()

        sqlite_select_query = """SELECT * from lab6"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        return records


class Page(object):
    columns = {}
    visit = ""

    def __init__(self, c, v):
        self.columns = c
        self.visit = v

    @cherrypy.expose
    def index(self):
        return f'''
        <html>
            <head>
                <meta charset="utf-8">
                <title>Лабораторная работа 6, вариант 3</title>
            </head>
                <body style="background: white">
                    <table  style="
                                margin-left: auto;
                                margin-right: auto;
                                text-align: left;
                                border-collapse: separate;
                                border-spacing: 10px;
                                background: #000000;
                                color: #999900;
                                border: 2px solid #000000;"
                    >
                        <h1 style="color: black; text-align: center; font-size: 50px;">Лабораторная работа 6, вариант 3</h1>
                            <tr>
                                {
        "".join(["<th style='color: white; text-align:center; padding: 20px; font-size: 20px;'>" + i + "</th>"
                 for i in self.columns])
        }
                            </tr>   
                                {stringi}
                    </table>
                </body>
        </html>

        '''


if __name__ == '__main__':
    db.create_tables([APPLab])
    app = APPLab()
    # app.Add("Just For Testing", datetime.datetime(2022, 5, 1, 16, 25), "Message")
    # app.Update(4, "Test", datetime.datetime(2025, 5, 5, 18, 50), "HeHeHe")

    columns = app.getColumn()
    strings = app.getStrings()

    stringi = parseToHtmlTable(strings)

    cherrypy.quickstart(Page(columns, stringi))

    db.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
