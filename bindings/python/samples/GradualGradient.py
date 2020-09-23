from ArrayManipulator import ArrayManipulator

class GradualGradient(ArrayManipulator):
    def __init__(self, *args, **kwargs):
        super(GradualGradient, self).__init__(*args, **kwargs)
        self._array[0][0] == 0xffffff

        self.cur_x = 1
        self.cur_y = 0

    def reset_array(self):
        for row in self._array:
            for col in range(len(row)):
                row[col] = 0

        self._array[0][0] == 0xffffff

    def process_frame(self):
        greater_than_zero = False
        y = self.cur_y
        x = self.cur_x
        advance_x = False
        if y == 0:
            prev = self._array[y][x-1]
            if self._array[y][x] > prev - ((0xff//(NUM_COLS*CHAIN_LEN))<<16):
                self._array[y][x] -= 0x10000
            else:
                advance_x = True
        elif y < NUM_ROWS:
            prev = self._array[y-1][x]
            if self._array[y][x] > prev - ((0xff//NUM_ROWS)<<8):
                self._array[y][x] -= 0x100
            else:
                self.cur_y += 1
        else:
            self.reset_array()

        if advance_x:
            self.cur_x += 1
            if self.cur_x == NUM_COLS * CHAIN_LEN:
                self.cur_x = 0
                self.cur_y += 1


    return True