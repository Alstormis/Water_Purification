# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'small_division_expenditure.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_expenditure(object):
    def setupUi(self, expenditure):
        expenditure.setObjectName("expenditure")
        expenditure.resize(690, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(expenditure)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_29 = QtWidgets.QWidget(expenditure)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.widget_29.setFont(font)
        self.widget_29.setStyleSheet("border-radius: 8px;\n"
"background-color:rgb(248, 249, 251);\n"
"color: rgb(140, 139, 139);")
        self.widget_29.setObjectName("widget_29")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.widget_29)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.name_expenditure = QtWidgets.QLabel(self.widget_29)
        self.name_expenditure.setMinimumSize(QtCore.QSize(0, 0))
        self.name_expenditure.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_expenditure.setFont(font)
        self.name_expenditure.setStyleSheet("background-color:rgb(248, 249, 251);\n"
"color: rgb(0, 0, 0);\n"
"margin-right: 0px;\n"
"")
        self.name_expenditure.setInputMethodHints(QtCore.Qt.ImhNone)
        self.name_expenditure.setWordWrap(True)
        self.name_expenditure.setObjectName("name_expenditure")
        self.horizontalLayout_55.addWidget(self.name_expenditure)
        self.value_expenditure = QtWidgets.QLineEdit(self.widget_29)
        self.value_expenditure.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.value_expenditure.setFont(font)
        self.value_expenditure.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.value_expenditure.setStyleSheet("background-color:rgb(248, 249, 251);\n"
"color: rgb(140, 139, 139);\n"
"outline: 0px;\n"
"padding-left: 10px;\n"
"margin-left: 20px;\n"
"margin-right: 10px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 00px;\n"
"border: none;\n"
"\n"
"")
        self.value_expenditure.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_expenditure.setObjectName("value_expenditure")
        self.horizontalLayout_55.addWidget(self.value_expenditure)
        self.dimension_expenditure = QtWidgets.QLabel(self.widget_29)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dimension_expenditure.setFont(font)
        self.dimension_expenditure.setStyleSheet("margin-right: 10px;\n"
"")
        self.dimension_expenditure.setObjectName("dimension_expenditure")
        self.horizontalLayout_55.addWidget(self.dimension_expenditure)
        self.clean_expenditure = QtWidgets.QPushButton(self.widget_29)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.clean_expenditure.setFont(font)
        self.clean_expenditure.setStyleSheet("QPushButton {\n"
"background-color:rgb(138, 161, 233);\n"
"color:rgb(255, 255, 255);\n"
"font-weight: 600;\n"
"border-radius: 8px;\n"
"padding: 5px 15px;\n"
"outline: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(125, 143, 202);\n"
"}")
        self.clean_expenditure.setObjectName("clean_expenditure")
        self.horizontalLayout_55.addWidget(self.clean_expenditure)
        self.value_expenditure.raise_()
        self.name_expenditure.raise_()
        self.dimension_expenditure.raise_()
        self.clean_expenditure.raise_()
        self.verticalLayout.addWidget(self.widget_29)

        self.retranslateUi(expenditure)
        QtCore.QMetaObject.connectSlotsByName(expenditure)

    def retranslateUi(self, expenditure):
        _translate = QtCore.QCoreApplication.translate
        expenditure.setWindowTitle(_translate("expenditure", "Form"))
        self.name_expenditure.setText(_translate("expenditure", "Вода"))
        self.value_expenditure.setPlaceholderText(_translate("expenditure", "0"))
        self.dimension_expenditure.setText(_translate("expenditure", "°C"))
        self.clean_expenditure.setText(_translate("expenditure", "-"))
