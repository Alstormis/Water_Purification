from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget
from src.app.ui.type_water_right import Ui_water_right

class Type_water_right_class(QWidget):
    # delete = pyqtSignal(int)
    def __init__(self, name: str, concentration, parent):
        super(Type_water_right_class, self).__init__()
        self.ui = Ui_water_right()
        self.ui.setupUi(self)
        self.ui.name_water.setText(name)
        self.ui.conc.setText(str(concentration))
    def change_right(self, name, concentration):
        self.ui.name_water.setText(name)
        self.ui.conc.setText(str(concentration))
    # def clean_rigth_water(self):
    #     self.delete.emit(self.id_widget)

