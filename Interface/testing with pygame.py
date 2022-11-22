# -------------------------------

#           IMPORTANT

# |||||||||||||||||||||||||||||

# this file is ONLY for testing

# |||||||||||||||||||||||||||||
# -------------------------------
import sys

import pygame
from pygame import mixer
pygame.init()

# background music



screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

rect = []

test = pygame.Rect(100, 100, 100, 100)
pygame.draw.rect(screen, (255, 255, 255), test)

def move_rec(speed, length):
    for i in range(0, length, speed):
        test = pygame.Rect(i, i, 100, 100)
        pygame.draw.rect(screen,(255,255,255), test)
current_time = 0
button_press_time = 0
counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        move_rec(1, 800)


    current_time = pygame.time.get_ticks()
    pygame.display.update()
    clock.tick(60)


