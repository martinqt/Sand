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

        self.table = Table(10, 20, self)
        self.populate()

        self.tableView = QTableView(self)
        self.tableView.setModel(self.table)

        horizontal = QHeaderView(Qt.Horizontal)
        horizontal.setResizeMode(QHeaderView.Stretch)
        self.tableView.setHorizontalHeader(horizontal)

        vertical = QHeaderView(Qt.Vertical)
        vertical.setResizeMode(QHeaderView.Stretch)
        self.tableView.setVerticalHeader(vertical)

        self.collapseButton = QPushButton('Collapse', self)
        self.collapseButton.clicked.connect(self.collapse)
        self.collapseAllButton = QPushButton('Collapse All', self)
        self.collapseAllButton.clicked.connect(self.collapseAll)

        self.reloadButton = QPushButton('Reload', self)
        self.reloadButton.clicked.connect(self.populate)

        widget = QWidget(self)
        layout = QVBoxLayout()

        layout.addWidget(self.tableView)
        layout.addWidget(self.collapseButton)
        layout.addWidget(self.collapseAllButton)
        layout.addWidget(self.reloadButton)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.statusBar().showMessage('Welcome')

    def populate(self):
        self.table.clear()
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
