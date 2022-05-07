import pygame
from pyggui.core import *
from pyggui.widgets import Label

from pyggui.uimanager import UIManager
import random


pygame.init()


WIDTH, HEIGHT = SIZE = 700, 500
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

ui = UIManager(window)

messages = ["'Allo 'Allo Sam!", "Hello", "I ask ze questions"]

for message in messages:
    _ = Label(text=message, background_col=(100, 149, 237), text_col=WHITE)
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

        window.fill(GREY)
        ui.draw()
        pygame.display.update()


if __name__ == '__main__':
    run()

