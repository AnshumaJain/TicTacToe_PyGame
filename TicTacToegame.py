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
        self.game_over = 0

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

        if cell_num == 1:
            x, y = 90, 90

        elif cell_num == 2:
            x, y = 150, 90

        elif cell_num == 3:
            x, y = 210, 90

        elif cell_num == 4:
            x, y = 90, 150

        elif cell_num == 5:
            x, y = 150, 150

        elif cell_num == 6:
            x, y = 210, 150

        elif cell_num == 7:
            x, y = 90, 210

        elif cell_num == 8:
            x, y = 150, 210

        elif cell_num == 9:
            x, y = 210, 210

        if self.game_over == 0:
            # for  O
            if symbol == 'O':
                text3 = self.font.render('O', True, BROWN)  # O
                text_rect3 = text3.get_rect()
                text_rect3.center = (x, y)
                self.screen.blit(text3, text_rect3)

            # for  X
            elif symbol == 'X':
                text4 = self.font.render('X', True, BROWN)  # X
                text_rect4 = text4.get_rect()
                text_rect4.center = (x, y)
                self.screen.blit(text4, text_rect4)

    def display_result(self, win):

        if win == 1:
            text5 = self.font.render('Player 1 Wins !', True, BROWN, YELLOW)  # O wins text
            text_rect5 = text5.get_rect()
            text_rect5.center = (150, 270)
            self.screen.blit(text5, text_rect5)

        elif win == 2:
            text6 = self.font.render('Player 2 Wins !', True, BROWN, YELLOW)  # x wins text
            text_rect6 = text6.get_rect()
            text_rect6.center = (150, 270)
            self.screen.blit(text6, text_rect6)

        elif win == 3:
            text7 = self.font.render("It's a Tie !", True, BROWN, YELLOW)  # tie text
            text_rect7 = text7.get_rect()
            text_rect7.center = (150, 270)
            self.screen.blit(text7, text_rect7)


