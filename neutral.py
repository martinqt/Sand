# -*-coding:Utf-8 -*

import png, sys, time
from src.Table import Table
from PySide.QtGui import QStandardItem

print('Table size:')
size = int(input())

zoom = 1

colors = list()
colors.append([5, 205, 0]*zoom)
colors.append([255, 240, 94]*zoom)
colors.append([249, 164, 0]*zoom)
colors.append([210, 59, 0]*zoom)


table = Table(size, size, 4)
table.fill('6')

t1 = time.clock()
print('Start Initial Collapse')
sys.stdout.flush()

table.collapseAll()

t2 = time.clock()
print('End Initial Collapse '+str(t2-t1))
sys.stdout.flush()

neutral = Table(size, size, 4)

i = 0

while i < size:
    j = 0
    while j < size:
        neutral.setItem(i, j, QStandardItem(str(3+3-int(table.item(i, j).text()))))
        j += 1
    i += 1

i = j = 0

t3 = time.clock()
print('End Neutral Generation '+str(t3-t2))
sys.stdout.flush()

neutral.collapseAll()

t4 = time.clock()
print('End Neutral Collapse '+str(t4-t3))
sys.stdout.flush()

mat = list()

while i < size:
    row = list()
    while j < size:
        row.append(colors[int(neutral.item(i, j).text())])
        j +=1
    merged = [item for sublist in row for item in sublist]
    for a in range(zoom):
        mat.append(merged)
    j = 0
    i += 1

print('End Image Loop '+str(time.clock()-t4))
sys.stdout.flush()

f = open('pics/'+str(size)+'.png', 'wb')
w = png.Writer(size*zoom, size*zoom)
w.write(f, mat) 
f.close()

print('== Ellapsed Time: '+str(time.clock()-t1)+' ==')
