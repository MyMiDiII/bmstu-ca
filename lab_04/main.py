import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

from MainWindow import Ui_MainWindow
from graphics import generate

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

        self.plotBtn.clicked.connect(generate)
        self.table_init()

    def table_init(self):
        self.pointsTable.setColumnCount(3)
        self.pointsTable.setRowCount(1)
        delegate = DoubleDelegate()
        for i in range(3):
            self.pointsTable.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
            self.pointsTable.setItemDelegateForColumn(i, delegate)


if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
