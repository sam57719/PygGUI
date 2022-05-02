import pygame
from pyggui.core import *
from pyggui.widgets import Label

pygame.init()


WIDTH, HEIGHT = SIZE = 700, 500
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

label = Label(text='This is a Label', background_col=(100, 149, 237), text_col=WHITE)
label2 = Label(text='This is a Label', background_col=(100, 149, 237), text_col=WHITE)

print(label2.widget_id)


def run():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.constants.K_t:
                    label.toggle_active()

        window.fill(GREY)
        label.draw(window)
        pygame.display.flip()


if __name__ == '__main__':
    run()
