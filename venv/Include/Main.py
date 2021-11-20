"""
# Version : 5.15.6
# Author : QA1T rjs4902
# Date : 21.11.17
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainApp:

    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        exitAction = QtWidgets.QAction(QtGui.QIcon('../resources/icon/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = QMainWindow.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        btn = QPushButton('Build', self)
        btn.move(100, 400)
        btn.resize(btn.sizeHint())

        QToolTip.setFont(QFont('SansNoto', 10))
        btn.setToolTip('*.cer, *.der, *.crt 파일만 첨부가 가능합니다.')

        btn1= QPushButton('Exit', self)
        btn1.move(315, 400)
        btn1.resize(btn.sizeHint())
        btn1.clicked.connect(QCoreApplication.instance().quit)

        QToolTip.setFont(QFont('SansNoto', 10))
        btn1.setToolTip('실행 창을 종료합니다.')

        # self.date.toString(Qt.DefaultLocaleLongDate)
        MainstatusBar = QStatusBar()
        self.setStatusBar(MainstatusBar)

        status1 = QProgressBar()
        status1.setValue(24)
        MainstatusBar.addPermanentWidget(status1)

        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Cert Package Build')
        self.setWindowIcon(QIcon('../resources/icon/icon.png'))
        self.resize(500, 500)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MainApp()
   sys.exit(app.exec_())