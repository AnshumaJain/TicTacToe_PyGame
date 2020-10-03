#!/usr/local/bin/python3
"""
Tic-tac-toe(ttt) game graphical user interface using pygame and class inheritance.
"""
import pygame

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PEACH = (255, 200, 150)
CHOCOLATE = (210, 105, 30)
BROWN = (165, 42, 42)

CELL_CENTER_HASH_MAP = {
    1: (90, 90),
    2: (150, 90),
    3: (210, 90),
    4: (90, 150),
    5: (150, 150),
    6: (210, 150),
    7: (90, 210),
    8: (150, 210),
    9: (210, 210)
}

X_BORDER_TO_CELL_MAP = {
    (120, 60): {1, 4, 7},
    (180, 120): {2, 5, 8},
    (240, 180): {3, 6, 9}
}

Y_BORDER_TO_CELL_MAP = {
    (60, 120): {1, 2, 3},
    (120, 180): {4, 5, 6},
    (180, 240): {7, 8, 9}
}

WINNING_CELL_COMBOS = {
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal combos
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical combos
    (0, 4, 8), (2, 4, 6),  # diagonal combos
}


class Gui:

    def __init__(self):
        pygame.init()

        # texts
        self.font = pygame.font.Font('freesansbold.ttf', 20)

        # Set up the drawing window
        self.screen = pygame.display.set_mode([300, 300])

        # Fill the background color
        self.screen.fill(PEACH)

        self.cell = [None] * 9  # cell array representing 9 cells of the ttt grid
        self.static_drawing()  # display the labels and the grid
        self.is_game_over = False   # Boolean to monitor if the game is over


    def static_drawing(self):
        """ display the labels, window name and the grid """

        pygame.display.set_caption('Welcome to Tic-Tac-Toe game')  # window name

        text1 = self.font.render('Player 1: O', True, CHOCOLATE)  # player 1 label
        text_rect1 = text1.get_rect()
        text_rect1.center = (55, 20)
        self.screen.blit(text1, text_rect1)

        text2 = self.font.render('Player 2: X', True, CHOCOLATE)  # player 2 label
        text_rect2 = text2.get_rect()
        text_rect2.center = (55, 50)
        self.screen.blit(text2, text_rect2)

        # Draw a solid vertical & horizontal lines in the center
        self.line1 = pygame.draw.line(self.screen, CHOCOLATE, (120, 60), (120, 240), 4)  # vertical line1
        self.line2 = pygame.draw.line(self.screen, CHOCOLATE, (180, 60), (180, 240), 4)  # vertical line2
        self.line3 = pygame.draw.line(self.screen, CHOCOLATE, (60, 120), (240, 120), 4)  # horizontal line1
        self.line4 = pygame.draw.line(self.screen, CHOCOLATE, (60, 180), (240, 180), 4)  # horizontal line2


    def display_symbol(self, symbol, cell_num):
        x, y = CELL_CENTER_HASH_MAP[cell_num]
        if not self.is_game_over:
            text = self.font.render(symbol, True, BROWN)
            text_rect = text.get_rect()
            text_rect.center = (x, y)
            self.screen.blit(text, text_rect)


    def display_win_message(self, win_message):
        text = self.font.render(win_message, True, BROWN, YELLOW)  # O wins text
        text_rect = text.get_rect()
        text_rect.center = (150, 270)
        self.screen.blit(text, text_rect)


    def display_game_result(self, win):
        if win == 1:
            self.display_win_message('Player 1 Wins !')
        elif win == 2:
            self.display_win_message('Player 2 Wins !')
        elif win == 3:
            self.display_win_message("It's a Tie !")


class TicTacToe(Gui):

    def __init__(self):
        Gui.__init__(self)
        self.count = 0      # variable to count the turns


    def cell_click_update(self, symbol , cell_no):
        if self.cell[cell_no - 1] is None:
            self.display_symbol(symbol, cell_no)
            self.count += 1
            self.cell[cell_no - 1] = symbol


    def check_player_turn(self, cell_no):
        if self.count % 2 == 0:
            self.cell_click_update('O', cell_no)
        else:
            self.cell_click_update('X', cell_no)


    def check_win(self):

        for i,j,k in WINNING_CELL_COMBOS:
            if [self.cell[i], self.cell[j], self.cell[k]] == ['O']*3:
                if not self.is_game_over:               # if the game is not over yet
                    self.display_game_result(1)         # display player 'O' win result
                    self.is_game_over = True
                    break
            elif [self.cell[i], self.cell[j], self.cell[k]] == ['X']*3:
                if not self.is_game_over:               # if the game is not over yet
                    self.display_game_result(2)         # display player 'X' win result
                    self.is_game_over = True
                    break

        if self.count == 9:                             # check if all 9 turns are over
            if not self.is_game_over:                   # if no one won the game yet
                self.display_game_result(3)             # display tie result
                self.is_game_over = True


    def get_click_pos(self):

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()  # if mouse is pressed get position of cursor ##

                    possible_cells_x = set()
                    possible_cells_y = set()
                    for x1,x2 in X_BORDER_TO_CELL_MAP.keys():
                        if x1 > pos[0] > x2:
                            possible_cells_x = X_BORDER_TO_CELL_MAP[(x1,x2)]

                    for y1,y2 in Y_BORDER_TO_CELL_MAP.keys():
                        if y1 < pos[1] < y2:
                            possible_cells_y = Y_BORDER_TO_CELL_MAP[(y1,y2)]

                    current_cell = possible_cells_x & possible_cells_y

                    if current_cell: # if the user didn't click outside the designated area
                        self.check_player_turn(current_cell.pop())
                        self.check_win()

                if event.type == pygame.QUIT:
                    pygame.quit()                                       # quitting pygame
                    quit()                                              # time to quit

            # Flip the display
            # pygame.display.flip()
            pygame.display.update()


object = TicTacToe()
object.get_click_pos()
