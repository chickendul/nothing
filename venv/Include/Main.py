"""
# Version : 5.15.6
# Author : QA1T rjs4902
# Date : 21.11.17
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class MainApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Build', self)
        btn.move(100, 400)
        btn.resize(btn.sizeHint())

        QToolTip.setFont(QFont('SansNoto', 10))
        btn.setToolTip('*.cer, *.der, *.crt 파일만 첨부가 가능합니다.')

        btn1= QPushButton('Exit', self)
        btn1.move(325, 400)
        btn1.resize(btn.sizeHint())
        btn1.clicked.connect(QCoreApplication.instance().quit)

        QToolTip.setFont(QFont('SansNoto', 10))
        btn1.setToolTip('실행 창을 종료합니다.')

        self.setWindowTitle('Cert Package Build')
        self.setWindowIcon(QIcon('../resources/icon/icon.png'))
        self.setGeometry(300, 300, 500, 500)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MainApp()
   sys.exit(app.exec_())