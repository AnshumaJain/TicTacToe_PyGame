# Import and initialize the pygame library
import pygame

pygame.init()

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PEACH = (255, 200, 150)
CHOCOLATE = (210, 105, 30)
BROWN = (165, 42, 42)

# texts
font = pygame.font.Font('freesansbold.ttf', 20)

# Set up the drawing window
screen = pygame.display.set_mode([300, 300])
# Fill the background with PEACH color
screen.fill(PEACH)


class TicTacToe:

    def __init__(self):
        # initializing vars for win function
        self.row1, self.row2, self.row3 = [0, 0, 0]
        self.col1, self.col2, self.col3 = [0, 0, 0]
        self.dia1, self.dia2 = [0, 0]

        self.cell = 0

    # create an array for cells
    # counter that keeps track of the current cell
    # conditions for each cell index

    def mark(self, symbol='O'):

        if self.cell == 1:
            x, y = 90, 90
            self.row1 += 1
            self.col1 += 1
            self.dia1 += 1
        elif self.cell == 2:
            x, y = 150, 90
            self.row1 += 1
            self.col2 += 1
        elif self.cell == 3:
            x, y = 210, 90
            self.row1 += 1
            self.col3 += 1
            self.dia2 += 1
        elif self.cell == 4:
            x, y = 90, 150
            self.row2 += 1
            self.col1 += 1
        elif self.cell == 5:
            x, y = 150, 150
            self.row2 += 1
            self.col2 += 1
            self.dia1 += 1
            self.dia2 += 1
        elif self.cell == 6:
            x, y = 210, 150
            self.row2 += 1
            self.col3 += 1
        elif self.cell == 7:
            x, y = 90, 210
            self.row3 += 1
            self.col1 += 1
            self.dia2 += 1
        elif self.cell == 8:
            x, y = 150, 210
            self.row3 += 1
            self.col2 += 1
        elif self.cell == 9:
            x, y = 210, 210
            self.row3 += 1
            self.col3 += 1
            self.dia1 += 1

        if symbol == 'O':
            print_text_O(x, y)
        elif symbol == 'X':
            print_text_X(x, y)


def user_interface():
    pygame.display.set_caption('Welcome to Tic-Tac-Toe game')

    text1 = font.render('Player 1: O', True, CHOCOLATE)  # player 1 text
    text_rect1 = text1.get_rect()
    text_rect1.center = (55, 20)
    screen.blit(text1, text_rect1)

    text2 = font.render('Player 2: X', True, CHOCOLATE)  # player 2 text
    text_rect2 = text2.get_rect()
    text_rect2.center = (55, 50)
    screen.blit(text2, text_rect2)

    # Draw a solid vertical & horizontal lines in the center
    line1 = pygame.draw.line(screen, CHOCOLATE, (120, 60), (120, 240), 4)  # vertical line1
    line2 = pygame.draw.line(screen, CHOCOLATE, (180, 60), (180, 240), 4)  # vertical line2
    line3 = pygame.draw.line(screen, CHOCOLATE, (60, 120), (240, 120), 4)  # horizontal line1
    line4 = pygame.draw.line(screen, CHOCOLATE, (60, 180), (240, 180), 4)  # horizontal line2


def check_win(count, t):
    if 3 in [t.row1, t.row2, t.row3, t.col1, t.col2, t.col3, t.dia1, t.dia2]:
        text5 = font.render('Player 1 Wins !', True, BROWN, YELLOW)  # O wins text
        text_rect5 = text5.get_rect()
        text_rect5.center = (100, 150)
        screen.blit(text5, text_rect5)

    elif 3 in [t.row1, t.row2, t.row3, t.col1, t.col2, t.col3, t.dia1, t.dia2]:
        text6 = font.render('Player 2 Wins !', True, BROWN, YELLOW)  # x wins text
        text_rect6 = text6.get_rect()
        text_rect6.center = (100, 150)
        screen.blit(text6, text_rect6)

    elif count == 9:
        text7 = font.render("It's a Tie !", True, BROWN, YELLOW)  # tie text
        text_rect7 = text7.get_rect()
        text_rect7.center = (120, 150)
        screen.blit(text7, text_rect7)


def print_text_O(x, y):
    text3 = font.render('O', True, BROWN)  # O
    text_rect3 = text3.get_rect()
    text_rect3.center = (x, y)
    screen.blit(text3, text_rect3)


def print_text_X(x, y):
    text4 = font.render('X', True, BROWN)  # X
    text_rect4 = text4.get_rect()
    text_rect4.center = (x, y)
    screen.blit(text4, text_rect4)


def main():
    user_interface()

    # initializing vars for win function
    t = TicTacToe()

    count = 0

    # Run until the user asks to quit
    while 1:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                # check if cursor is on grid then count ##
                if 240 > pos[0] > 60 and 60 < pos[1] < 240:
                    count += 1

                # if cursor is on buttons print 0 or X
                # if count < 9:
                if 120 > pos[0] > 60 and 60 < pos[1] < 120:  # 1
                    t.cell = 1
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif 180 > pos[0] > 120 and 60 < pos[1] < 120:  # 2
                    t.cell = 2
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif 240 > pos[0] > 180 and 60 < pos[1] < 120:  # 3
                    t.cell = 3
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif 120 > pos[0] > 60 and 120 < pos[1] < 180:  # 4
                    t.cell = 4
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif 180 > pos[0] > 120 and 120 < pos[1] < 180:  # 5
                    t.cell = 5
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif 240 > pos[0] > 180 and 120 < pos[1] < 180:  # 6
                    t.cell = 6
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif 120 > pos[0] > 60 and 180 < pos[1] < 240:  # 7
                    t.cell = 7
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif 180 > pos[0] > 120 and 180 < pos[1] < 240:  # 8
                    t.cell = 8
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif 240 > pos[0] > 180 and 180 < pos[1] < 240:  # 9
                    t.cell = 9
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

            if event.type == pygame.QUIT:
                # quitting pygame
                pygame.quit()
                # Time to quit
                quit()

            check_win(count, t)

        # Flip the display
        # pygame.display.flip()
        pygame.display.update()


main()
