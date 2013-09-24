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
