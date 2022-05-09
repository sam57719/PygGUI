import pygame
from pyggui.core import *
from pyggui.widgets import Widget
from pyggui.theme import Theme
from pygame.math import Vector2 as Vector


class UIManager:
    def __init__(self, window, size=None, position=None, theme=None):
        self.window = window
        self.size = size
        self.position = position
        self.theme = Theme(theme)

        self.size = Vector(self.size) if self.size is not None else Vector(self.window.get_size())
        self.position = Vector(self.position) if self.position is not None else Vector()

        self.widgets = []
        self.last_widget = None
        self.ui_surface = pygame.Surface(self.size)

    def add_widget(self, widget):
        if not isinstance(widget, Widget):
            raise TypeError(f'widget parameter must be a Widget, not {type(widget).__name__}')

        widget.ui_container = self
        if widget.theme is None:
            widget.theme = self.theme

        widget.render()

        if self.last_widget is not None:
            widget.rect.y += self.last_widget.bottom_of_padding

        self.widgets.append(widget)
        self.last_widget = widget

    def draw(self):
        self.ui_surface.fill(self.theme.main_bg)
        for widget in self.widgets:
            widget.draw(self.ui_surface)

        self.window.blit(self.ui_surface, self.position)

    def update(self):
        pass

    def handle_events(self, events):
        pass
