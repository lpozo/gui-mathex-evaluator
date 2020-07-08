import sys

from PyQt5.QtWidgets import QApplication

from controller import MainCtrl


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = MainCtrl()
    controller.showWindow()
    sys.exit(app.exec_())
