# -*-coding:Utf-8 -*

##############################

#Array class

#table.collapse(0,5) -> collapse the cell if it value is higher than 3
#table.collapsable() -> return an array of collapsable cells


#table.get(0, 5) -> access the cell
#table.set(0, 5, 3) -> set the cell value
#table.exists(0,5) -> wether or not this is an existing cell

# def __getitem__(self, index):
# def __setitem__(self, index, valeur):
##############################

#http://srinikom.github.io/pyside-docs/PySide/QtGui/QStandardItem.html

from PySide.QtGui import QStandardItemModel, QStandardItem

class Table(QStandardItemModel):
    """Represents the 'sand table'."""

    def __init__(self, rows, columns, parent=None):
        QStandardItemModel.__init__(self, rows, columns, parent)

        self.height = rows
        self.width = columns
        self.clear()

    def exists(self, row, column):
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
                if (int(self.item(i, j).text()) > 3):
                    cells.append([i, j])

                j += 1

            i += 1

        return cells

    def collapse(self, row, column):
        value = int(self.item(row, column).text())
        nb = int(value/4)
        remains = value%4

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
        i = 0

        while i < self.height:
            j = 0

            while j < self.width:
                self.setItem(i, j, QStandardItem('0'))

                j += 1

            i += 1

"""
    def get(self, x, y):
        if(self.exists(x, y)):
            row = self.table[y]

            return row[x]

        return 0

    def set(self, x, y, value):
        if(self.exists(x, y)):
            row = list(self.table[y])
            row[x] = value
            self.table[y] = list(row)
"""
