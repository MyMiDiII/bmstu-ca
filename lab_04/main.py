import sys  
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Загрузите страницу интерфейса
        uic.loadUi('mainwindow.ui', self)

        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

    # мы добавили метод plot(), который принимает два массива: 
    # temperature и hour, затем строит данные с помощью метода graphWidget.plot().

    def plot(self, hour, temperature):
        self.graphWidget.plot(hour, temperature)

if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
