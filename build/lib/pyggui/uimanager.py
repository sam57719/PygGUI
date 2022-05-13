import pygame
import sys
from pyggui.core import *
from pyggui.widgets import Widget
from pyggui.theme import Theme
from pygame.math import Vector2 as Vector


class UIManager:
    def __init__(self, window, clock=None, size=None, position=None, theme=None):
        self.window = window
        self.clock = clock
        self.size = size
        self.position = position
        self.theme = Theme(theme)

        self.clock = self.clock if self.clock is not None else pygame.time.Clock()
        self.size = Vector(self.size) if self.size is not None else Vector(self.window.get_size())
        self.position = Vector(self.position) if self.position is not None else Vector()

        self.widgets = []
        self.last_widget = None
        self.ui_surface = pygame.Surface(self.size)
        self.looping = False

    def add_widget(self, widget):
        if not isinstance(widget, Widget):
            raise TypeError(f'widget parameter must be a Widget, not {type(widget).__name__}')

        widget.ui_container = self
        if widget.theme is None:
            widget.theme = self.theme.get_widget_theme(widget)

        widget.render()

        if self.last_widget is not None:
            widget.rect.y += self.last_widget.bottom_of_padding

        self.widgets.append(widget)
        self.last_widget = widget

    def mainloop(self):
        self.looping = True
        while self.looping:
            self.loop()
            pygame.display.flip()
            self.clock.tick(FPS)

        self.quit()

    def loop(self, events=None):
        self.handle_events(events)
        self.update()
        self.draw()

    def draw(self):
        self.ui_surface.fill(self.theme['bg-col'])
        for widget in self.widgets:
            widget.draw(self.ui_surface)

        self.window.blit(self.ui_surface, self.position)

    def update(self):
        for widget in self.widgets:
            widget.update()

    def handle_events(self, events):
        events = events if events is not None else pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()

    def quit(self):
        if self.looping:
            self.looping = False
        else:
            pygame.display.quit()
            sys.exit()
