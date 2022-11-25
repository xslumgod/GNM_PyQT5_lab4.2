#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        #self.textEdit_words.clear()


        text = self.textEdit_text.toPlainText()  # получаем наш текст
        text2 = self.textEdit_words.toPlainText()
        txt = text.split()
        txt2 = text2.split()
        stroka = ""
        count = 0
        words = {}
        for i in txt:
            for j in txt2:
                if i.lower() == j.lower():
                    count += 1
            # if count < count_past:
            #     stroka = stroka + i + " - " + str(count) + "\n"
            # else:
            #     stroka = i + " - " + str(count) + "\n" + stroka
            if count != 0:
                words[count] = i + " - "
            count = 0
        words = sorted(words.items(), reverse=True)
        print(words)
        #for i in range(len(words)):
        #stroka = ''.join(words)
        for item in words:
            stroka += item[1] + str(item[0])  + ", "
        stroka = stroka[:-2]
        self.textEdit_words_2.setPlainText(stroka)

        # text3 = self.textEdit_words_2.toPlainText()
        # txt3 = text3.split("\n")
        # #print(sorted(txt3, key = lambda x: x[-1], reverse = True))
        # #txt3 = sorted(txt3, key = lambda x: x[-1], reverse = True)
        # stroka2 = ""
        # for i in txt3:
        #     stroka2 += str(i) + "\n"
        #
        # self.textEdit_words_2.setPlainText(stroka2)
        #for s in txt:
        #    self.textEdit_words.insertPlainText(s.upper()+" ")

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()
        self.textEdit_words_2.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()