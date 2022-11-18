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
        for i in txt:
            for j in txt2:
                if i == j:
                    count += 1
            stroka += i + " - " + str(count) + "\n"
            count = 0

        self.textEdit_words_2.setPlainText(stroka)

        text3 = self.textEdit_words_2.toPlainText()
        txt3 = text3.split("\n")
        txt3.pop(-1)
        #print(sorted(txt3, key = lambda x: x[-1], reverse = True))
        txt3 = sorted(txt3, key = lambda x: x[-1], reverse = True)
        stroka2 = ""
        for i in txt3:
            stroka2 += str(i) + "\n"

        self.textEdit_words_2.setPlainText(stroka2)
        #for s in txt:
        #    self.textEdit_words.insertPlainText(s.upper()+" ")

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
