#!/usr/local/bin/python3
"""
Tic-tac-toe(ttt) game graphical user interface using pygame and class inheritance.
"""
import pygame

# Colors
BG_SCREEN_COLOR = (32, 178, 170)                # LIGHT SEA GREEN
O_COLOR = (255, 255, 255)                       # WHITE
X_COLOR = (0, 0, 0)                             # BLACK
OX_DRAW_COLOR = (105, 105, 105)                 # GRAY
LINE_COLOR = (0, 128, 128)                      # TEAL
RESTART_BG_COLOR = (255, 255, 255)              # WHITE
RESTART_FONT_COLOR_ACTIVE = (0, 128, 128)       # TEAL
RESTART_FONT_COLOR_PASSIVE = (32, 178, 170)     # LIGHT SEA GREEN

# Display Pixel Area
SCREEN_SIZE = [300, 300]
RESTART_BUTTON_X_START = 0
RESTART_BUTTON_WIDTH = 300
RESTART_BUTTON_Y_START = 260
RESTART_BUTTON_HEIGHT = 40

# Maps cell no. to its center coordinates
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

# Maps column pixel border to Cell No.
X_BORDER_TO_CELL_MAP = {
    (120, 60): {1, 4, 7},               # cells in 1st col
    (180, 120): {2, 5, 8},              # cells in 2nd col
    (240, 180): {3, 6, 9}               # cells in 3rd col
}

# Maps row pixel border to Cell No.
Y_BORDER_TO_CELL_MAP = {
    (60, 120): {1, 2, 3},               # cells in 1st row
    (120, 180): {4, 5, 6},              # cells in 2nd row
    (180, 240): {7, 8, 9}               # cells in 3rd row
}

# Cell combos needed to win
WINNING_CELL_COMBOS = {
    (0, 1, 2), (3, 4, 5), (6, 7, 8),    # horizontal combos
    (0, 3, 6), (1, 4, 7), (2, 5, 8),    # vertical combos
    (0, 4, 8), (2, 4, 6),               # diagonal combos
}


class Gui:

    def __init__(self):
        pygame.init()                                           # initialize all imported pygame modules
        self.font = pygame.font.Font('freesansbold.ttf', 25)    # default font
        self.screen = pygame.display.set_mode(SCREEN_SIZE)      # set up the drawing window
        self.screen.fill(BG_SCREEN_COLOR)                       # fill the background color
        self.draw_initial_grid_and_labels()                     # draw all the initial labels and the grid

    def draw_initial_grid_and_labels(self):
        """ set window title; draw the labels and the tic-tac-toe grid """

        pygame.display.set_caption('Welcome to Tic-Tac-Toe game')                   # set pygame window title

        # Draw the tic-tac-toe hatched lines
        pygame.draw.line(self.screen, LINE_COLOR, (120, 60), (120, 240), 5)         # vertical line1
        pygame.draw.line(self.screen, LINE_COLOR, (180, 60), (180, 240), 5)         # vertical line2
        pygame.draw.line(self.screen, LINE_COLOR, (60, 120), (240, 120), 5)         # horizontal line1
        pygame.draw.line(self.screen, LINE_COLOR, (60, 180), (240, 180), 5)         # horizontal line2

        # display the initial turn text
        turn_text = self.font.render(" O Turn ", True, O_COLOR, BG_SCREEN_COLOR)    # label for initial turn
        turn_text_rect = turn_text.get_rect()
        turn_text_rect.center = (150, 25)
        self.screen.blit(turn_text, turn_text_rect)

        # restart button area
        pygame.draw.rect(self.screen, RESTART_BG_COLOR, [RESTART_BUTTON_X_START, RESTART_BUTTON_Y_START,
                                                         RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGHT])

    def display_symbol(self, symbol, cell_num):
        """ function to draw the 'X' and 'O' symbols in the given cell no."""
        if not self.is_game_over:                                           # if the game isn't over yet
            if symbol == 'O':
                symbol_color = O_COLOR
                turn_text = self.font.render(' X Turn ', True,
                                             X_COLOR, BG_SCREEN_COLOR)      # display the next turn
            else:
                symbol_color = X_COLOR
                turn_text = self.font.render(" O Turn ", True,
                                             O_COLOR, BG_SCREEN_COLOR)      # display the next turn

            x, y = CELL_CENTER_HASH_MAP[cell_num]  # get center coordinates of the given cell no.

            # draw the 'X' or 'O' symbol on the grid
            symbol_text = self.font.render(symbol, True, symbol_color)
            symbol_text_rect = symbol_text.get_rect()
            symbol_text_rect.center = (x, y)
            self.screen.blit(symbol_text, symbol_text_rect)

            # display the text for next turn
            turn_text_rect = turn_text.get_rect()
            turn_text_rect.center = (150, 25)
            self.screen.blit(turn_text, turn_text_rect)

    def display_win_message(self, win_message, color):
        """ function to display the win message """
        win_text = self.font.render(win_message, True, color, BG_SCREEN_COLOR)
        win_text_rect = win_text.get_rect()
        win_text_rect.center = (150, 25)
        self.screen.blit(win_text, win_text_rect)

    def display_game_result(self, win_symbol, winning_cells=None):
        """ function to display the winning screen """
        if win_symbol == 'XO':                                      # if there is a tie
            self.display_win_message("X-O Draw!", OX_DRAW_COLOR)
        else:
            if win_symbol == 'O':                                   # if 'O' has won
                color = O_COLOR
                win_message = 'O Wins!'
            elif win_symbol == 'X':                                 # if 'X' has won
                color = X_COLOR
                win_message = 'X Wins!'

            self.display_win_message(win_message, color)
            cord_start = CELL_CENTER_HASH_MAP[winning_cells[0] + 1]
            cord_end = CELL_CENTER_HASH_MAP[winning_cells[2] + 1]
            pygame.draw.line(self.screen, color, cord_start, cord_end, 3)


