from settings import *
import pygame
import math


class Drawing:

    def __init__(self, sc):
        self.sc = sc
        self.myfont = pygame.font.SysFont("arial", 45)
        self.myfont1 = pygame.font.SysFont("arial", 20)

    def background(self):
        pygame.draw.rect(self.sc, WHITE, (0, 0, WIDTH, HEIGHT))

    def board(self):
        for i in range(ROOT_BOARD+1):
            pygame.draw.line(self.sc,
                             BLACK,
                             [BOARD_TOPLEFT_X+i*ROOT_BOARD*CELL_WIDTH, BOARD_TOPLEFT_Y],
                             [BOARD_TOPLEFT_X+i*ROOT_BOARD*CELL_WIDTH, BOARD_TOPLEFT_Y+BOARD_HEIGHT],
                             BOLD,
                            )
            pygame.draw.line(self.sc,
                             BLACK,
                             [BOARD_TOPLEFT_X, BOARD_TOPLEFT_Y+i*ROOT_BOARD*CELL_HEIGHT],
                             [BOARD_TOPLEFT_X+BOARD_WIDTH, BOARD_TOPLEFT_Y+i*ROOT_BOARD*CELL_HEIGHT],
                             BOLD,
                            )

        for j in range(1, LEN_BOARD):
            pygame.draw.line(self.sc,
                             BLACK,
                             [BOARD_TOPLEFT_X + j * CELL_WIDTH, BOARD_TOPLEFT_Y],
                             [BOARD_TOPLEFT_X + j * CELL_WIDTH, BOARD_TOPLEFT_Y + BOARD_HEIGHT],
                             )
            pygame.draw.line(self.sc,
                             BLACK,
                             [BOARD_TOPLEFT_X, BOARD_TOPLEFT_Y + j * CELL_HEIGHT],
                             [BOARD_TOPLEFT_X + BOARD_WIDTH, BOARD_TOPLEFT_Y + j * CELL_HEIGHT],
                             )

    def update_cells(self, board):
        puzzle = board.puzzle
        for row in puzzle:
            for cell in row:
                if cell.temp_cell_colour != WHITE and cell.cell_colour != PINK:
                    pygame.draw.rect(self.sc, cell.temp_cell_colour, cell.rect)
                elif cell.cell_colour == PINK and cell.value_colour == RED and cell.temp_cell_colour != WHITE:
                    pygame.draw.rect(self.sc, cell.temp_cell_colour, cell.rect)
                else:
                    pygame.draw.rect(self.sc, cell.cell_colour, cell.rect)

                if cell.value:
                    label = self.myfont.render(str(cell.value), True, cell.value_colour)
                    self.sc.blit(label, (cell.x+CELL_WIDTH//4, cell.y))

    def game_over(self):
        label = self.myfont.render("GAME OVER", True, RED)
        self.sc.blit(label, (BOARD_TOPLEFT_X+BOARD_WIDTH//4, BOARD_TOPLEFT_Y-50))

        label = self.myfont.render("Second chance", True, WHITE)
        pygame.draw.rect(self.sc, SKYBLUE,
                         (BOARD_TOPLEFT_X - BOARD_WIDTH//2-50, BOARD_TOPLEFT_Y + BOARD_HEIGHT // 2, 270, 50),)
        self.sc.blit(label, (BOARD_TOPLEFT_X-len("Second chance")*20, BOARD_TOPLEFT_Y+BOARD_HEIGHT//2))

        label = self.myfont.render("AGAIN", True, WHITE)
        pygame.draw.rect(self.sc, SKYBLUE,
                         (BOARD_TOPLEFT_X - BOARD_WIDTH // 2 - 50, BOARD_TOPLEFT_Y + BOARD_HEIGHT//2+60, 270, 50), )
        self.sc.blit(label, (BOARD_TOPLEFT_X - len("AGAIN") * 50, BOARD_TOPLEFT_Y + BOARD_HEIGHT//2+60))

        pygame.draw.rect(self.sc, DARKGRAY, (BOARD_TOPLEFT_X, BOARD_TOPLEFT_Y, BOARD_WIDTH, BOARD_HEIGHT))


    def update_solved_cells(self, board):
        puzzle = board.puzzle
        for row in puzzle:
            for cell in row:
                if cell.temp_cell_colour != WHITE and cell.cell_colour != PINK:
                    pygame.draw.rect(self.sc, cell.temp_cell_colour, cell.rect)
                elif cell.cell_colour == PINK and cell.value_colour == RED and cell.temp_cell_colour != WHITE:
                    pygame.draw.rect(self.sc, cell.temp_cell_colour, cell.rect)
                else:
                    pygame.draw.rect(self.sc, cell.cell_colour, cell.rect)

                if cell.value:
                    label = self.myfont1.render(str(cell.value), True, cell.value_colour)
                    self.sc.blit(label, (cell.x+CELL_WIDTH1//4, cell.y))

    def game_won(self):
        label = self.myfont.render("YOU WON", True, GREEN)
        self.sc.blit(label, (BOARD_TOPLEFT_X + BOARD_WIDTH // 4, BOARD_TOPLEFT_Y - 50))
        label = self.myfont.render("AGAIN", True, WHITE)
        pygame.draw.rect(self.sc, SKYBLUE,
                         (BOARD_TOPLEFT_X - BOARD_WIDTH // 2 - 50, BOARD_TOPLEFT_Y + BOARD_HEIGHT // 2 + 60, 270, 50), )
        self.sc.blit(label, (BOARD_TOPLEFT_X - len("AGAIN") * 50, BOARD_TOPLEFT_Y + BOARD_HEIGHT // 2 + 60))

    def puzzle_level(self):
        label = self.myfont.render("EASY", True, BLUE)
        pygame.draw.rect(self.sc, BLACK,
                         (1000, BOARD_TOPLEFT_Y, 270, 50), )
        self.sc.blit(label, (1000, BOARD_TOPLEFT_Y))

        label = self.myfont.render("MEDIUM", True, BLUE)
        pygame.draw.rect(self.sc, BLACK,
                         (1000, BOARD_TOPLEFT_Y+60, 270, 50), )
        self.sc.blit(label, (1000, BOARD_TOPLEFT_Y+60))

        label = self.myfont.render("HARD", True, BLUE)
        pygame.draw.rect(self.sc, BLACK,
                         (1000, BOARD_TOPLEFT_Y+120, 270, 50), )
        self.sc.blit(label, (1000, BOARD_TOPLEFT_Y+120))

        label = self.myfont.render("EXPERT", True, BLUE)
        pygame.draw.rect(self.sc, BLACK,
                         (1000, BOARD_TOPLEFT_Y+180, 270, 50), )
        self.sc.blit(label, (1000, BOARD_TOPLEFT_Y+180))

        label = self.myfont.render("EVIL", True, BLUE)
        pygame.draw.rect(self.sc, BLACK,
                         (1000, BOARD_TOPLEFT_Y+240, 270, 50), )
        self.sc.blit(label, (1000, BOARD_TOPLEFT_Y+240))
