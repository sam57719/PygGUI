import pygame
from pyggui.core import *
from pyggui.widgets import Label

from pyggui.uimanager import UIManager
import random


pygame.init()

bgcol = "#608BD5"

WIDTH, HEIGHT = SIZE = 700, 500
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

ui = UIManager(window)

messages = [str(i) for i in range(14)]

for message in messages:
    _ = Label(text=message, background_col=bgcol, text_col=WHITE)
    ui.add_widget(_)


def run():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.constants.K_t:
                    random.choice(ui.widgets).toggle_active()

        ui.draw()
        pygame.display.update()


if __name__ == '__main__':
    run()

