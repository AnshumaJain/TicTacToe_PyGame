#!/usr/local/bin/python3
"""
Tic-tac-toe(ttt) game graphical user interface using pygame and class inheritance.
"""
import pygame

# Colors
BG_SCREEN_COLOR = (32, 178, 170)  # LIGHT SEA GREEN
O_COLOR = (255, 255, 255)  # WHITE
X_COLOR = (0, 0, 0)  # BLACK
OX_DRAW_COLOR = (105, 105, 105)  # GRAY
LINE_COLOR = (0, 128, 128)  # TEAL

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
        self.font = pygame.font.Font('freesansbold.ttf', 25)

        # Set up the drawing window
        self.screen = pygame.display.set_mode([300, 300])

        # Fill the background color
        self.screen.fill(BG_SCREEN_COLOR)

        self.cell = [None] * 9  # cell array representing 9 cells of the ttt grid
        self.static_drawing()  # display the labels and the grid
        self.is_game_over = False  # Boolean to monitor if the game is over


    def static_drawing(self):
        """ display the labels, window name and the grid """

        pygame.display.set_caption('Welcome to Tic-Tac-Toe game')  # window name

        # Draw a solid vertical & horizontal lines in the center
        pygame.draw.line(self.screen, LINE_COLOR, (120, 60), (120, 240), 5)  # vertical line1
        pygame.draw.line(self.screen, LINE_COLOR, (180, 60), (180, 240), 5)  # vertical line2
        pygame.draw.line(self.screen, LINE_COLOR, (60, 120), (240, 120), 5)  # horizontal line1
        pygame.draw.line(self.screen, LINE_COLOR, (60, 180), (240, 180), 5)  # horizontal line2

        # start turn instruction
        text1 = self.font.render(" O Turn ", True, O_COLOR, BG_SCREEN_COLOR)  # O label
        text_rect1 = text1.get_rect()
        text_rect1.center = (150, 25)
        self.screen.blit(text1, text_rect1)


    def display_symbol(self, symbol, cell_num, color):
        x, y = CELL_CENTER_HASH_MAP[cell_num]
        if not self.is_game_over:
            text = self.font.render(symbol, True, color)
            text_rect = text.get_rect()
            text_rect.center = (x, y)
            self.screen.blit(text, text_rect)

            if symbol == 'O':
                text2 = self.font.render(' X Turn ', True, X_COLOR, BG_SCREEN_COLOR)  # X label
                text_rect2 = text2.get_rect()
                text_rect2.center = (150, 25)
                self.screen.blit(text2, text_rect2)
            else:
                text1 = self.font.render(" O Turn ", True, O_COLOR, BG_SCREEN_COLOR)  # O label
                text_rect1 = text1.get_rect()
                text_rect1.center = (150, 25)
                self.screen.blit(text1, text_rect1)


    def display_win_message(self, win_message, color):
        text = self.font.render(win_message, True, color, BG_SCREEN_COLOR)  # O wins text
        text_rect = text.get_rect()
        text_rect.center = (150, 25)
        self.screen.blit(text, text_rect)


    def display_game_result(self, win, winning_cells=None):
        if win == 1:
            cord1 = CELL_CENTER_HASH_MAP[winning_cells[0] + 1]
            cord2 = CELL_CENTER_HASH_MAP[winning_cells[1] + 1]
            cord3 = CELL_CENTER_HASH_MAP[winning_cells[2] + 1]
            self.display_win_message('O Wins!', O_COLOR)
            pygame.draw.line(self.screen, O_COLOR, cord1, cord2, 3)
            pygame.draw.line(self.screen, O_COLOR, cord2, cord3, 3)
        elif win == 2:
            cord1 = CELL_CENTER_HASH_MAP[winning_cells[0] + 1]
            cord2 = CELL_CENTER_HASH_MAP[winning_cells[1] + 1]
            cord3 = CELL_CENTER_HASH_MAP[winning_cells[2] + 1]
            self.display_win_message('X Wins!', X_COLOR)
            pygame.draw.line(self.screen, X_COLOR, cord1, cord2, 3)
            pygame.draw.line(self.screen, X_COLOR, cord2, cord3, 3)

        elif win == 3:
            self.display_win_message("X-O Draw!", OX_DRAW_COLOR)


class TicTacToe(Gui):

    def __init__(self):
        Gui.__init__(self)
        self.turn = 0  # variable to turn the turns


    def cell_click_update(self, symbol, cell_no, color):
        if self.cell[cell_no - 1] is None:
            self.display_symbol(symbol, cell_no, color)
            self.turn += 1
            self.cell[cell_no - 1] = symbol


    def check_player_turn(self, cell_no):
        if self.turn % 2 == 0:
            self.cell_click_update('O', cell_no, O_COLOR)
        else:
            self.cell_click_update('X', cell_no, X_COLOR)


    def check_win(self):

        for i, j, k in WINNING_CELL_COMBOS:
            if [self.cell[i], self.cell[j], self.cell[k]] == ['O'] * 3:
                if not self.is_game_over:  # if the game is not over yet
                    self.display_game_result(1, (i, j, k))  # display player 'O' win result
                    self.is_game_over = True
                    break
            elif [self.cell[i], self.cell[j], self.cell[k]] == ['X'] * 3:
                if not self.is_game_over:  # if the game is not over yet
                    self.display_game_result(2, (i, j, k))  # display player 'X' win result
                    self.is_game_over = True
                    break

        if self.turn == 9:  # check if all 9 turns are over
            if not self.is_game_over:  # if no one won the game yet
                self.display_game_result(3)  # display tie result
                self.is_game_over = True


    def process_mouse_click(self, pos):
        possible_cells_x = set()
        possible_cells_y = set()
        for x1, x2 in X_BORDER_TO_CELL_MAP.keys():
            if x1 > pos[0] > x2:
                possible_cells_x = X_BORDER_TO_CELL_MAP[(x1, x2)]
        for y1, y2 in Y_BORDER_TO_CELL_MAP.keys():
            if y1 < pos[1] < y2:
                possible_cells_y = Y_BORDER_TO_CELL_MAP[(y1, y2)]
        current_cell = possible_cells_x & possible_cells_y
        if current_cell:  # if the user didn't click outside the designated area
            self.check_player_turn(current_cell.pop())
            self.check_win()


    def get_click_pos(self):

        while 1:

            pos = pygame.mouse.get_pos()  # if mouse is pressed get position of cursor

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.process_mouse_click(pos)

                if event.type == pygame.QUIT:
                    pygame.quit()  # quitting pygame
                    quit()  # time to quit


            pygame.display.update()


ob = TicTacToe()
ob.get_click_pos()
