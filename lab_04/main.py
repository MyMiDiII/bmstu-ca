"""
    Модуль для запуска программы
    ЛАБОРАТОРНАЯ РАБОТА №4
    ПОСТРОЕНИЕ И ПРОГРАММНАЯ РЕАЛИЗАЦИЯ АЛГОРИТМА
    НАИЛУЧШЕГО СРЕДНЕКВАДРАТИЧНОГО ПРИБЛИЖЕНИЯ
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
import matplotlib.pyplot as plt

from MainWindow import Ui_MainWindow
import points
import graphics

class DoubleDelegate(QtWidgets.QItemDelegate):

    def createEditor(self, parent, option, index):
        self.doubleSpin = QtWidgets.QDoubleSpinBox(parent)
        self.doubleSpin.setMaximum(1000)
        if index.column() == 2:
            self.doubleSpin.setMinimum(0)
        else:
            self.doubleSpin.setMinimum(-1000)
        return self.doubleSpin


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.table_init()
        self.generateBtn.clicked.connect(self.generateTable)
        self.weightsRadioBtn.clicked.connect(self.switch)
        self.plotBtn.clicked.connect(self.getPlots)


    def table_init(self):
        self.pointsTable.setColumnCount(3)
        delegate = DoubleDelegate()
        for i in range(3):
            self.pointsTable.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
            self.pointsTable.setItemDelegateForColumn(i, delegate)


    def switch(self):
        self.weightsDSpin.setDisabled(self.weightsDSpin.isEnabled())


    def generateTable(self):
        num = self.pointsNumSpin.value()

        equal = [False, 0.]
        if (self.weightsRadioBtn.isChecked()):
            equal = [True, self.weightsDSpin.value()]

        table = points.generateTable(num, equal)

        self.pointsTable.setRowCount(num)
        for i, rec in enumerate(table):
            for j, value in enumerate(rec):
                self.pointsTable.setItem(i, j, QTableWidgetItem(str(value)))


    def getPlots(self):
        checks = [
            self.degree1Check,
            self.degree2Check,
            self.degree3Check,
            self.degree4Check,
            self.degree5Check
            ]

        degrees = []
        for i, check in enumerate(checks):
            if (check.isChecked()):
                degrees.append(i + 1)

        plt.close()

        table = self.getTable()

        for degree in degrees:
            plot = graphics.getPlot(table, degree)
            plt.plot(plot[0], plot[1])

        plt.show()

    
    def getTable(self):
        table = []
        for i in range(self.pointsTable.rowCount()):
            table.append([float(self.pointsTable.item(i, j).text())
                          for j in range(3)])
        return table


if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
