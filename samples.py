# -*-coding:Utf-8 -*

import sys
from src.mainWindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

############################

from PySide.QtCore import *
from PySide.QtGui import *

brush = QBrush()

table.item(row, column).setBackground(brush.setColor(QColor(r, g, b)))

