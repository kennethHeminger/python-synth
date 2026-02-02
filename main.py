import pygame
import numpy

#init pygame & audio
pygame.init()
pygame.mixer.init()

# window to receive events
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Stage 1 - play sound on key space stroke")

beep_sound = pygame.mixer.Sound("beep.wav")

running = True
while running:
    for event in pygame.event.get():
        #Quitting event
        if event.type == pygame.QUIT:
            running = False

        #Space for beep
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                beep_sound.play()

pygame.quit()
