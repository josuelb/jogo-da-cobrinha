import pygame
from random import randint


class Python:
    def __init__(self, w, h, screen):
        self.screen = screen
        self.x_py = w / 2
        self.y_py = h / 2

        self.w_py = 20
        self.h_py = 20

        self.list_py = []

        self.len_initial = 5

        self.python = ''

    def criate(self):
        self.python = pygame.draw.rect(self.screen, (0, 230, 0), (self.x_py, self.y_py, self.w_py, self.h_py))
        header_python = []
        header_python.append(self.x_py)
        header_python.append(self.y_py)
        self.list_py.append(header_python)
        if len(self.list_py) > self.len_initial:
            del self.list_py[0]

    def draw_python(self):
        for XeY in self.list_py:
            pygame.draw.rect(self.screen, (0, 230, 0), (XeY[0], XeY[1], 20, 20))


class Apple:
    def __init__(self, w, h, screen):
        self.screen = screen
        self.x_apple = randint(40, 600)
        self.y_apple = randint(50, 430)
        self.apple = ''

    def criate(self):
        self.apple = pygame.draw.circle(self.screen, (255, 0, 0), (self.x_apple, self.y_apple), 10)
