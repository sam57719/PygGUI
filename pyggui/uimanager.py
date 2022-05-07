import pygame
from pyggui.core import *
from pyggui.widgets import Widget
from pygame.math import Vector2 as Vector


class UIManager:
    def __init__(self, window):
        self.window = window
        self.widgets = []
        self.last_widget = None

    def add_widget(self, widget):
        if not isinstance(widget, Widget):
            raise TypeError(f'widget parameter must be a Widget, not {type(widget).__name__}')

        widget.ui_container = self

        if self.last_widget is not None:
            widget.rect.y += self.last_widget.bottom_of_padding

        self.widgets.append(widget)
        self.last_widget = widget

    def draw(self):
        for widget in self.widgets:
            widget.draw(self.window)

    def update(self):
        pass

    def handle_events(self, events):
        pass
