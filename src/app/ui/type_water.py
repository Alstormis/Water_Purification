# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'type_water.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Water(object):
    def setupUi(self, Water):
        Water.setObjectName("Water")
        Water.resize(779, 110)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Water)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_8 = QtWidgets.QWidget(Water)
        self.widget_8.setStyleSheet("border-radius: 8px;\n"
"background-color:rgb(248, 249, 251);\n"
"color: rgb(140, 139, 139);")
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_22.setContentsMargins(0, 9, 9, 9)
        self.horizontalLayout_22.setSpacing(20)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.water_rb_btn = QtWidgets.QRadioButton(self.widget_8)
        self.water_rb_btn.setStyleSheet("")
        self.water_rb_btn.setText("")
        self.water_rb_btn.setObjectName("water_rb_btn")
        self.horizontalLayout_22.addWidget(self.water_rb_btn)
        self.name_water = QtWidgets.QLabel(self.widget_8)
        self.name_water.setMinimumSize(QtCore.QSize(300, 0))
        self.name_water.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_water.setFont(font)
        self.name_water.setStyleSheet("background-color:rgb(248, 249, 251);\n"
"color: rgb(0, 0, 0);\n"
"margin-right: 0px;\n"
"")
        self.name_water.setInputMethodHints(QtCore.Qt.ImhNone)
        self.name_water.setWordWrap(True)
        self.name_water.setObjectName("name_water")
        self.horizontalLayout_22.addWidget(self.name_water)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"background-color:rgb(240, 241, 242);\n"
"color:rgb(255, 255, 255);\n"
"font-weight: 600;\n"
"border-radius: 8px;\n"
"padding: 5px 15px;\n"
"margin-top: 10px;\n"
"outline: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(125, 143, 202);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/editing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QtCore.QSize(20, 36))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_22.addWidget(self.pushButton_9)
        self.horizontalLayout_22.setStretch(1, 2)
        self.horizontalLayout.addWidget(self.widget_8)

        self.retranslateUi(Water)
        QtCore.QMetaObject.connectSlotsByName(Water)

    def retranslateUi(self, Water):
        _translate = QtCore.QCoreApplication.translate
        Water.setWindowTitle(_translate("Water", "Form"))
        self.name_water.setText(_translate("Water", "Вода"))

