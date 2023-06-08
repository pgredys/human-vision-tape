import sys
from PySide6 import QtWidgets
from widget import Widget


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = Widget()
    window.show()
    app.exec()
