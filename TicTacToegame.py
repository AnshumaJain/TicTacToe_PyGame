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
RESTART_BG_COLOR = (255, 255, 255)   # WHITE
RESTART_FONT_COLOR_ACTIVE = (0, 128, 128) # TEAL
RESTART_FONT_COLOR_PASSIVE = (32, 178, 170)  # LIGHT SEA GREEN

# Display Pixel Area
SCREEN_SIZE = [300, 300]
RESTART_BUTTON_X_START = 0
RESTART_BUTTON_WIDTH = 300
RESTART_BUTTON_Y_START = 260
RESTART_BUTTON_HEIGHT = 40

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

# Maps X-Pixel Border to Cell No.
X_BORDER_TO_CELL_MAP = {
    (120, 60): {1, 4, 7},
    (180, 120): {2, 5, 8},
    (240, 180): {3, 6, 9}
}

# Maps Y-Pixel Border to Cell No.
Y_BORDER_TO_CELL_MAP = {
    (60, 120): {1, 2, 3},
    (120, 180): {4, 5, 6},
    (180, 240): {7, 8, 9}
}

# Cell combos needed to win
WINNING_CELL_COMBOS = {
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal combos
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical combos
    (0, 4, 8), (2, 4, 6),  # diagonal combos
}


class Gui:

    def __init__(self):
        pygame.init()

        # default font
        self.font = pygame.font.Font('freesansbold.ttf', 25)

        # Set up the drawing window
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        # Fill the background color
        self.screen.fill(BG_SCREEN_COLOR)

        # draw the labels and the grid
        self.static_drawing()


    def static_drawing(self):
        """ draw the labels, window name and the tic-tac-toe grid """

        pygame.display.set_caption('Welcome to Tic-Tac-Toe game')  # window name

        # Draw the tic-tac-toe hatched lines
        pygame.draw.line(self.screen, LINE_COLOR, (120, 60), (120, 240), 5)  # vertical line1
        pygame.draw.line(self.screen, LINE_COLOR, (180, 60), (180, 240), 5)  # vertical line2
        pygame.draw.line(self.screen, LINE_COLOR, (60, 120), (240, 120), 5)  # horizontal line1
        pygame.draw.line(self.screen, LINE_COLOR, (60, 180), (240, 180), 5)  # horizontal line2

        # initial turn text
        text1 = self.font.render(" O Turn ", True, O_COLOR, BG_SCREEN_COLOR)  # O label
        text_rect1 = text1.get_rect()
        text_rect1.center = (150, 25)
        self.screen.blit(text1, text_rect1)

        # restart button area
        pygame.draw.rect(self.screen, RESTART_BG_COLOR, [RESTART_BUTTON_X_START, RESTART_BUTTON_Y_START,
                                                         RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGHT])


    def display_symbol(self, symbol, cell_num):
        """ function to draw the 'X' and 'O' symbols in the given cell no."""

        x, y = CELL_CENTER_HASH_MAP[cell_num]
        if not self.is_game_over:

            # display the 'X' or 'O' symbol text
            if symbol == 'O':
                symbol_color = O_COLOR
            else:
                symbol_color = X_COLOR

            symbol_text = self.font.render(symbol, True, symbol_color)
            symbol_text_rect = symbol_text.get_rect()
            symbol_text_rect.center = (x, y)
            self.screen.blit(symbol_text, symbol_text_rect)

            # display the turn text
            if symbol == 'O':
                turn_text = self.font.render(' X Turn ', True, X_COLOR, BG_SCREEN_COLOR)  # X label
            else:
                turn_text = self.font.render(" O Turn ", True, O_COLOR, BG_SCREEN_COLOR)  # O label

            turn_text_rect = turn_text.get_rect()
            turn_text_rect.center = (150, 25)
            self.screen.blit(turn_text, turn_text_rect)

    def display_win_message(self, win_message, color):
        """ function to display the win message """

        text = self.font.render(win_message, True, color, BG_SCREEN_COLOR)  # O wins text
        text_rect = text.get_rect()
        text_rect.center = (150, 25)
        self.screen.blit(text, text_rect)


    def display_game_result(self, win, winning_cells=None):
        """ function to display the winning screen """

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
        Gui.__init__(self) # call the parent class constructor
        self.turn = 0  # variable to count the turns (1-9)
        self.is_game_over = False  # boolean to monitor if the game is over
        self.cell = [None] * 9  # cell array representing 9 cells of the tic-tac-toe grid


    def restart_game(self):
        self.turn = 0   # reset the turns
        self.is_game_over = False  # reset game over boolean
        self.cell = [None] * 9  # reinitialize the tic-tac-toe cell array
        super().__init__() # call parent class constructor to redraw the GUI


    def process_player_turn(self, cell_no):
        """ function to process the turn """
        if self.turn % 2 == 0:  # if the turn is even
            symbol = 'O'
        else:
            symbol = 'X'

        if not self.cell[cell_no - 1]: # if the clicked cell isn't already filled
            self.display_symbol(symbol, cell_no)
            self.turn += 1
            self.cell[cell_no - 1] = symbol


    def check_win(self):
        """ function to check if anyone has won yet of if there is a tie"""

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
        """ method to process any mouse clicks """

        # if clicked in the 'restart area'
        if RESTART_BUTTON_X_START <= pos[0] <= RESTART_BUTTON_X_START + RESTART_BUTTON_WIDTH and \
                RESTART_BUTTON_Y_START <= pos[1] <= RESTART_BUTTON_Y_START + RESTART_BUTTON_HEIGHT:
            self.restart_game()
        else: # check if user clicked on any of the tic-tac-toe cells
            possible_cells_x = set()    # to store horizontal cell no.
            possible_cells_y = set()    # to store vertical cell no.
            for x1, x2 in X_BORDER_TO_CELL_MAP.keys():
                if x1 > pos[0] > x2:
                    possible_cells_x = X_BORDER_TO_CELL_MAP[(x1, x2)]
            for y1, y2 in Y_BORDER_TO_CELL_MAP.keys():
                if y1 < pos[1] < y2:
                    possible_cells_y = Y_BORDER_TO_CELL_MAP[(y1, y2)]

            current_cell = possible_cells_x & possible_cells_y
            if current_cell:  # if the user didn't click outside the designated area
                self.process_player_turn(current_cell.pop())
                self.check_win() # check if anyone has one


    def start_game(self):
        """ entry point into the game after init"""

        while 1: # keep running until quit() is called
            pos = pygame.mouse.get_pos()  # get cursor position

            for event in pygame.event.get():    # process all events
                if event.type == pygame.MOUSEBUTTONUP:  # if mouse click event detected
                    self.process_mouse_click(pos)

                if event.type == pygame.QUIT:   # if the user closes the pygame window
                    pygame.quit()  # quitting pygame
                    quit()  # time to quit

            # check if the user hovers over the 'restart game' area
            restart_font = pygame.font.Font('freesansbold.ttf', 19)
            if RESTART_BUTTON_X_START <= pos[0] and RESTART_BUTTON_Y_START <= pos[1]:
                text = restart_font.render("Restart Game", True, RESTART_FONT_COLOR_ACTIVE)
            else:
                text = restart_font.render("Restart Game", True, RESTART_FONT_COLOR_PASSIVE)
            text_rect = text.get_rect()
            text_rect.center = (150, 280)
            self.screen.blit(text, text_rect) # draw the text on screen

            pygame.display.update() # update display


if __name__ == "__main__":
    game_obj = TicTacToe()
    game_obj.start_game()
