from settings import *


class Logic:
    def __init__(self):
        self.wrong_number_count = 0

    def is_right_value(self, x, y, cell):
        for row in cell.board.puzzle:
            for cell in row:
                if cell.value_colour == RED:
                    cell.value_colour = BLACK

        for i in range(LEN_BOARD):
            if cell.board.puzzle[x][y].value == cell.board.puzzle[x][i].value and i != y:
                cell.board.puzzle[x][i].cell_colour = PINK
                cell.board.puzzle[x][y].value_colour = RED

            if cell.board.puzzle[x][y].value == cell.board.puzzle[i][y].value and i != x:
                cell.board.puzzle[i][y].cell_colour = PINK
                cell.board.puzzle[x][y].value_colour = RED

        for j in range(x//ROOT_BOARD*ROOT_BOARD, x//ROOT_BOARD*ROOT_BOARD+ROOT_BOARD):
            for k in range(y//ROOT_BOARD*ROOT_BOARD, y//ROOT_BOARD*ROOT_BOARD+ROOT_BOARD):
                if cell.board.puzzle[x][y].value == cell.board.puzzle[j][k].value and j != x and k != y:
                    cell.board.puzzle[j][k].cell_colour = PINK
                    cell.board.puzzle[x][y].value_colour = RED

        if cell.board.puzzle[x][y].value_colour != RED and SOLVED_BOARD[x][y] == cell.board.puzzle[x][y].value:
            cell.board.puzzle[x][y].value_colour = BLUE
            cell.board.puzzle[x][y].cell_colour = WHITE
        else:
            cell.board.puzzle[x][y].cell_colour = PINK
            self.wrong_number_count += 1

    def is_game_over(self):
        if self.wrong_number_count >= 3:
            return True

    def is_game_won(self, board):
        for i in range(LEN_BOARD):
            for j in range(LEN_BOARD):
                if board.puzzle[i][j].value != SOLVED_BOARD[i][j]:
                    return False
        return True
