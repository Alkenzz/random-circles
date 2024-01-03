from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtWidgets
import sys
import random
SCREEN_SIZE = [680, 480]


class RandomCircles_UI(object):
    def setup_UI(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(683, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 420, 241, 23))
        self.pushButton.setObjectName('pushButton')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 21))
        self.menubar.setObjectName('menubar')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)
        self.retranslate_UI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_UI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'MainWindow'))
        self.pushButton.setText(_translate('MainWindow', 'Показать случайный круг'))


class RandomCircles(QMainWindow, RandomCircles_UI):
    def __init__(self):
        super().__init__()
        self.setup_UI(self)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)
        self.coords = []

    def draw(self):
        self.figure = 'circle'
        self.size = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # 'yellow'
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            if self.figure == 'circle':
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = RandomCircles()
    ex.show()
    sys.exit(app.exec_())