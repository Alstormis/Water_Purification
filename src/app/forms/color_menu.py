import sys
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5 import QtWidgets, QtCore
from src.app.ui.color import Ui_Color_form






class Color(QtWidgets.QMainWindow):
    # add = pyqtSignal(int)
    def __init__(self, x_cor: int, y_cor: int):
        super(Color, self).__init__()
        self.ui = Ui_Color_form()
        self.ui.setupUi(self)
        self.move(x_cor, y_cor)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.blue.clicked.connect(self.close)







