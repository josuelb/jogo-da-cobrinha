import pygame
from random import randint
from pygame.locals import *
from sys import exit
from objects import person

"Variáveis"
w = 640
h = 480

"Inicialização do sistema"
pygame.init()
pygame.font.init()
time = pygame.time.Clock()
fonts = pygame.font.SysFont('arial', 40, True, True)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Jogo da Cobrinha')

x_apple = randint(40, 600)
y_apple = randint(50, 430)

ponts = 0

python = person.Python(w, h, screen)
apple = person.Apple(w, h, screen)

while True:
    screen.fill((255, 255, 255))
    time.tick(15)

    msg = f"Pontos: {ponts}"
    text = fonts.render(msg, True, (0, 0, 0))

    "Criação de objetos"
    apple.criate()
    python.criate()

    "Área de inputs"
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        print(event.type)

    if pygame.key.get_pressed()[K_a]:
        python.x_py -= 20
    elif pygame.key.get_pressed()[K_d]:
        python.x_py += 20
    elif pygame.key.get_pressed()[K_w]:
        python.y_py -= 20
    elif pygame.key.get_pressed()[K_s]:
        python.y_py += 20

    "Área de colisão"
    if python.python.colliderect(apple.apple):
        apple.x_apple = randint(40, 600)
        apple.y_apple = randint(50, 430)
        ponts += 1
        python.h_py += 10

    "Área de colisão com paredes"
    if python.x_py >= w:
        python.x_py = 0
    elif python.x_py <= -5:
        python.x_py = w
    elif python.y_py >= h:
        python.y_py = 0
    elif python.y_py <= -5:
        python.y_py = h

    python.draw_python()
    screen.blit(text, (430, 40))
    pygame.display.update()
