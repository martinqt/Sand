# -*-coding:Utf-8 -*

import png, sys, itertools, time
from src.Table import Table

list2d = [[1,2,3],[4,5,6], [7], [8,9]]
merged = list(itertools.chain.from_iterable(list2d))

zoom = 1

colors = list()
colors.append([5, 205, 0]*zoom)
colors.append([255, 240, 94]*zoom)
colors.append([249, 164, 0]*zoom)
colors.append([210, 59, 0]*zoom)

size = 20

table = Table(size, size, 4)
table.fill('6')

t1 = time.clock()
print('Start Collapse')
sys.stdout.flush()

table.collapseAll()

t2 = time.clock()
print('End Collapse '+str(t2-t1))
sys.stdout.flush()

i = j = 0

mat = list()

while i < size:
    row = list()
    while j < size:
        row.append(colors[int(table.item(i, j).text())])
        j +=1
    merged = [item for sublist in row for item in sublist]
    for a in range(zoom):
        mat.append(merged)
    j = 0
    i += 1

print('End Loop '+str(time.clock()-t2))
sys.stdout.flush()

f = open('pics/a.png', 'wb')
w = png.Writer(size*zoom, size*zoom)
w.write(f, mat) 
f.close()
