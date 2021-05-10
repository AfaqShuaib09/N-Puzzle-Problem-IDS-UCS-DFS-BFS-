import math as m


class Puzzle_board:
    def __init__(self, ls_tiles, path=None, zero_position=None):
        if path is None:
            self.path = ''
        else:
            self.path = path
        self.zero_position = zero_position
        self.board = []
        self.dimension = int(m.sqrt(len(ls_tiles)))
        for i in range(self.dimension):
            self.board.append(list())
        for i in range(len(ls_tiles)):
            self.board[int(i / self.dimension)].append(ls_tiles[i])
            if ls_tiles[i] == '0':
                self.zero_position = [int(i / self.dimension), i % self.dimension]

    def get_zero_position(self):
        return self.zero_position

    def print_board(self):
        for row in self.board:
            print(row)
        print('\n')

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __eq__(self, other):
        return True

    def move_left(self):
        if self.zero_position[1] == 0:
            return
        else:
            zp = self.zero_position
            self.board[zp[0]][zp[1]], self.board[zp[0]][zp[1] - 1] = self.board[zp[0]][zp[1] - 1], self.board[zp[0]][
                zp[1]]
            self.zero_position[1] = self.zero_position[1] - 1
            self.path = self.path + 'L'

    def move_right(self):
        if self.zero_position[1] == self.dimension-1:
            return
        else:
            zp = self.zero_position
            self.board[zp[0]][zp[1]], self.board[zp[0]][zp[1] + 1] = self.board[zp[0]][zp[1] + 1], self.board[zp[0]][
                zp[1]]
            self.zero_position[1] = self.zero_position[1] + 1
            self.path = self.path + 'R'

    def move_up(self):
        if self.zero_position[0] == 0:
            return
        else:
            zp = self.zero_position
            self.board[zp[0]][zp[1]], self.board[zp[0] - 1][zp[1]] = self.board[zp[0] - 1][zp[1]], self.board[zp[0]][zp[1]]
            self.zero_position[0] = self.zero_position[0] - 1
            self.path = self.path + 'U'

    def move_down(self):
        if self.zero_position[0] == self.dimension-1:
            return
        else:
            zp = self.zero_position
            self.board[zp[0]][zp[1]], self.board[zp[0] + 1][zp[1]] = self.board[zp[0] + 1][zp[1]], self.board[zp[0]][
                zp[1]]
            self.zero_position[0] = self.zero_position[0] + 1
            self.path = self.path + 'D'

    def is_boards_equal(self, temp_board):    # returns true when both when passing board is equal to calling board
        flag = True
        for row1, row2 in zip(self.board, temp_board):
            for val1, val2 in zip(row1, row2):
                if val1 != val2:
                    flag = False
                    return flag
        return flag
