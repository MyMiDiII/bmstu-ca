import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
import matplotlib.pyplot as plt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi('mainwindow.ui', self)
        self.plotBtn.clicked.connect(generate)

        self.pointsTable.setColumnCount(3)
        self.pointsTable.setRowCount(1)
        self.pointsTable.setItem(0, 0, QTableWidgetItem("0.9989"))
        self.pointsTable.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.pointsTable.setItem(0, 2, QTableWidgetItem("Text in column 3"))
        self.pointsTable.horizontalHeader().setSectionResizeMode(2,QtWidgets.QHeaderView.Stretch)
        print(self.pointsTable.item(0,0).text())


def generate():
    plt.scatter(1.0, 1.0)
    plt.show()


if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)

    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
