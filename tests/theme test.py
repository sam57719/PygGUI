import pygame
from pyggui.uimanager import UIManager
from pyggui.widgets import Label

pygame.init()

SIZE = WIDTH, HEIGHT = (1400, 900)

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

ui = UIManager(window, clock)

label = Label(text='Test Label')
ui.add_widget(label)

label2 = Label(text='Test 2nd Label')
ui.add_widget(label2)

ui.mainloop()
