# -*-coding:Utf-8 -*

from PySide.QtGui import QTableView
from PySide.QtCore import *
from PySide.QtGui import *

class View(QTableView):
    """Custom view."""

    def __init__(self, parent=None):
        QTableView.__init__(self, parent)

    """def mouseReleaseEvent(self, event):
        if(event.button == Qt.NoButton):
            print('there')
            index = self.indexAt(event.localPos())
            self.model.addOne(index)
        else:
            print('ouch')"""
            