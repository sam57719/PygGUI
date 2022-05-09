import pygame
from pyggui.uimanager import UIManager
from pyggui.widgets import Label

pygame.init()

SIZE = WIDTH, HEIGHT = (600, 500)

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

ui = UIManager(window)

label = Label(text='Test Label')
ui.add_widget(label)

label2 = Label(text='Test 2nd Label')
ui.add_widget(label2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                label.toggle_hidden()

    ui.draw()
    pygame.display.update()
