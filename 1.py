from PyQt5 import QtWidgets, QtGui, QtCore
from class4 import Ui_MainWindow
import sys
import requests
import os


class YandexMapsAPI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ll = [0, 0]
        self.spn = [30.0, 30.0]
        self.l = ''
        self.static_API()
        self.mapbox.clicked.connect(self.box_callback)
        self.satbox.clicked.connect(self.box_callback)
        self.sklbox.clicked.connect(self.box_callback)
        self.maptrfsklbox.clicked.connect(self.box_callback)
        self.satsklbox.clicked.connect(self.box_callback)
        self.sattrfsklbox.clicked.connect(self.box_callback)

    def static_API(self):
        params = {
            'll': str(self.ll[0]) + ',' + str(self.ll[1]),
            'spn': str(self.spn[0]) + ',' + str(self.spn[1]),
            'l': self.l if self.l else 'map'
        }
        address = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(address, params=params)
        try:
            os.remove('img.png')
        except FileNotFoundError:
            pass
        with open('img.png', 'wb') as file:
            file.write(response.content)
        self.image = QtGui.QPixmap('img.png')
        print('changed')
        self.show_map()

    def show_map(self):
        self.label.setPixmap(self.image)
        print('showed')

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_PageUp:
            if self.spn[0] < 180 and self.spn[1] < 90:
                self.spn[0] *= 1.5
                self.spn[1] *= 1.5
                if self.spn[0] > 180 or self.spn[1] > 90:
                    self.spn = [180, 90]
                self.static_API()
        if e.key() == QtCore.Qt.Key_PageDown:
            if self.spn[0] > 0.001 and self.spn[1] > 0.001:
                self.spn[0] *= 0.5
                self.spn[1] *= 0.5
                if self.spn[0] < 0.001 or self.spn[1] < 0.001:
                    self.spn = [0.001, 0.001]
                self.static_API()
        if e.key() == QtCore.Qt.Key_W:
            if -90 < self.ll[1] < 90:
                self.ll[1] += 50 * ((self.spn[0] + self.spn[1]) / 2) / 180
                if not (-90 < self.ll[1] < 90):
                    self.ll[1] = 0
                self.static_API()
        if e.key() == QtCore.Qt.Key_S:
            if -90 < self.ll[1] < 90:
                self.ll[1] -= 50 * ((self.spn[0] + self.spn[1]) / 2) / 180
                if not (-90 < self.ll[1] < 90):
                    self.ll[1] = 0
                self.static_API()
        if e.key() == QtCore.Qt.Key_D:
            self.ll[0] += 50 * ((self.spn[0] + self.spn[1]) / 2) / 180
            if self.ll[0] > 180:
                self.ll[0] -= 360
            self.static_API()
        if e.key() == QtCore.Qt.Key_A:
            self.ll[0] -= 50 * ((self.spn[0] + self.spn[1]) / 2) / 180
            if self.ll[0] < -180:
                self.ll[0] += 360
            self.static_API()

        print(e.key())

    def box_callback(self, instance):
        self.l = self.sender().text()
        print(self.l, 'new map')
        self.static_API()


def exit_(app):
    app.exec()
    os.remove('img.png')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    program = YandexMapsAPI()
    program.show()
    sys.exit(exit_(app))