class TicTacToe(Gui):

    def __init__(self):
        # initializing vars for win function
        Gui.__init__(self)
        self.self.count = 0


        # create an array for cells

    # self.counter that keeps track of the current cell
    # conditions for each cell index

    def check_win(self):

        if ([self.cell[0], self.cell[1], self.cell[2]] == ['O'] * 3 or
                [self.cell[3], self.cell[4], self.cell[5]] == ['O'] * 3 or
                [self.cell[6], self.cell[7], self.cell[8]] == ['O'] * 3 or
                [self.cell[0], self.cell[3], self.cell[6]] == ['O'] * 3 or
                [self.cell[1], self.cell[4], self.cell[7]] == ['O'] * 3 or
                [self.cell[2], self.cell[5], self.cell[8]] == ['O'] * 3 or
                [self.cell[0], self.cell[4], self.cell[8]] == ['O'] * 3 or
                [self.cell[2], self.cell[4], self.cell[6]] == ['O'] * 3):

            if self.game_over == 0:
                self.display_result(1)
                self.game_over +=1

        elif ([self.cell[0], self.cell[1], self.cell[2]] == ['X'] * 3 or
              [self.cell[3], self.cell[4], self.cell[5]] == ['X'] * 3 or
              [self.cell[6], self.cell[7], self.cell[8]] == ['X'] * 3 or
              [self.cell[0], self.cell[3], self.cell[6]] == ['X'] * 3 or
              [self.cell[1], self.cell[4], self.cell[7]] == ['X'] * 3 or
              [self.cell[2], self.cell[5], self.cell[8]] == ['X'] * 3 or
              [self.cell[0], self.cell[4], self.cell[8]] == ['X'] * 3 or
              [self.cell[2], self.cell[4], self.cell[6]] == ['X'] * 3):
            if self.game_over == 0:
                self.display_result(2)
                self.game_over += 1

        else:
            if self.count == 9:
                if self.game_over == 0:
                    self.display_result(3)
                    self.game_over += 1

    def get_click_pos(self):

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()  # if mouse is pressed get position of cursor ##

                    if 120 > pos[0] > 60 and 60 < pos[1] < 120:  # 1
                        if self.count % 2 == 0:
                            if self.cell[0] is None:
                                self.display_symbol('O', 1)
                                self.count += 1
                                self.cell[0] = 'O'

                        else:
                            if self.cell[0] is None:
                                self.display_symbol('X', 1)
                                self.count += 1
                                self.cell[0] = 'X'


                    elif 180 > pos[0] > 120 and 60 < pos[1] < 120:  # 2
                        if self.count % 2 == 0:
                            if self.cell[1] is None:
                                self.display_symbol('O', 2)
                                self.count += 1
                                self.cell[1] = 'O'

                        else:
                            if self.cell[1] is None:
                                self.display_symbol('X', 2)
                                self.count += 1
                                self.cell[1] = 'X'


                    elif 240 > pos[0] > 180 and 60 < pos[1] < 120:  # 3
                        if self.count % 2 == 0:
                            if self.cell[2] is None:
                                self.display_symbol('O', 3)
                                self.count += 1
                                self.cell[2] = 'O'

                        else:
                            if self.cell[2] is None:
                                self.display_symbol('X', 3)
                                self.count += 1
                                self.cell[2] = 'X'


                    elif 120 > pos[0] > 60 and 120 < pos[1] < 180:  # 4
                        if self.count % 2 == 0:
                            if self.cell[3] is None:
                                self.display_symbol('O', 4)
                                self.count += 1
                                self.cell[3] = 'O'

                        else:
                            if self.cell[3] is None:
                                self.display_symbol('X', 4)
                                self.count += 1
                                self.cell[3] = 'X'

                    elif 180 > pos[0] > 120 and 120 < pos[1] < 180:  # 5
                        if self.count % 2 == 0:
                            if self.cell[4] is None:
                                self.display_symbol('O', 5)
                                self.count += 1
                                self.cell[4] = 'O'

                        else:
                            if self.cell[4] is None:
                                self.display_symbol('X', 5)
                                self.count += 1
                                self.cell[4] = 'X'

                    elif 240 > pos[0] > 180 and 120 < pos[1] < 180:  # 6
                        if self.count % 2 == 0:
                            if self.cell[5] is None:
                                self.display_symbol('O', 6)
                                self.count += 1
                                self.cell[5] = 'O'

                        else:
                            if self.cell[5] is None:
                                self.display_symbol('X', 6)
                                self.count += 1
                                self.cell[5] = 'X'


                    elif 120 > pos[0] > 60 and 180 < pos[1] < 240:  # 7
                        if self.count % 2 == 0:
                            if self.cell[6] is None:
                                self.display_symbol('O', 7)
                                self.count += 1
                                self.cell[6] = 'O'

                        else:
                            if self.cell[6] is None:
                                self.display_symbol('X', 7)
                                self.count += 1
                                self.cell[6] = 'X'


                    elif 180 > pos[0] > 120 and 180 < pos[1] < 240:  # 8
                        if self.count % 2 == 0:
                            if self.cell[7] is None:
                                self.display_symbol('O', 8)
                                self.count += 1
                                self.cell[7] = 'O'

                        else:
                            if self.cell[7] is None:
                                self.display_symbol('X', 8)
                                self.count += 1
                                self.cell[7] = 'X'


                    elif 240 > pos[0] > 180 and 180 < pos[1] < 240:  # 9
                        if self.count % 2 == 0:
                            if self.cell[8] is None:
                                self.display_symbol('O', 9)
                                self.count += 1
                                self.cell[8] = 'O'

                        else:
                            if self.cell[8] is None:
                                self.display_symbol('X', 9)
                                self.count += 1
                                self.cell[8] = 'X'

                    self.check_win()
                if event.type == pygame.QUIT:
                    # quitting pygame
                    pygame.quit()
                    # Time to quit
                    quit()

            # Flip the display
            # pygame.display.flip()
            pygame.display.update()


object = TicTacToe()
object.get_click_pos()
