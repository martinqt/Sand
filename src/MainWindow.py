# -*-coding:Utf-8 -*

from PySide.QtCore import *
from PySide.QtGui import *
from src.Table import Table
import pickle

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.resize(800, 800)
        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Sand Table')

        self.timer = QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.collapse)

        self.table = Table(31, 31, self)

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
        self.collapseAutoButton = QPushButton('Start Auto Collapse', self)
        self.collapseAutoButton.clicked.connect(self.start)
        self.stopCollapseAutoButton = QPushButton('Stop Auto Collapse', self)
        self.stopCollapseAutoButton.clicked.connect(self.stop)

        self.reloadButton = QPushButton('Reload', self)
        self.reloadButton.clicked.connect(self.load)
        self.saveButton = QPushButton('Save', self)
        self.saveButton.clicked.connect(self.save)

        self.clearButton = QPushButton('Clear', self)
        self.clearButton.clicked.connect(self.clear)
        
        self.reloadButton.setEnabled(False)
        self.saveButton.setEnabled(False)

        widget = QWidget(self)
        layout = QHBoxLayout()
        subLayout = QVBoxLayout()

        layout.addWidget(self.tableView)
        subLayout.addWidget(self.collapseButton)
        subLayout.addWidget(self.collapseAllButton)
        subLayout.addWidget(self.collapseAutoButton)
        subLayout.addWidget(self.stopCollapseAutoButton)
        subLayout.addWidget(self.clearButton)
        subLayout.addWidget(self.reloadButton)
        subLayout.addWidget(self.saveButton)
        layout.addLayout(subLayout)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.statusBar().showMessage('Welcome')

    def load(self):
        return 0

        with open('table', 'rb') as fileObj:
            self.table = pickle.load(fileObj)

    def clear(self):
        self.table.clear()

    def collapse(self):
        """Step by step collapse."""
        if(self.table.collapsable() != []):
            for cell in self.table.collapsable():
                self.table.collapse(cell[0], cell[1])
        else:
            self.stop()

    def collapseAll(self):
        """Collapse all at once."""
        while self.table.collapsable() != []:
            for cell in self.table.collapsable():
                self.table.collapse(cell[0], cell[1])

    def save(self):
        return 0

        with open('table', 'wb') as fileObj:
            pickle.dump(self.table, fileObj)

    def start(self):
        """Start the timer."""
        if(not self.timer.isActive()):
            self.collapseButton.setEnabled(False)
            self.collapseAllButton.setEnabled(False)
            self.timer.start()
            self.statusBar().showMessage('Auto mode started')

    def stop(self):
        """Stop the timer."""
        self.timer.stop()
        self.statusBar().showMessage('Auto mode stopped')
        self.collapseButton.setEnabled(True)
        self.collapseAllButton.setEnabled(True)
