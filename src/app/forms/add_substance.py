from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget
from src.app.ui.substance import Ui_substance
from src.app.ui.substance_right import Ui_substance_right
from src.app.DB import *


class Substances(QWidget):
    add = pyqtSignal(int)
    dimension = ["мг/л", "кг/м3", "г/см3"]
    def __init__(self, name: str, id_widget: int, kol_vo: int, type_sub: int, child):
        super(Substances, self).__init__()
        self.child_class = child
        self.type_class = type_sub
        self.ui = Ui_substance()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.dimension_sub.addItems(self.dimension)
        self.ui.name_sub.setText(name)
        self.ui.clean_sub.clicked.connect(self.press_clean)
        self.ui.value_sub.editingFinished.connect(self.add_to_column)
        self.change_the_number(kol_vo)
    def change_right(self, new_str):
        self.ui.value_sub.setText(new_str)
    def change_the_number(self, count):
        if count != 0:
            self.ui.value_sub.setText(count)
    def get_class_values(self):
        return self.ui.value_sub.text(), self.ui.name_sub.text(), self.ui.dimension_sub.currentText()
    def add_to_column(self):
        self.add.emit(self.id_widget)
    def press_clean(self):
        self.ui.value_sub.clear()
        if self.child_class != None:
            self.child_class.deleteLater()
        self.child_class = None
    def change_to_DB(self,name, count, type):
        if type == 1:
            chance_insoluble(name, count, 0)
        if type == 2:
            chance_soluble(name, count, 0)

class Substances_right(Substances):
    delet = pyqtSignal(int)
    link_parent = 0
    def __init__(self, name: str, id_widget: int, kol_vo: int, parent_obj, dimension_text):
        super(Substances, self).__init__()
        self.ui = Ui_substance_right()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.dimension.setText(dimension_text)
        # self.ui.dimension_sub.addItems(self.dimension)
        self.ui.name_sub.setText(name)
        self.ui.clean_sub.clicked.connect(self.delete_widget)
        self.ui.value_sub.setText(kol_vo)
        self.link_parent = parent_obj
        # print(parent_obj)

    def delete_widget(self):
        self.link_parent.press_clean()
        self.delet.emit(self.id_widget)
