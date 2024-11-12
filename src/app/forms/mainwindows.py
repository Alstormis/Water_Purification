import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QFileDialog

from src.app.ui.mainWindows import Ui_MainWindow
from src.app.forms import *
from src.app.DB import *
import sys


class Mywindow(QtWidgets.QMainWindow):
    right_obj = {}
    list_right_char = {}
    name_device = str
    list_of_soluble, list_of_insoluble, list_of_water, list_of_device = value()
    insoluble_in_prog= list()
    soluble_in_prog = list()
    first_open = True
    end_type_water = 0
    type_right = None
    flag_device = True
    device_list_btn = []
    file_path = ''
    water_expenditure = 0
    concentration = 0
    file = ''


    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)




        #Для работы с типом воды
        self.rb_water = QButtonGroup(self)
        self.rb_water.buttonClicked.connect(self.get_end_water)
        self.ui.own_water_conc.textChanged.connect(lambda: self.ui.own_water_rb.toggle())
        self.ui.own_water_conc.editingFinished.connect(self.get_end_water)
        self.ui.clean_own_water.clicked.connect(lambda: self.ui.own_water_conc.setText("0"))


        #### Вещество
        self.ui.substance_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.substance))
        self.ui.open_add_substance.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_substance))
        self.ui.back_substance.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.substance))
        self.ui.add_substance_btn.clicked.connect(self.add_substance_in_DB)
        self.ui.from_prop_to_sub.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.substance))
        self.ui.del_sub.clicked.connect(self.del_substance_in_DB)
        self.ui.open_del_substance.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.delete_substance))
        self.ui.back_substance_from_del.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.substance))
        #### Свойства
        self.ui.quality_btn_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.characteristic))
        self.ui.from_sub_to_prop.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.characteristic))
        self.ui.from_water_to_prop.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.characteristic))
        #### Тип воды
        self.ui.type_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.type_of_water))
        self.ui.from_prop_to_water.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.type_of_water))
        self.ui.from_device_to_water.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.type_of_water))
        #### Аппараты
        self.ui.from_water_to_device.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.device))
        self.ui.device_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.device))
        self.ui.from_exp_to_device.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.device))
        #### Расход воды
        self.ui.from_device_to_exp.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.expenditure))
        self.ui.expenditure_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.expenditure))
        self.ui.from_exp_to_conclusion.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.expenditure))
        #### Вывод
        self.ui.output_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.output))
        self.ui.from_conclusion_to_exp.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.output))




        #### Нужные единичные вещи
        self.ui.calculation.clicked.connect(self.get_scheme)
        self.counter_id: int = 0
        self.add_sub_insoluble()
        self.add_sub_soluble()
        self.add_device()
        self.add_type_water()
        self.radio_btn()



        #### Изменения в свойствах
        self.ui.value_temperature.editingFinished.connect(lambda: self.add_char_right(self.ui.value_temperature.parentWidget(),
                                                                                  self.ui.temperature.text(),
                                                                                  self.ui.value_temperature.text(),
                                                                                  self.ui.dimension_temperature.text()))
        self.ui.value_temperature.editingFinished.connect(lambda: chance_temperature(self.ui.value_temperature.text()))

        self.ui.value_KRK.editingFinished.connect(lambda: self.add_char_right(self.ui.value_KRK.parentWidget(),
                                                                                  self.ui.KRK.text(),
                                                                                  self.ui.value_KRK.text(),
                                                                                  self.ui.dimension_KRK.text()))
        self.ui.value_KRK.editingFinished.connect(lambda: chance_KRK(self.ui.value_KRK.text()))

        self.ui.value_BPK.editingFinished.connect(lambda: self.add_char_right(self.ui.value_BPK.parentWidget(),
                                                                                  self.ui.BPK.text(),
                                                                                  self.ui.value_BPK.text(),
                                                                                  self.ui.dimension_BPK.text()))
        self.ui.value_BPK.editingFinished.connect(lambda: chance_BPK(self.ui.value_BPK.text()))

        self.ui.value_HPK.editingFinished.connect(lambda: self.add_char_right(self.ui.value_HPK.parentWidget(),
                                                                                  self.ui.HPK.text(),
                                                                                  self.ui.value_HPK.text(),
                                                                                  self.ui.dimension_HPK.text()))
        self.ui.value_HPK.editingFinished.connect(lambda: chance_HPK(self.ui.value_HPK.text()))

        self.ui.value_alkalinity.editingFinished.connect(lambda: self.add_char_right(self.ui.value_alkalinity.parentWidget(),
                                                                                  self.ui.alkalinity.text(),
                                                                                  self.ui.value_alkalinity.text(),
                                                                                  self.ui.dimension_alkalinity.text()))
        self.ui.value_alkalinity.editingFinished.connect(lambda: chance_alkalinity(self.ui.value_alkalinity.text()))

        self.ui.value_smell.editingFinished.connect(lambda: self.add_char_right(self.ui.value_smell.parentWidget(),
                                                                                  self.ui.smell.text(),
                                                                                  self.ui.value_smell.text(),
                                                                                  self.ui.dimension_smell.text()))
        self.ui.value_smell.editingFinished.connect(lambda: chance_smell(self.ui.value_smell.text()))


        self.ui.value_chroma.editingFinished.connect(lambda: self.add_char_right(self.ui.value_chroma.parentWidget(),
                                                                                  self.ui.chroma.text(),
                                                                                  self.ui.value_chroma.text(),
                                                                                  self.ui.dimension_chroma.text()))
        self.ui.value_chroma.editingFinished.connect(lambda: chance_chroma(self.ui.value_chroma.text()))

        self.ui.value_radioactivity.editingFinished.connect(lambda: self.add_char_right(self.ui.value_radioactivity.parentWidget(),
                                                                                  self.ui.radioactivity.text(),
                                                                                  self.ui.value_radioactivity.text(),
                                                                                  self.ui.dimension_radioactivity.text()))
        self.ui.value_radioactivity.editingFinished.connect(lambda: chance_radioactivity(self.ui.value_radioactivity.text()))

        self.ui.value_rigidity.editingFinished.connect(lambda: self.add_char_right(self.ui.value_rigidity.parentWidget(),
                                                                                  self.ui.rigidity.text(),
                                                                                  self.ui.value_rigidity.text(),
                                                                                  self.ui.dimension_rigidity.text()))
        self.ui.value_rigidity.editingFinished.connect(lambda: chance_rigidity(self.ui.value_rigidity.text()))

        #### Кнопки очистки в окне свойств
        self.ui.clean_temperature.clicked.connect(lambda: self.ui.value_temperature.clear())
        self.ui.clean_temperature.clicked.connect(lambda: self.clean_right_widget(self.ui.value_temperature.parentWidget()))

        self.ui.clean_KRK.clicked.connect(lambda: self.ui.value_KRK.clear())
        self.ui.clean_KRK.clicked.connect(lambda: self.clean_right_widget(self.ui.value_KRK.parentWidget()))

        self.ui.clean_BPK.clicked.connect(lambda: self.ui.value_BPK.clear())
        self.ui.clean_BPK.clicked.connect(lambda: self.clean_right_widget(self.ui.value_BPK.parentWidget()))

        self.ui.clean_HPK.clicked.connect(lambda: self.ui.value_HPK.clear())
        self.ui.clean_HPK.clicked.connect(lambda: self.clean_right_widget(self.ui.value_HPK.parentWidget()))

        self.ui.clean_alkalinity.clicked.connect(lambda: self.ui.value_alkalinity.clear())
        self.ui.clean_alkalinity.clicked.connect(lambda: self.clean_right_widget(self.ui.value_alkalinity.parentWidget()))

        self.ui.clean_smell.clicked.connect(lambda: self.ui.value_smell.clear())
        self.ui.clean_smell.clicked.connect(lambda: self.clean_right_widget(self.ui.value_smell.parentWidget()))

        self.ui.clean_chroma.clicked.connect(lambda: self.ui.value_chroma.clear())
        self.ui.clean_chroma.clicked.connect(lambda: self.clean_right_widget(self.ui.value_chroma.parentWidget()))

        self.ui.clean_radioactivity.clicked.connect(lambda: self.ui.value_radioactivity.clear())
        self.ui.clean_radioactivity.clicked.connect(lambda: self.clean_right_widget(self.ui.value_radioactivity.parentWidget()))

        self.ui.clean_rigidity.clicked.connect(lambda: self.ui.value_rigidity.clear())
        self.ui.clean_rigidity.clicked.connect(lambda: self.clean_right_widget(self.ui.value_rigidity.parentWidget()))



        #Сторонние кнопки
        #self.ui.clean_search.clicked.connect(lambda: self.ui.text_search.clear())
        self.ui.choose_all_device.clicked.connect(self.butt_all_device)

        #Количество аппаратов справа
        self.ui.kol_vo_device.setText(str(len(self.list_of_device)))
        # self.ui.choose_all_device.clicked.connect()

        # print(self.ui.value_temperature.parentWidget())

        #Расход воды
        self.ui.sr_syt.editingFinished.connect(lambda: self.convert_water("sr_syt"))
        self.ui.max_syt.editingFinished.connect(lambda: self.convert_water("max_syt"))
        self.ui.min_syt.editingFinished.connect(lambda: self.convert_water("min_syt"))
        self.ui.sr_cas.editingFinished.connect(lambda: self.convert_water("sr_cas"))
        self.ui.max_cas.editingFinished.connect(lambda: self.convert_water("max_cas"))
        self.ui.min_cas.editingFinished.connect(lambda: self.convert_water("min_cas"))
        self.ui.sr_cek.editingFinished.connect(lambda: self.convert_water("sr_cek"))
        self.ui.max_cek.editingFinished.connect(lambda: self.convert_water("max_cek"))
        self.ui.min_cek.editingFinished.connect(lambda: self.convert_water("min_cek"))
        #Удаление расхода воды
        self.ui.clean_sr_syt.clicked.connect(self.clean_water_consumption)
        self.ui.clean_max_syt.clicked.connect(self.clean_water_consumption)
        self.ui.clean_min_syt.clicked.connect(self.clean_water_consumption)
        self.ui.clean_sr_cas.clicked.connect(self.clean_water_consumption)
        self.ui.clean_max_cas.clicked.connect(self.clean_water_consumption)
        self.ui.clean_min_cas.clicked.connect(self.clean_water_consumption)
        self.ui.clean_sr_cek.clicked.connect(self.clean_water_consumption)
        self.ui.clean_max_cek.clicked.connect(self.clean_water_consumption)
        self.ui.clean_min_cek.clicked.connect(self.clean_water_consumption)

    ### Добавление в право концентрации воды
    def get_end_water(self):
        conc = self.rb_water.button(self.rb_water.checkedId()).parentWidget().children()[2].text()
        if conc == 'Своя концентрация':
            self.end_type_water = self.ui.own_water_conc.text()
            self.concentration = self.ui.own_water_conc.text()
        else:
            self.end_type_water = end_concent_water(self.rb_water.button(self.rb_water.checkedId()).parentWidget()
                                                    .children()[2].text())
            self.concentration = self.end_type_water
        if self.type_right == None:
            self.type_right = Type_water_right_class(conc, self.end_type_water, self.rb_water.button(self.rb_water.checkedId()).parentWidget())
            self.ui.lay_TW_right.addWidget(self.type_right)
        else:
            self.type_right.change_right(conc, self.end_type_water)
        # type_right.delete.connect(self.clean_rigth_water)
        # print(self.end_type_water)
        # pl = self.rb_water.buttonClicked()
        # print(pl.parentWidget().parent())
    ########################################
    def clean_right_widget(self, wid_parent):
        rigth = self.list_right_char[wid_parent]
        rigth.deleteLater()
        del self.list_right_char[wid_parent]
    #######################################
    #добавление нерастворимых веществ
    def add_sub_insoluble(self):
        for insoluble in range(len(self.list_of_insoluble)):
            if insoluble not in self.insoluble_in_prog:
                self.insoluble_in_prog.append(insoluble)
                self.counter_id += 1
                substances = Substances(self.list_of_insoluble[insoluble],self.counter_id, 0, 1, None)
                self.ui.lay_insoluble.addWidget(substances)
                substances.add.connect(self.add_to_column_right)

    # добавление растворимых веществ
    def add_sub_soluble(self):
        for soluble in range(len(self.list_of_soluble)):
            if soluble not in self.soluble_in_prog:
                self.soluble_in_prog.append(soluble)
                self.counter_id += 1
                substances = Substances(self.list_of_soluble[soluble], self.counter_id, 0, 2, None)
                self.ui.lay_soluble.addWidget(substances)
                substances.add.connect(self.add_to_column_right)

    # добавить в правое окно
    @QtCore.pyqtSlot(int)
    def add_to_column_right(self):
        widget = self.sender()
        count, name, dimension = widget.get_class_values()
        type_class = widget.type_class
        self.add_sub_right(widget, name, count, type_class, dimension)
    ##Добавление в бд. Нужно сделать, чтобы программа понимала из какой таблицы удалять по типу вещества
        # chance_insoluble(name, count, 0)
        #print(widget)
        #print(widget.text())
        #print(widget.currentItem().text())
        #item = self.ui.lay_soluble.takeAt(0)
        #print(item)
        #self.ui.lay_insoluble.removeWidget(widget)
        #print(widget)
        # self.ui.lay_insoluble.removeWidget(widget)
        #widget.deleteLater()
    def add_sub_right(self, widget, name: str, kol_vo: int, type_sub, dimension):
        if widget.child_class != None:
            widget.child_class.change_right(kol_vo)
            widget.child_class.change_to_DB(name, kol_vo, type_sub)
        else:
            self.counter_id += 1
            substances = Substances_right(name, self.counter_id, kol_vo, widget, dimension)
            widget.child_class = substances
            widget.child_class.change_to_DB(name, kol_vo, type_sub)
            # self.right_obj[widget] = substances
            if type_sub == 1:
                self.ui.lay_insoluble_right.addWidget(substances)
            else:
                self.ui.lay_soluble_right.addWidget(substances)
            substances.delet.connect(self.del_sub_right)

    #удалить в правом окне
    @QtCore.pyqtSlot(int)
    def del_sub_right(self):
        # print(f'Удаляем виджет с id: {wid}')
        widget = self.sender()
        for k, v in self.right_obj.items():
            if v == widget:
                del self.right_obj[k]
                break
        widget.deleteLater()

    #################################
    ### Отображение свойств в правом окне ###
    #################################
    def add_char_right(self, widget, name, kol_vo, dimension):
        if widget in self.list_right_char:
            change = self.list_right_char[widget]
            change.change_right(kol_vo)
        else:
            characteristic = Characteristic_worm(name, kol_vo, dimension, widget)
            self.list_right_char.update({widget: characteristic})
            self.ui.lay_characteristic_right.addWidget(characteristic)
            characteristic.delet.connect(self.del_char_right)
        # if widget.child_class != None:
        #     widget.child_class.change_right(kol_vo)
        # else:
        #     self.counter_id += 1
        #characteristic = Characteristic(name, kol_vo, dimension, widget)
        # widget.child_class = characteristic

    ### Потом необходимо добавить обновление данных из бд для всех свойств
    @QtCore.pyqtSlot(int)
    def del_char_right(self):
        widget = self.sender()
        widget.deleteLater()

    #################################
    ### Показ типов воды ###
    #################################
    def add_type_water(self):
        self.rb_water.addButton(self.ui.own_water_rb)
        for water_sp in range(len(self.list_of_water)):
            self.counter_id += 1
            water = Type_water_class(self.list_of_water[water_sp], self.counter_id, None)
            self.rb_water.addButton(water.ui.water_rb_btn)
            self.ui.water_lay.addWidget(water)
            # self.ui.water_lay.addSpacing(-2)

    #################################
    ### Показ аппаратов ###
    #################################
    def add_device(self):
        for dev in range(len(self.list_of_device)):
            self.counter_id += 1
            water = Device_class(self.list_of_device[dev], self.counter_id, None)
            self.ui.pokaz_dev.addWidget(water)
            self.device_list_btn.append(water)
            water.change.connect(self.count_device)
            water.device_ch.connect(self.open_device)

            #water.add.connect(self.reset_to_zero_substances)
            # print(self.ui.pokaz_dev.count())

    @QtCore.pyqtSlot(int)
    def count_device(self):
        value = int(self.ui.kol_vo_device.text())
        if self.sender().children()[1].children()[1].isChecked() == True:
            self.ui.kol_vo_device.setText(str(value + 1))
        else:
            self.ui.kol_vo_device.setText(str(value - 1))
    ########################################
    #открыть свойства устройств
    ########################################
    @QtCore.pyqtSlot(str)
    def open_device(self):
        widget = self.sender()
        name = widget.get_name()
        self.pokas_device(name)

    def pokas_device(self, name):
        # device_open_char(name)
        (expenditure, start, effectiveness, temperature, oxygen, BPK, XPK, pH, radioactivity, color, coloration, smell,
         rigidity, level, cost) = device_open_char(name)
        self.ui.stackedWidget.setCurrentWidget(self.ui.show_the_device)
        self.ui.vater_ras.setText(str(expenditure))
        self.ui.value_start.setText(str(start))
        self.ui.efff.setText(str(effectiveness))
        self.ui.value_temperature_2.setText(str(temperature))
        self.ui.value_KRK_2.setText(str(oxygen))
        self.ui.value_BPK_2.setText(str(BPK))
        self.ui.value_HPK_2.setText(str(XPK))
        self.ui.value_alkalinity_2.setText(str(pH))
        self.ui.value_radioactivity_2.setText(str(radioactivity))
        self.ui.value_color_2.setText(str(color))
        self.ui.value_chroma_2.setText(str(coloration))
        self.ui.value_smell_2.setText(str(smell))
        self.ui.value_rigidity_2.setText(str(rigidity))
        self.ui.value_lvl.setText(str(level))
        self.ui.value_coint.setText(str(cost))
        self.ui.label_32.setText(name)
        self.ui.to_device.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.device))

    def device_ismen(self):
        device_change_char(self.ui.label_32.text(), self.ui.vater_ras.text(), self.ui.value_start.text(),
                           self.ui.efff.text(), self.ui.value_temperature_2.text(), self.ui.value_KRK_2.text(),
                           self.ui.value_BPK_2.text(), self.ui.value_HPK_2.text(), self.ui.value_alkalinity_2.text(),
                           self.ui.value_radioactivity_2.text(), self.ui.value_color_2.text(),
                           self.ui.value_chroma_2.text(), self.ui.value_smell_2.text(), self.ui.value_rigidity_2.text(),
                           self.ui.value_lvl.text(), self.ui.value_coint.text())

    def butt_all_device(self):
        if self.flag_device == True:
            for i in range(len(self.device_list_btn)):
                self.device_list_btn[i].change_box(False)
                self.flag_device = False
                self.ui.kol_vo_device.setText('0')
        else:
            for i in range(len(self.device_list_btn)):
                self.device_list_btn[i].change_box(True)
                self.flag_device = True
                self.ui.kol_vo_device.setText(str(len(self.list_of_device)))

    #################################
    ### Для работы с окном цветов ###
    #################################
    def open_color_form(self):
        #color_form = Color()
        #color_form = QtWidgets.QApplication([])
        self.color_form = Color(self.ui.open_color.mapToGlobal(QPoint(0, 0)).x(),
                                self.ui.open_color.mapToGlobal(QPoint(0,0)).y() + self.ui.open_color.height())
        self.color_form.show()
        app.focusChanged.connect(self.onFocusChanged)
    def onFocusChanged(self):
        if self.isActiveWindow():
            self.color_form.close()

    #################################
    ### Расход воды ###
    #################################
    def convert_water(self, type):
        match type:
            case "sr_syt":
                self.water_expenditure = int(self.ui.sr_syt.text())
                chas, cek = syt_chas_cek(self.ui.sr_syt.text())
                self.ui.sr_cas.setText(str(round(chas, 3)))
                self.ui.sr_cek.setText(str(round(cek, 7)))
                self.block_water(False, True, True, True, True, True, True, True, True)
                self.add_consumption_water(self.ui.sr_syt.parentWidget(),
                                                self.ui.sr_syt_text.text(),
                                                self.ui.sr_syt.text(),
                                                self.ui.sr_syt_dim.text(),
                                                'Суточный'
                                           )
            case "max_syt":
                self.water_expenditure = int(self.ui.max_syt.text())
                chas, cek = syt_chas_cek(self.ui.max_syt.text())
                self.ui.max_cas.setText(str(round(chas, 3)))
                self.ui.max_cek.setText(str(round(cek, 7)))
                self.block_water(True, False, True, True, True, True, True, True, True)
                self.add_consumption_water(self.ui.max_syt.parentWidget(),
                                                self.ui.max_syt_text.text(),
                                                self.ui.max_syt.text(),
                                                self.ui.max_syt_dim.text(),
                                                'Суточный'
                                           )
            case "min_syt":
                self.water_expenditure = int(self.ui.min_syt.text())
                chas, cek = syt_chas_cek(self.ui.min_syt.text())
                self.ui.min_cas.setText(str(round(chas, 3)))
                self.ui.min_cek.setText(str(round(cek, 7)))
                self.block_water(True, True, False, True, True, True, True, True, True)
                self.add_consumption_water(self.ui.min_syt.parentWidget(),
                                                self.ui.min_syt_text.text(),
                                                self.ui.min_syt.text(),
                                                self.ui.min_syt_dim.text(),
                                                'Суточный'
                                           )
            case "sr_cas":
                syt, cek = chas_syt_cek(self.ui.sr_cas.text())
                self.water_expenditure = round(syt, 3)
                self.ui.sr_syt.setText(str(round(syt, 3)))
                self.ui.sr_cek.setText(str(round(cek, 7)))
                self.block_water(True, True, True, False, True, True, True, True, True)
                self.add_consumption_water(self.ui.sr_cas.parentWidget(),
                                                self.ui.sr_cas_text.text(),
                                                self.ui.sr_cas.text(),
                                                self.ui.sr_cas_dim.text(),
                                                'Часовой'
                                           )
            case "max_cas":
                syt, cek = chas_syt_cek(self.ui.max_cas.text())
                self.ui.max_syt.setText(str(round(syt, 3)))
                self.ui.max_cek.setText(str(round(cek, 7)))
                self.water_expenditure = round(syt, 3)
                self.block_water(True, True, True, True, False, True, True, True, True)
                self.add_consumption_water(self.ui.max_cas.parentWidget(),
                                                self.ui.max_cas_text.text(),
                                                self.ui.max_cas.text(),
                                                self.ui.max_cas_dim.text(),
                                                'Часовой'
                                           )
            case "min_cas":
                syt, cek = chas_syt_cek(self.ui.min_cas.text())
                self.ui.min_syt.setText(str(round(syt, 3)))
                self.ui.min_cek.setText(str(round(cek, 7)))
                self.water_expenditure = round(syt, 3)
                self.block_water(True, True, True, True, True, False, True, True, True)
                self.add_consumption_water(self.ui.min_cas.parentWidget(),
                                                self.ui.min_cas_text.text(),
                                                self.ui.min_cas.text(),
                                                self.ui.min_cas_dim.text(),
                                                'Часовой'
                                           )
            case "sr_cek":
                syt, chas = cek_syt_chas(self.ui.sr_cek.text())
                self.ui.sr_syt.setText(str(round(syt, 3)))
                self.ui.sr_cas.setText(str(round(chas, 3)))
                self.water_expenditure = round(syt, 3)
                self.block_water(True, True, True, True, True, True, False, True, True)
                self.add_consumption_water(self.ui.sr_cek.parentWidget(),
                                                self.ui.sr_cek_text.text(),
                                                self.ui.sr_cek.text(),
                                                self.ui.sr_cek_dim.text(),
                                                'Секундный'
                                           )
            case "max_cek":
                syt, chas = cek_syt_chas(self.ui.max_cek.text())
                self.ui.max_syt.setText(str(round(syt, 3)))
                self.ui.max_cas.setText(str(round(chas, 3)))
                self.water_expenditure = round(syt, 3)
                self.block_water(True, True, True, True, True, True, True, False, True)
                self.add_consumption_water(self.ui.max_cek.parentWidget(),
                                                self.ui.max_cek_text.text(),
                                                self.ui.max_cek.text(),
                                                self.ui.max_cek_dim.text(),
                                                'Секундный'
                                           )
            case "min_cek":
                syt, chas = cek_syt_chas(self.ui.min_cek.text())
                self.ui.min_syt.setText(str(round(syt, 3)))
                self.ui.min_cas.setText(str(round(chas, 3)))
                self.water_expenditure = round(syt, 3)
                self.block_water(True, True, True, True, True, True, True, True, False)
                self.add_consumption_water(self.ui.min_cek.parentWidget(),
                                                self.ui.min_cek_text.text(),
                                                self.ui.min_cek.text(),
                                                self.ui.min_cek_dim.text(),
                                                'Секундный'
                                           )
            case _:
                print(3)
    def clean_water_consumption(self):
        self.ui.sr_syt.clear()
        self.ui.max_syt.clear()
        self.ui.min_syt.clear()
        self.ui.sr_cas.clear()
        self.ui.max_cas.clear()
        self.ui.min_cas.clear()
        self.ui.sr_cek.clear()
        self.ui.max_cek.clear()
        self.ui.min_cek.clear()
        self.block_water(False, False, False, False, False, False, False, False, False)
    def block_water(self, one, two, three, four, five, six, seven, eight, nine):
        self.ui.sr_syt.setReadOnly(one)
        self.ui.max_syt.setReadOnly(two)
        self.ui.min_syt.setReadOnly(three)
        self.ui.sr_cas.setReadOnly(four)
        self.ui.max_cas.setReadOnly(five)
        self.ui.min_cas.setReadOnly(six)
        self.ui.sr_cek.setReadOnly(seven)
        self.ui.max_cek.setReadOnly(eight)
        self.ui.min_cek.setReadOnly(nine)




    ########################################
    ### Добавить расход в правую область ###
    #######################################
    def add_consumption_water(self, widget, name, kol_vo, dimension, type):
        if widget in self.right_obj:
            change = self.right_obj[widget]
            change.change_right(kol_vo)
        else:
            self.ui.expenditure_right_type.setStyleSheet('background-color:rgb(138, 161, 233);')
            self.ui.expenditure_right_type.setText(type)
            expenditure_class = Expenditure_class(name, kol_vo, dimension, 1, widget)
            self.right_obj.update({widget: expenditure_class})
            self.ui.lay_expenditure_right.addWidget(expenditure_class)
            #expenditure_class.delet.connect(self.del_char_right)
    def delete_right_consumption(self):
        pass


    #################################
    ### Добавление веществ в БД ###
    #################################
    def radio_btn(self):
        bg_sub = QButtonGroup(self)
        bg_sub.addButton(self.ui.insoluble_rb)
        bg_sub.addButton(self.ui.soluble_rb)
        bg_sub_del = QButtonGroup(self)
        bg_sub_del.addButton(self.ui.insoluble_rb_del)
        bg_sub_del.addButton(self.ui.soluble_rb_del)
    def add_substance_in_DB(self):
        name = self.ui.name_sub_add.text()
        if self.ui.insoluble_rb.isChecked():
            if add_insoluble(name) is None:
                self.ui.error_sub_add.setText("Данное вещество уже есть в программе")
            else:
                self.list_of_insoluble.append(name)
                self.add_sub_insoluble()
                self.ui.name_sub_add.clear()
                self.ui.error_sub_add.clear()
                self.ui.stackedWidget.setCurrentWidget(self.ui.substance)
        elif self.ui.soluble_rb.isChecked():
            if add_soluble(name) is None:
                self.ui.error_sub_add.setText("Данное вещество уже есть в программе")
            else:
                self.list_of_soluble.append(name)
                self.add_sub_soluble()
                print(self.list_of_soluble)
                self.ui.name_sub_add.clear()
                self.ui.error_sub_add.clear()
                self.ui.stackedWidget.setCurrentWidget(self.ui.substance)
    #################################
    ### Удаление веществ из БД ###
    #################################
    def del_substance_in_DB(self):
        name = self.ui.name_sub_del.text()
        if self.ui.insoluble_rb_del.isChecked():
            if del_insoluble(name) is None:
                self.ui.error_sub_del.setText("Не правильно")
            else:
                self.ui.name_sub_del.clear()
                self.ui.error_sub_del.clear()
                self.ui.stackedWidget.setCurrentWidget(self.ui.substance)
        elif self.ui.soluble_rb_del.isChecked():
            if del_soluble(name) is None:
                self.ui.error_sub_del.setText("Данного вещества нет в базе")
            else:
                self.ui.name_sub_del.clear()
                self.ui.error_sub_del.clear()
                self.ui.stackedWidget.setCurrentWidget(self.ui.substance)



    def get_scheme(self):
        self.ui.gotov_shema.setText("")
        self.getDirectory()
        stroka = 'Схема'
        spisok, money = enumeration(self.file, self.water_expenditure, self.concentration, float(self.ui.money.text()))
        for i in range(len(spisok)):
            stroka += '\n'
            stroka += '\n' + 'Название: '
            stroka += '\n' + spisok[i].get('name')
            stroka += '\n' + 'Начальная концентрация: '
            stroka += '\n' + str(spisok[i].get('start'))
            stroka += '\n' + 'Эффективность: '
            stroka += '\n' + str(spisok[i].get('effectiv'))
            stroka += '\n' + 'Конечная концентрация: '
            stroka += '\n' + str(spisok[i].get('end'))
            stroka += '\n' + 'Конечная концентрация/ПДК: '
            stroka += '\n' + str(spisok[i].get('end/PDK'))
            stroka += '\n' + 'Цена: '
            stroka += '\n' + str(spisok[i].get('cost'))
            # ''.join({s1: 'a', s2: 'b'})
        stroka += '\n' + 'Итоговая цена: '
        stroka += '\n' + str(money)
        print(stroka)
        print(type(stroka))
        self.ui.plainTextEdit.appendPlainText(stroka)
        self.ui.gotov_shema.setText("Схема готова")

    def getDirectory(self):
        self.file, check = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName() Demo",
                                                  "", ".xlsx (*.xlsx)")



    #################################
    def mainwind_start(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.substance)
    def close_windows(self):
        self.close()
        self.first_open = True
        clean_DB()


    def maxim(self):
        self.setWindowState(QtCore.Qt.WindowMaximized)
    def minimized(self):
        self.setWindowState(QtCore.Qt.WindowMinimized)
        # QtCore.Qt.WindowMinimized


app = QtWidgets.QApplication([])
application = Mywindow()
application.show()
application.mainwind_start()
sys.exit(app.exec_())
