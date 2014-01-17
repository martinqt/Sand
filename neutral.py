# -*-coding:Utf-8 -*

import png, sys, time
from src.Table import Table
from PySide.QtGui import QStandardItem

zoom = 1
colors = list()
colors.append([5, 205, 0]*zoom)
colors.append([255, 240, 94]*zoom)
colors.append([249, 164, 0]*zoom)
colors.append([210, 59, 0]*zoom)

def createInitialTable(size):
    table = Table(size, size, 4)
    table.fill('6')

    return table

def collapseTable(table):
    t1 = time.clock()
    print('Start Table Collapse')
    sys.stdout.flush()

    table.collapseAll()

    t2 = time.clock()
    print('End Table Collapse '+str(t2-t1))
    sys.stdout.flush()

    return t2

def neutralTable(table, size, t2):
    neutral = Table(size, size, 4)
    i = 0

    while i < size:
        j = 0
        while j < size:
            neutral.setItem(i, j, QStandardItem(str(3+3-int(table.item(i, j).text()))))
            j += 1
        i += 1

    t3 = time.clock()
    print('End Neutral Generation '+str(t3-t2))
    sys.stdout.flush()

    return neutral

def generateImage(neutral, size, t4, t0):
    mat = list()
    i = 0

    while i < size:
        j = 0
        row = list()
        while j < size:
            row.append(colors[int(neutral.item(i, j).text())])
            j +=1
        merged = [item for sublist in row for item in sublist]
        for a in range(zoom):
            mat.append(merged)
        i += 1

    print('End Image Loop '+str(time.clock()-t4))
    sys.stdout.flush()

    if(size<10):
        f = open('pics/0'+str(size)+'.png', 'wb')
    else:
        f = open('pics/'+str(size)+'.png', 'wb')
    w = png.Writer(size*zoom, size*zoom)
    w.write(f, mat) 
    f.close()

    print('== Ellapsed Time: '+str(time.clock()-t0)+' ==')



#======   MAIN PART    =========================================
try:
    cont = sys.argv[1]
except IndexError:
    cont = ''

if cont == '--restore':
    print('== Restoring Previous Collapsing ==')

    print('Restore Initial Collapse?')
    ans = input()

    print('Table size:')
    size = int(input())

    if(ans=='y' or ans=='1'):
        print('Restoring From Initial')

        t0 = time.clock()
        table = Table(size, size, 4)
        table.readPickled()
        t2 = collapseTable(table)
        neutral = neutralTable(table, size, t2)
        t4 = collapseTable(neutral)
        generateImage(neutral, size, t4, t0)

    else:
        print('Restoring From Neutral')

        t0 = time.clock()
        neutral = Table(size, size, 4)
        neutral.readPickled()
        t4 = collapseTable(neutral)
        generateImage(neutral, size, t4, t0)
else:
    print('Table size:')
    size = int(input())

    t0 = time.clock()
    table = createInitialTable(size)
    t2 = collapseTable(table)
    neutral = neutralTable(table, size, t2)
    t4 = collapseTable(neutral)
    generateImage(neutral, size, t4, t0)
