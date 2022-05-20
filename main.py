import pygame
from random import randint
from pygame.locals import *
from sys import exit

"Inicialização do sistema"
pygame.init()
pygame.font.init()

"Variáveis"
w = 640
h = 480

x_py = w / 2
y_py = h / 2
w_py = 20
h_py = 20
list_py = []

x_apple = randint(40, 600)
y_apple = randint(50, 430)

ponts = 0

time = pygame.time.Clock()
fonts = pygame.font.SysFont('arial', 40, True, True)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Jogo da Cobrinha')


def draw_python(list_py):
    for XeY in list_py:
        pygame.draw.rect(screen, (255, 0, 0), (XeY[0], XeY[1], 20, 20))


while True:
    screen.fill((255, 255, 255))
    time.tick(15)

    msg = f"Pontos: {ponts}"
    text = fonts.render(msg, True, (0, 0, 0))

    header_python = []
    header_python.append(x_py)
    header_python.append(y_py)
    list_py.append(header_python)

    "Criação de objetos"
    apple = pygame.draw.circle(screen, (0, 255, 0), (x_apple, y_apple), 10)
    python = pygame.draw.rect(screen, (255, 0, 0), (x_py, y_py, w_py, h_py))

    "Área de inputs"
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        print(event.type)

    if pygame.key.get_pressed()[K_a]:
        x_py -= 20
    elif pygame.key.get_pressed()[K_d]:
        x_py += 20
    elif pygame.key.get_pressed()[K_w]:
        y_py -= 20
    elif pygame.key.get_pressed()[K_s]:
        y_py += 20

    "Área de colisão"
    if python.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        ponts += 1
        h_py += 10

    "Área de colisão com paredes"
    if x_py >= w:
        x_py = 0
    elif x_py <= -5:
        x_py = w
    elif y_py >= h:
        y_py = 0
    elif y_py <= -5:
        y_py = h

    draw_python(list_py)
    screen.blit(text, (430, 40))
    pygame.display.update()
