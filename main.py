import pygame
from pygame.locals import *
from sys import exit


pygame.init()

w = 640
h = 480
x_rect = w/2
y_rect = h/2
time = pygame.time.Clock()

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Jogo da Cobrinha')

while True:
    screen.fill((0, 0, 0))
    time.tick(30)

    "Área de inputs"
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        print(event.type)

    if pygame.key.get_pressed()[K_a]:
        x_rect -= 20
    elif pygame.key.get_pressed()[K_d]:
        x_rect += 20
    elif pygame.key.get_pressed()[K_w]:
        y_rect -= 20
    elif pygame.key.get_pressed()[K_s]:
        y_rect += 20


    if x_rect >= w:
        x_rect = 0
    if y_rect >= h:
        y_rect = 0
    pygame.draw.rect(screen, (255, 0, 0), (x_rect, y_rect, 30, 40))
    pygame.display.update()
