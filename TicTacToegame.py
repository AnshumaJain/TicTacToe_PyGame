
# Import and initialize the pygame library
import pygame
pygame.init()

# Colors
black = (0, 0, 0)
yellow = (255, 255, 0)
peach = (255, 200, 150)
chocolate = (210, 105, 30)
brown = (165, 42, 42)

# texts
font = pygame.font.Font('freesansbold.ttf', 20)

# Set up the drawing window
screen = pygame.display.set_mode([300, 300])
# Fill the background with peach color
screen.fill(peach)

class tic_tac_toe():

    
    # initializing vars for win function
    row1, row2, row3 = [0, 0, 0]
    col1, col2, col3 = [0, 0, 0]
    dia1, dia2 = [0, 0]

    cell = 0

    #create an array for cells
    #counter that keeps track of the cirrent cell
    #conditions for each cell index

    def mark(self, symbol):

        if self.cell == 1:
            x, y = 90, 90
            t.row1 += 1
            t.col1 += 1
            t.dia1 += 1
        elif self.cell == 2:
            x, y = 150, 90
            t.row1 += 1
            t.col2 += 1
        elif self.cell == 3:
            x, y = 210, 90
            t.row1 += 1
            t.col3 += 1
            t.dia2 += 1
        elif self.cell == 4:
            x, y = 90, 150
            t.row2 += 1
            t.col1 += 1
        elif self.cell == 5:
            x, y = 150, 150
            t.row2 += 1
            t.col2 += 1
            t.dia1 += 1
            t.dia2 += 1
        elif self.cell == 6:
            x, y = 210, 150
            t.row2 += 1
            t.col3 += 1
        elif self.cell == 7:
            x, y = 90, 210
            t.row3 += 1
            t.col1 += 1
            t.dia2 += 1
        elif self.cell == 8:
            x, y = 150, 210
            t.row3 += 1
            t.col2 += 1
        elif self.cell == 9:
            x, y = 210, 210
            t.row3 += 1
            t.col3 += 1
            t.dia1 += 1

        if symbol == 'O':
            PrintText_O(x, y)
        elif symbol == 'X':
            PrintText_X(x, y)


def UI():

    pygame.display.set_caption('Welcome to Tic-Tac-Toe game')

    text1 = font.render('Player 1: O', True, chocolate) # player 1 text
    textRect1 = text1.get_rect()
    textRect1.center = (55, 20)
    screen.blit(text1, textRect1)

    text2 = font.render('Player 2: X', True, chocolate) # player 2 text
    textRect2 = text2.get_rect()
    textRect2.center = (55, 50)
    screen.blit(text2, textRect2)


    # Draw a solid vertical & horizontal lines in the center
    line1 = pygame.draw.line(screen, chocolate, (120, 60), (120, 240), 4)  # vertical line1
    line2 = pygame.draw.line(screen, chocolate, (180, 60), (180, 240), 4)  # vertical line2
    line3 = pygame.draw.line(screen, chocolate, (60, 120), (240, 120), 4)  # horizontal line1
    line4 = pygame.draw.line(screen, chocolate, (60, 180), (240, 180), 4)  # horizontal line2


def check_win(count, t):


    if 3 in [t.row1o, t.row2o, t.row3o, t.col1o, t.col2o, t.col3o, t.dia1o, t.dia2o]:
        text5 = font.render('Player 1 Wins !', True, brown, yellow)  # O wins text
        textRect5 = text5.get_rect()
        textRect5.center = (100, 150)
        screen.blit(text5, textRect5)

    elif 3 in [t.row1x, t.row2x, t.row3x, t.col1x, t.col2x, t.col3x, t.dia1x, t.dia2x]:
        text6 = font.render('Player 2 Wins !', True, brown, yellow)  # x wins text
        textRect6 = text6.get_rect()
        textRect6.center = (100, 150)
        screen.blit(text6, textRect6)

    elif count == 9:
        text7 = font.render("It's a Tie !", True, brown, yellow)  # tie text
        textRect7 = text7.get_rect()
        textRect7.center = (120, 150)
        screen.blit(text7, textRect7)


def PrintText_O(x, y):
    text3 = font.render('O', True, brown)  # O
    textRect3 = text3.get_rect()
    textRect3.center = (x, y)
    screen.blit(text3, textRect3)


def PrintText_X(x, y):
    text4 = font.render('X', True, brown)  # X
    textRect4 = text4.get_rect()
    textRect4.center = (x, y)
    screen.blit(text4, textRect4)


def main():
    UI()

    # initializing vars for win function
    t = tic_tac_toe

    count = 0


    # Run until the user asks to quit
    while 1:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                ## check if cursor is on grid then count ##
                if pos[0] < 240 and pos[0] > 60 and pos[1] > 60 and pos[1] < 240:
                    count += 1

                # if cursor is on buttons print 0 or X
                    #if count < 9:
                if pos[0] < 120 and pos[0] > 60 and pos[1] > 60 and pos[1] < 120:   # 1
                    t.cell = 1
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif pos[0] < 180 and pos[0] > 120 and pos[1] > 60 and pos[1] < 120: #2
                    t.cell = 2
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif pos[0] < 240 and pos[0] > 180 and pos[1] > 60 and pos[1] < 120: #3
                    t.cell = 3
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif pos[0] < 120 and pos[0] > 60 and pos[1] > 120 and pos[1] < 180: #4
                    t.cell = 4
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif pos[0] < 180 and pos[0] > 120 and pos[1] > 120 and pos[1] < 180: #5
                    t.cell = 5
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif pos[0] < 240 and pos[0] > 180 and pos[1] > 120 and pos[1] < 180: #6
                    t.cell = 6
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif pos[0] < 120 and pos[0] > 60 and pos[1] > 180 and pos[1] < 240: #7
                    t.cell = 7
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif pos[0] < 180 and pos[0] > 120 and pos[1] > 180 and pos[1] < 240: #8
                    t.cell = 8
                    if count % 2 == 0:
                        t.mark('O')
                    else:
                        t.mark('X')

                elif pos[0] < 240 and pos[0] > 180 and pos[1] > 180 and pos[1] < 240: #9
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
        #pygame.display.flip()
        pygame.display.update()


main()