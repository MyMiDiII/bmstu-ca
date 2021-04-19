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

class doubleDelegate(QtWidgets.QItemDelegate):
    """
        Класс настройки полей для ввода
        вещественных чисел
    """

    def createEditor(self, parent, option, index):
        """
            Настройка поля ввода на
            получение только вещественных чисел
        """
        self.doubleSpin = QtWidgets.QDoubleSpinBox(parent)
        self.doubleSpin.setMaximum(1000)
        if index.column() == 2:
            self.doubleSpin.setMinimum(0)
        else:
            self.doubleSpin.setMinimum(-1000)
        return self.doubleSpin


def callError(title, text):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec_()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
        Класс главного окна
    """

    def __init__(self, *args, **kwargs):
        """
            Инициализация главного окна
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.table_init()
        self.generateBtn.clicked.connect(self.generateTable)
        self.weightsRadioBtn.clicked.connect(self.switch)
        self.plotBtn.clicked.connect(self.getPlots)


    def table_init(self):
        """
            Начальные настройки таблицы
        """
        self.pointsTable.setColumnCount(3)
        delegate = doubleDelegate()
        for i in range(3):
            self.pointsTable.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
            self.pointsTable.setItemDelegateForColumn(i, delegate)


    def switch(self):
        """
            Блокировка/разблокировка поля ввода веса
        """
        self.weightsDSpin.setDisabled(self.weightsDSpin.isEnabled())


    def generateTable(self):
        """
            Генерация таблицы по введенным данным
        """
        num = self.pointsNumSpin.value()

        equal = [False, 0.]
        if self.weightsRadioBtn.isChecked():
            equal = [True, self.weightsDSpin.value()]

        table = points.generateTable(num, equal)

        self.pointsTable.setRowCount(num)
        for i, rec in enumerate(table):
            for j, value in enumerate(rec):
                self.pointsTable.setItem(i, j, QTableWidgetItem(str(value)))


    def getPlots(self):
        """
            Получение графиков по таблице
        """
        checks = [
            self.degree1Check,
            self.degree2Check,
            self.degree3Check,
            self.degree4Check,
            self.degree5Check
            ]

        degrees = []
        for i, check in enumerate(checks):
            if check.isChecked():
                if i + 1 >= self.pointsTable.rowCount():
                    callError("n >= N!", "Полином не может быть построен")
                    return

                degrees.append(i + 1)

        plt.close()

        table = self.getTable()
        plt.plot(graphics.getXs(table), graphics.getYs(table),
                 "o", label="Исходные")

        for degree in degrees:
            plot = graphics.getPlot(table, degree)
            plt.plot(plot[0], plot[1], label="{:d}-я степень".format(degree))

        plt.get_current_fig_manager().window.move(700, 100)
        plt.get_current_fig_manager().resize(1000, 758)
        plt.grid()
        plt.legend()
        plt.show()


    def getTable(self):
        """
            Получение таблицы
        """
        table = []
        for i in range(self.pointsTable.rowCount()):
            table.append([float(self.pointsTable.item(i, j).text())
                          for j in range(3)])
        return table


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.move(200, 100)
    main.show()
    sys.exit(app.exec_())
