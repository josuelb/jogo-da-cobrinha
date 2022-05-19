import pygame
from pygame.locals import *
from sys import exit


pygame.init()

w = 640
h = 480
x_rect = w/2
y_rect = h/2


screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Jogo da Cobrinha')

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        print(event.type)
        if event.type == KEYDOWN:
            if event.key == K_w:
                y_rect -= 20
            elif event.key == K_s:
                y_rect += 20
            elif event.key == K_a:
                x_rect -= 20
            elif event.key == K_d:
                x_rect += 20

    pygame.draw.rect(screen, (255, 0, 0), (x_rect, y_rect, 30, 40))
    pygame.display.update()
