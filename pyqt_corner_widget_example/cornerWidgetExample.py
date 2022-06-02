from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication, QPushButton, QGraphicsDropShadowEffect, QSizePolicy
from PyQt5.QtCore import Qt, QPoint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # under the experiment
        # self.__btn = QPushButton('Corner Widget', self)
        self.__btn = QPushButton('Corner Widget')
        self.__effect = QGraphicsDropShadowEffect()
        self.__effect.setBlurRadius(5.0)
        self.__effect.setColor(QColor(0, 0, 0, 127))
        self.__effect.setOffset(0.0)
        self.__btn.setGraphicsEffect(self.__effect)
        self.__btn.setMaximumSize(self.__btn.sizeHint())
        self.__btn.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.__btn.setAttribute(Qt.WA_TranslucentBackground)
        self.__btn.setAutoFillBackground(True)
        self.__initUi()

    def __initUi(self):
        t = QTextEdit()
        self.setCentralWidget(t)

    def __setPosition(self):
        gg = self.geometry()
        wg = self.__btn.geometry()
        wg.moveBottomRight(QPoint(gg.right()-5, gg.bottom()-5))
        self.__btn.setGeometry(wg)
        self.__btn.show()
        self.__btn.raise_()

    def event(self, e):
        if e.type() == 17 or e.type() == 24 or e.type() == 174:
            self.__setPosition()
        elif e.type() == 13:
            self.__setPosition()
        elif e.type() == 14:
            self.__setPosition()
        return super().event(e)
