# -*-coding:Utf-8 -*

import sys
from src.Table import Table

table = Table(3, 4)
print(table)

if(table.exists(1, 2) != True):
    print('Existing cell not recognized!!')

if(table.exists(7, 8) != False):
    print('Unexisting cell found :$')

if(table.exists(-2, -1) != False):
    print('Unexisting cell found :$')

table.set(1, 2, 3)
table.set(0, 2, 4)
table.set(3, 2, 2)
table.set(1, 1, 0)
table.set(2, 0, 4)

print(table)
print(table.collapsable())

print('\n \n')

while table.collapsable() != []:
    for point in table.collapsable():
        table.collapse(point[0], point[1])
        print(table)
