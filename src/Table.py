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


class Table:
    """Represents the 'sand table'."""

    def __init__(self, height, width):
        self.table = []
        self.height = height
        self.width = width

        row = []
        
        i = 0
        while i < width:
            row.append(0)
            i += 1

        i = 0
        while i < height:
            self.table.append(row)
            i += 1

    def __str__(self):
        return self.table.__str__()

    def exists(self, x, y):
        if ((x >= self.width or not x >= 0) or (y >= self.height or not y >= 0)):
            return False

        return True

    def get(self, x, y):
        row = self.table[y]

        return row[x]

    def set(self, x, y, value):
        row = list(self.table[y])
        row[x] = value
        self.table[y] = list(row)

    def collapsable(self):
        i = 0

        while i < self.height:
            j = 0

            row = list(self.table[i])

            while j < self.width:
                if (row[j] > 3):
                    return [j, i]

                j += 1

            i += 1

    def collapse(self, x, y):

