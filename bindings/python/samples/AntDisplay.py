from Ant.constants import *
from Ant.Display import LEDDisplay
from Ant.Ant import Ant
from Ant.Board import Board

class AntDisplay(ArrayManipulator):
    def __init__(self):
        super(AntDisplay, self).__init__()
        self.test_board = Board()
        self.test_board.add_ant(Ant(pos=(16, 16), direction=UP))
        self.displayObj = LEDDisplay(self.test_board.get_positions())

    def process_frame(self):
        for r in enumerate(self.displayObj.render(self.test_board.get_positions())):
            for c, col in enumerate(row):
                self._array[r][c] = col
        self.test_board.move_all_ants()

