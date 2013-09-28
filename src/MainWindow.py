# -*-coding:Utf-8 -*

from PySide.QtCore import *
from PySide.QtGui import *
from src.Table import Table

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.resize(700, 500)
        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Sand Table')

        self.table = Table(5, 6, self)
        self.tableView = QTableView(self)
        self.tableView.setModel(self.table)

        widget = QWidget(self)
        layout = QVBoxLayout()

        layout.addWidget(self.tableView)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.statusBar().showMessage('Welcome')
