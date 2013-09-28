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
        self.populate()

        self.tableView = QTableView(self)
        self.tableView.setModel(self.table)

        self.collapseButton = QPushButton('Collapse', self)
        self.collapseButton.clicked.connect(self.collapse)
        self.collapseAllButton = QPushButton('Collapse All', self)
        self.collapseAllButton.clicked.connect(self.collapseAll)

        widget = QWidget(self)
        layout = QVBoxLayout()

        layout.addWidget(self.tableView)
        layout.addWidget(self.collapseButton)
        layout.addWidget(self.collapseAllButton)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.statusBar().showMessage('Welcome')

    def populate(self):
        self.table.setItem(0, 5, QStandardItem('4'))
        self.table.setItem(0, 4, QStandardItem('3'))
        self.table.setItem(2, 3, QStandardItem('3'))
        self.table.setItem(2, 1, QStandardItem('2'))

    def collapse(self):
        """Step by step collapse."""
        for cell in self.table.collapsable():
            self.table.collapse(cell[0], cell[1])

    def collapseAll(self):
        """Collapse all at once."""
        while self.table.collapsable() != []:
            for cell in self.table.collapsable():
                self.table.collapse(cell[0], cell[1])
