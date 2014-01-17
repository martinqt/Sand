# -*-coding:Utf-8 -*

from PySide.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PySide.QtCore import *
from PySide.QtGui import *
import pickle

class Table(QStandardItemModel):
    """Represents the 'sand table'."""

    def __init__(self, columns, rows, limit, parent=None):
        QStandardItemModel.__init__(self, rows, columns, parent)

        self.height = rows
        self.width = columns
        self.limit = limit

        self.clear()

    def exists(self, row, column):
        """Checks if the cell exists"""
        if((row >= self.height or not row >= 0) or (column >= self.width or not column >= 0)):
            return False

        return True

    def collapsable(self):
        """Returns collapsable cells under the [row, column] format"""
        i = 0
        cells = []

        while i < self.height:
            j = 0

            while j < self.width:
                if (int(self.item(i, j).text()) > self.limit-1):
                    cells.append([i, j])

                j += 1

            i += 1

        return cells

    def collapse(self, row, column):
        value = int(self.item(row, column).text())
        nb = int(value/self.limit)
        remains = value%self.limit

        self.setItem(row, column, QStandardItem(str(remains)))

        if(self.exists(row+1, column)):
            self.setItem(row+1, column, QStandardItem(str(int(self.item(row+1, column).text())+nb)))
        if(self.exists(row-1, column)):
            self.setItem(row-1, column, QStandardItem(str(int(self.item(row-1, column).text())+nb)))
        if(self.exists(row, column+1)):
            self.setItem(row, column+1, QStandardItem(str(int(self.item(row, column+1).text())+nb)))
        if(self.exists(row, column-1)):
            self.setItem(row, column-1, QStandardItem(str(int(self.item(row, column-1).text())+nb)))

    def clear(self):
        self.fill(0)

    def data(self, index, role = Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if(self.item(index.row(), index.column()).text() == '0'):
                return ''
            else:
                return self.item(index.row(), index.column()).text()

        elif(role == Qt.BackgroundRole):
            if(self.item(index.row(), index.column()).text() == ''):
                return QColor(230, 255, 240)
            elif(int(self.item(index.row(), index.column()).text()) == 0):
                return QColor(230, 255, 240)

            elif(int(self.item(index.row(), index.column()).text()) == 1):
                return QColor(230, 255, 145)

            elif(int(self.item(index.row(), index.column()).text()) == 2):
                return QColor(255, 245, 140)

            elif(int(self.item(index.row(), index.column()).text()) == 3):
                return QColor(255, 190, 125)

            else:
                return QColor(255, 0, 0)

        elif(role == Qt.TextAlignmentRole):
            return Qt.AlignCenter;

        return None

    def addOne(self, index):
        self.setItem(index.row(), index.column(), QStandardItem(str(int(self.item(index.row(), index.column()).text())+1)))

    def collapseAll(self):
        """Collapse all at once."""
        i=0
        while self.collapsable() != []:
            for cell in self.collapsable():
                self.collapse(cell[0], cell[1])
            if(i>1000):
                self.writePickled()
                i=0
            i+=1

    def fill(self, value):
        i = 0

        while i < self.height:
            j = 0

            while j < self.width:
                self.setItem(i, j, QStandardItem(value))

                j += 1

            i += 1

    def toList(self):
        i = 0
        mat = list()

        while i < self.height:
            j = 0
            row = list()
            while j < self.width:
                row.append(int(self.item(i,j).text()))
                j += 1

            mat.append(list(row))
            i += 1

        return mat

    def fromList(self, mat):
        i = 0

        while i < self.height:
            j = 0
            while j < self.width:
                self.setItem(i, j, QStandardItem(mat[i][j]))
                j += 1

            i += 1

        return mat

    def writePickled(self):
        """Write pickled dump file"""
        with open('tmp/table.dump', 'wb') as fileObj:
            pickle.dump(self.toList(), fileObj)

    def readPickled(self):
        """Load pickled dump file"""
        return 0
        with open('tmp/table.dump', 'rb') as fileObj:
            self.fromList(pickle.load(fileObj))
