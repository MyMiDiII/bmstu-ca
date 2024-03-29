# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 806)
        MainWindow.setMinimumSize(QtCore.QSize(501, 806))
        MainWindow.setMaximumSize(QtCore.QSize(501, 806))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pointsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.pointsTable.setMinimumSize(QtCore.QSize(0, 0))
        self.pointsTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.pointsTable.setObjectName("pointsTable")
        self.pointsTable.setColumnCount(3)
        self.pointsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pointsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointsTable.setHorizontalHeaderItem(2, item)
        self.pointsTable.horizontalHeader().setVisible(True)
        self.pointsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.pointsTable.verticalHeader().setVisible(True)
        self.pointsTable.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.pointsTable)
        self.pointsNumHLayout = QtWidgets.QHBoxLayout()
        self.pointsNumHLayout.setObjectName("pointsNumHLayout")
        self.pointsNumLbl = QtWidgets.QLabel(self.centralwidget)
        self.pointsNumLbl.setObjectName("pointsNumLbl")
        self.pointsNumHLayout.addWidget(self.pointsNumLbl)
        self.pointsNumSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.pointsNumSpin.setMinimum(1)
        self.pointsNumSpin.setMaximum(1000)
        self.pointsNumSpin.setObjectName("pointsNumSpin")
        self.pointsNumHLayout.addWidget(self.pointsNumSpin)
        self.verticalLayout.addLayout(self.pointsNumHLayout)
        self.weightsHLayout = QtWidgets.QHBoxLayout()
        self.weightsHLayout.setObjectName("weightsHLayout")
        self.weightsRadioBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.weightsRadioBtn.setObjectName("weightsRadioBtn")
        self.weightsHLayout.addWidget(self.weightsRadioBtn)
        self.weightsDSpin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.weightsDSpin.setEnabled(False)
        self.weightsDSpin.setMinimum(0.0)
        self.weightsDSpin.setMaximum(1000.0)
        self.weightsDSpin.setObjectName("weightsDSpin")
        self.weightsHLayout.addWidget(self.weightsDSpin)
        self.verticalLayout.addLayout(self.weightsHLayout)
        self.generateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.generateBtn.setObjectName("generateBtn")
        self.verticalLayout.addWidget(self.generateBtn)
        self.polyomialLbl = QtWidgets.QLabel(self.centralwidget)
        self.polyomialLbl.setObjectName("polyomialLbl")
        self.verticalLayout.addWidget(self.polyomialLbl)
        self.degreesHLayout = QtWidgets.QHBoxLayout()
        self.degreesHLayout.setObjectName("degreesHLayout")
        self.degree1Check = QtWidgets.QCheckBox(self.centralwidget)
        self.degree1Check.setObjectName("degree1Check")
        self.degreesHLayout.addWidget(self.degree1Check)
        self.degree2Check = QtWidgets.QCheckBox(self.centralwidget)
        self.degree2Check.setObjectName("degree2Check")
        self.degreesHLayout.addWidget(self.degree2Check)
        self.degree3Check = QtWidgets.QCheckBox(self.centralwidget)
        self.degree3Check.setObjectName("degree3Check")
        self.degreesHLayout.addWidget(self.degree3Check)
        self.degree4Check = QtWidgets.QCheckBox(self.centralwidget)
        self.degree4Check.setObjectName("degree4Check")
        self.degreesHLayout.addWidget(self.degree4Check)
        self.degree5Check = QtWidgets.QCheckBox(self.centralwidget)
        self.degree5Check.setObjectName("degree5Check")
        self.degreesHLayout.addWidget(self.degree5Check)
        self.verticalLayout.addLayout(self.degreesHLayout)
        self.plotBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plotBtn.setObjectName("plotBtn")
        self.verticalLayout.addWidget(self.plotBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 501, 28))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.pointsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x"))
        item = self.pointsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y"))
        item = self.pointsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ρ"))
        self.pointsNumLbl.setText(_translate("MainWindow", "Количество узлов:"))
        self.weightsRadioBtn.setText(_translate("MainWindow", "Одинаковые веса"))
        self.generateBtn.setText(_translate("MainWindow", "Сгенерировать таблицу"))
        self.polyomialLbl.setText(_translate("MainWindow", "Степень аппроксимирующeго полинома:"))
        self.degree1Check.setText(_translate("MainWindow", "1"))
        self.degree2Check.setText(_translate("MainWindow", "2"))
        self.degree3Check.setText(_translate("MainWindow", "3"))
        self.degree4Check.setText(_translate("MainWindow", "4"))
        self.degree5Check.setText(_translate("MainWindow", "5"))
        self.plotBtn.setText(_translate("MainWindow", "Построить графики"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
