from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget
from src.app.ui.small_division_expenditure import Ui_expenditure



class Expenditure_class(QWidget):
    add = pyqtSignal(int)
    def __init__(self, name: str, value, dimension, id_widget: int, parent):
        super(Expenditure_class, self).__init__()
        self.ui = Ui_expenditure()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.name_expenditure.setText(name)
        self.ui.value_expenditure.setText(value)
        self.ui.dimension_expenditure.setText(dimension)
    def change_right(self, new_str):
        self.ui.value_expenditure.setText(new_str)
    def add_to_column(self):
        self.add.emit(self.id_widget)