from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget
from src.app.ui.type_water import Ui_Water




class Type_water_class(QWidget):
    add = pyqtSignal(int)
    def __init__(self, name: str, id_widget: int, parent):
        super(Type_water_class, self).__init__()
        self.ui = Ui_Water()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.name_water.setText(name)
    def add_to_column(self):
        self.add.emit(self.id_widget)

