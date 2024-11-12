from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget
from src.app.ui.characteristic import Ui_Characteristic



class Characteristic_worm(QWidget):
    delet = pyqtSignal(int)
    def __init__(self, name: str, kol_vo: int, dimension_text, parent_obj):
        super(Characteristic_worm, self).__init__()
        self.ui = Ui_Characteristic()
        self.ui.setupUi(self)
        self.ui.dimension_quality.setText(dimension_text)
        self.ui.name_quality.setText(name)
        self.ui.clean_quality.clicked.connect(self.delete_widget)
        self.ui.value_quality.setText(kol_vo)
        self.link_parent = parent_obj

    def delete_widget(self):
        self.delet.emit(1)
        # self.change_the_number(kol_vo)
    def change_right(self, new_str):
        self.ui.value_quality.setText(new_str)
    #
    # def change_the_number(self, count):
    #     if count != 0:
    #         self.ui.value_sub.setText(count)
    # def get_class_values(self):
    #     return self.ui.value_sub.text(), self.ui.name_sub.text(), self.ui.dimension_sub.currentText()

    # def press_clean(self):
    #     self.ui.value_sub.clear()
    #     if self.child_class != None:
    #         self.child_class.deleteLater()
    #     self.child_class = None

