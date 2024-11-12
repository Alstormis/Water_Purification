from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget
from src.app.ui.device import Ui_device
from src.app.DB import *



class Device_class(QWidget):
    change = pyqtSignal(int)
    device_ch = pyqtSignal(str)
    def __init__(self, name: str, id_widget: int, parent):
        super(Device_class, self).__init__()
        self.name_dv = name
        self.ui = Ui_device()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.text_device.setText(name)
        self.ui.check_device.stateChanged.connect(lambda: self.change_DB(name))
        self.ui.check_device.stateChanged.connect(self.change_count)
        self.ui.change_btn.clicked.connect(lambda:self.change_device_char(name))
    def change_DB(self,name):
        if self.ui.check_device.isChecked():
            chance_device_status(name, True)
        else:
            chance_device_status(name, False)
    def change_box(self, F):
        self.ui.check_device.setChecked(F)
    def change_count(self):
        self.change.emit(self.id_widget)
    def change_device_char(self, name):
        self.device_ch.emit(name)
    def get_name(self):
        return self.name_dv