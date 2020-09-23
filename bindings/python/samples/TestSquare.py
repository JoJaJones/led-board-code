from ArrayManipulator import ArrayManipulator
from random import randint
from constants import *

class TestSquare(ArrayManipulator):
    def __init__(self):
        self._array = []
        for r in range(NUM_ROWS):
            self._array.append([])
            for _ in range(NUM_COLS*CHAIN_LEN):
                self._array[r].append(randint(0x888888, 0xFFFFFF))

    def get_canvas(self):
        return self._array

    def process_frame(self):
        greater_than_zero = False
        for row in self._array:
            for col in range(len(row)):
                r = (row[col]&0xff0000)>>16
                g = (row[col]&0xff00)>>8
                b = row[col]&0xff
                #if row == self._array[0] and col == 0:
                 #   print(r,g,b, row[col])
                which = randint(0,2)
                if which == 0:
                    r = randint(r//2, r)
                elif which == 1:
                    g = randint(g//2, g)
                else:
                    b = randint(b//2, b)

                r<<=16
                g<<=8
                row[col] = r + g + b
                #if row == self._array[0] and col == 0:
                 #   print(r,g,b, row[col])

                if row[col] > 0:
                    greater_than_zero = True

        return greater_than_zero
