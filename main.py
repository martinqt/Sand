# -*-coding:Utf-8 -*

import sys
from src.MainWindow import MainWindow
from PySide.QtGui import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
