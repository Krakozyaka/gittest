# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parent_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnotherWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 231, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_.setGeometry(QtCore.QRect(259, 130, 75, 23))
        self.pushButton_.setObjectName("pushButton_")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(259, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(259, 100, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(259, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(332, 101, 41, 21))
        self.comboBox.setObjectName("comboBox")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(260, 160, 211, 71))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 47, 13))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_1.setText(_translate("MainWindow", "Удалить"))
        self.label.setText(_translate("MainWindow", "Ввод:"))
