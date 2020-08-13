import pygame

pygame.init()

#### Create a canvas on which to display everything ####
window = (400,400)
screen = pygame.display.set_mode(window)
#### Create a canvas on which to display everything ####

#### Create a surface with the same size as the window ####

#### Create a surface with the same size as the window ####

#### Populate the surface with objects to be displayed ####
pygame.draw.rect(screen,(0,255,255),(20,20,40,40))
pygame.draw.rect(screen,(255,0,255),(120,120,50,50))
#### Populate the surface with objects to be displayed ####

#### Blit the surface onto the canvas ####
#screen.blit(background,(0,0))
#### Blit the surface onto the canvas ####

#### Update the the display and wait ####
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#### Update the the display and wait ####

pygame.quit()

# Defining 9 buttons + grid button
button_grid = pygame.draw.rect(screen, black, (60, 60, 180, 180))
pygame.display.flip()

button1 = [60, 120, 60, 120]
pygame.display.flip()

button2 = pygame.draw.rect(screen, black, (120, 60, 60, 60))
pygame.display.flip()

button3 = pygame.draw.rect(screen, black, (180, 60, 60, 60))
pygame.display.flip()

button4 = pygame.draw.rect(screen, black, (60, 120, 60, 60))
pygame.display.flip()

button5 = pygame.draw.rect(screen, black, (120, 120, 60, 60))
pygame.display.flip()

button6 = pygame.draw.rect(screen, black, (180, 120, 60, 60))
pygame.display.flip()

button7 = pygame.draw.rect(screen, black, (60, 180, 60, 60))
pygame.display.flip()

button8 = pygame.draw.rect(screen, black, (120, 180, 60, 60))
pygame.display.flip()

button9 = pygame.draw.rect(screen, black, (180, 180, 60, 60))
pygame.display.flip()
