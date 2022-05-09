from pyggui.core import *
from pyggui.theme import Theme
from pyggui.uimanager import UIManager
from pyggui.widgets import Label
import pygame

pygame.font.init()

print(pygame.font.get_fonts())
font = pygame.font.SysFont('couriernew', 13)

theme = Theme()

print(theme.colours.get("main_bg"))

print(theme.font)

pygame.init()

bgcol = "#608BD5"

WIDTH, HEIGHT = SIZE = 700, 500
FPS = 60

pygame.font.init()

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

ui = UIManager(window)

messages = [str(i) for i in range(13)]

for message in messages:
    _ = Label(text=message, background_col=bgcol, text_col=WHITE, font=theme.font)
    ui.add_widget(_)


def run():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill("grey10")
        ui.draw()
        pygame.display.update()


if __name__ == '__main__':
    run()
