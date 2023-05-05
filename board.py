from pygame.locals import *
from cell import Cell
from settings import *


class Board:
    puzzle = []

    def __init__(self, initialPuzzle):
        for i, row in enumerate(initialPuzzle):
            _row = []
            for j, value in enumerate(row):
                cell = Cell(value, value != 0, self)
                _x = BOARD_TOPLEFT_X + i*CELL_WIDTH
                _y = BOARD_TOPLEFT_Y + j*CELL_HEIGHT
                cell.rect = Rect(_x+2, _y+2, CELL_WIDTH-2, CELL_HEIGHT-2)
                cell.x = _x
                cell.y = _y
                _row.append(cell)
            self.puzzle.append(_row)

    @classmethod
    def marked_cell(cls, x, y):
        for row in cls.puzzle:
            for cell in row:
                cell.temp_cell_colour = WHITE
                if cell.value_colour == RED:
                    cell.temp_cell_colour = WHITE

        for i, row in enumerate(cls.puzzle):
            for j, cell in enumerate(row):
                if cell.x < x < (cell.x+CELL_WIDTH) and cell.y < y < (cell.y+CELL_HEIGHT):
                    for k in range(LEN_BOARD):
                        if k != j and cls.puzzle[i][k].value_colour != RED:
                            cls.puzzle[i][k].temp_cell_colour = CERULEAN
                        if k != i and cls.puzzle[k][j].value_colour != RED:
                            cls.puzzle[k][j].temp_cell_colour = CERULEAN
                        cell.temp_cell_colour = POWDERBLUE
                        if cell.value:
                            for row1 in cls.puzzle:
                                for cell1 in row1:
                                    if cell1.value == cell.value:
                                        cell1.temp_cell_colour = POWDERBLUE

                    for l in range(i//ROOT_BOARD*ROOT_BOARD, i//ROOT_BOARD*ROOT_BOARD+ROOT_BOARD):
                        for m in range(j//ROOT_BOARD*ROOT_BOARD, j//ROOT_BOARD*ROOT_BOARD+ROOT_BOARD):
                            if (l != i and m != j) and cls.puzzle[l][m].cell_colour != PINK:
                                cls.puzzle[l][m].temp_cell_colour = CERULEAN




class Board1:
    puzzle = []

    def __init__(self, initialPuzzle):
        for i, row in enumerate(initialPuzzle):
            _row = []
            for j, value in enumerate(row):
                cell = Cell(value, value != 0, self)
                _x = BOARD1_TOPLEFT_X + i*CELL_WIDTH1
                _y = BOARD1_TOPLEFT_Y + j*CELL_HEIGHT1
                cell.rect = Rect(_x+2, _y+2, CELL_WIDTH1-2, CELL_HEIGHT1-2)
                cell.x = _x
                cell.y = _y
                _row.append(cell)
            self.puzzle.append(_row)