class TicTacToe(Gui):                               # inherited from Gui class

    def __init__(self):
        Gui.__init__(self)                          # call the parent class constructor
        self.turn = 0                               # variable to count the turns (1-9)
        self.is_game_over = False                   # boolean to monitor if the game is over
        self.cell = [None] * 9                      # cell array representing 9 cells of the tic-tac-toe grid

    def restart_game(self):
        self.turn = 0                               # reset the turns
        self.is_game_over = False                   # reset game_over boolean
        self.cell = [None] * 9                      # reinitialize the tic-tac-toe cell array
        super().__init__()                          # call parent class constructor to redraw the GUI

    def process_player_turn(self, cell_no):
        """ function to process the turn """
        if self.turn % 2 == 0:                      # if the turn is even
            symbol = 'O'
        else:
            symbol = 'X'

        if not self.cell[cell_no - 1]:              # if the clicked cell isn't already filled
            self.display_symbol(symbol, cell_no)
            self.turn += 1
            self.cell[cell_no - 1] = symbol

    def check_win(self):
        """ function to check if anyone has won yet or if there is a tie"""
        for i, j, k in WINNING_CELL_COMBOS:                                 # loop thru the valid winning cell combos
            if [self.cell[i], self.cell[j], self.cell[k]] == ['O'] * 3:     # if winning combo found for 'O'
                if not self.is_game_over:                                   # if the game is not over yet
                    self.display_game_result('O', (i, j, k))                # display the 'O' win result
                    self.is_game_over = True                                # declare game_over
                    break
            elif [self.cell[i], self.cell[j], self.cell[k]] == ['X'] * 3:   # if winning combo found for 'X'
                if not self.is_game_over:                                   # if the game is not over yet
                    self.display_game_result('X', (i, j, k))                # display the 'X' win result
                    self.is_game_over = True                                # declare game_over
                    break

        if self.turn == 9:                                                  # check if all 9 turns are over
            if not self.is_game_over:                                       # if no one won the game yet
                self.display_game_result('XO')                              # display the tie result
                self.is_game_over = True                                    # declare game_over

    def process_mouse_click(self, pos):
        """ method to process any mouse clicks """

        # if clicked in the 'restart area'
        if RESTART_BUTTON_X_START <= pos[0] <= RESTART_BUTTON_X_START + RESTART_BUTTON_WIDTH and \
                RESTART_BUTTON_Y_START <= pos[1] <= RESTART_BUTTON_Y_START + RESTART_BUTTON_HEIGHT:
            self.restart_game()                                         # reset the game
        else:                                                           # check if user clicked on any of the tic-tac-toe cells
            possible_cells_x = set()                                    # variable to store column cell no.
            possible_cells_y = set()                                    # variable to store row cell no.
            for x1, x2 in X_BORDER_TO_CELL_MAP.keys():                  # loop thru valid column pixed borders
                if x1 > pos[0] > x2:
                    possible_cells_x = X_BORDER_TO_CELL_MAP[(x1, x2)]
            for y1, y2 in Y_BORDER_TO_CELL_MAP.keys():                  # loop thru valid row pixed borders
                if y1 < pos[1] < y2:
                    possible_cells_y = Y_BORDER_TO_CELL_MAP[(y1, y2)]

            current_cell = possible_cells_x & possible_cells_y          # current cell will be the intersecting cell
            if current_cell:                                            # if the user didn't click outside the designated area
                self.process_player_turn(current_cell.pop())            # process the current turn
                self.check_win()                                        # check if anyone has won

    def start_game(self):
        """ entry point into the game after init"""
        while 1:                                                        # keep the game running until quit() is invoked
            pos = pygame.mouse.get_pos()                                # get current cursor position

            for event in pygame.event.get():                            # process all queued events
                if event.type == pygame.MOUSEBUTTONUP:                  # if mouse click event detected
                    self.process_mouse_click(pos)

                if event.type == pygame.QUIT:                           # if the user closes the pygame window
                    pygame.quit()                                       # quitting pygame
                    quit()                                              # built-in quit

            # check if the user hovers over the 'restart game' area
            restart_font = pygame.font.Font('freesansbold.ttf', 19)
            if RESTART_BUTTON_X_START <= pos[0] and RESTART_BUTTON_Y_START <= pos[1]:
                text = restart_font.render("Restart Game", True, RESTART_FONT_COLOR_ACTIVE)
            else:
                text = restart_font.render("Restart Game", True, RESTART_FONT_COLOR_PASSIVE)
            text_rect = text.get_rect()
            text_rect.center = (150, 280)
            self.screen.blit(text, text_rect)                           # redraw the text on screen

            pygame.display.update()                                     # update display


if __name__ == "__main__":
    game_obj = TicTacToe()
    game_obj.start_game()
