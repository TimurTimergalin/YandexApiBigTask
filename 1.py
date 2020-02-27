from PyQt5 import QtWidgets, QtGui, QtCore
from class1 import Ui_MainWindow
import sys
import requests
import os


class YandexMapsAPI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ll = 0, 0
        self.spn = 30, 30
        self.static_API()

    def static_API(self):
        params = {
            'll': str(self.ll[0]) + ',' + str(self.ll[1]),
            'spn': str(self.spn[0]) + ',' + str(self.spn[1]),
            'l': 'map'
        }
        address = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(address, params=params)
        with open('img.png', 'wb') as file:
            file.write(response.content)
        self.image = QtGui.QPixmap('img.png')
        self.show_map()

    def show_map(self):
        self.label.setPixmap(self.image)


def exit_(app):
    app.exec()
    os.remove('img.png')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    program = YandexMapsAPI()
    program.show()
    sys.exit(exit_(app))
