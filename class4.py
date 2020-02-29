# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 140, 600, 450))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(830, 120, 101, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mapbox = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.mapbox.setObjectName("mapbox")
        self.verticalLayout.addWidget(self.mapbox)
        self.maptrfsklbox = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.maptrfsklbox.setObjectName("maptrfsklbox")
        self.verticalLayout.addWidget(self.maptrfsklbox)
        self.satbox = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.satbox.setObjectName("satbox")
        self.verticalLayout.addWidget(self.satbox)
        self.sklbox = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.sklbox.setObjectName("sklbox")
        self.verticalLayout.addWidget(self.sklbox)
        self.sattrfsklbox = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.sattrfsklbox.setObjectName("sattrfsklbox")
        self.verticalLayout.addWidget(self.sattrfsklbox)
        self.satsklbox = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.satsklbox.setObjectName("satsklbox")
        self.verticalLayout.addWidget(self.satsklbox)
        self.address_input = QtWidgets.QLineEdit(self.centralwidget)
        self.address_input.setGeometry(QtCore.QRect(100, 0, 621, 41))
        self.address_input.setObjectName("address_input")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(770, 0, 121, 41))
        self.search_button.setObjectName("search_buuton")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(770, 40, 121, 41))
        self.clear_button.setObjectName("clear_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mapbox.setText(_translate("MainWindow", "map"))
        self.maptrfsklbox.setText(_translate("MainWindow", "map,trf,skl"))
        self.satbox.setText(_translate("MainWindow", "sat"))
        self.sklbox.setText(_translate("MainWindow", "skl"))
        self.sattrfsklbox.setText(_translate("MainWindow", "sat,trf,skl"))
        self.satsklbox.setText(_translate("MainWindow", "sat,skl"))
        self.search_button.setText(_translate("MainWindow", "Искать"))
        self.clear_button.setText(_translate("MainWindow", "Сбросить"))
