import pygame
from pygame.math import Vector2 as Vector
from pyggui.core import widget_count
from pyggui.core.functions import convert_to_greyscale


class Widget:
    def __init__(self, widget_id: str = None):
        self.widget_id = widget_id

        self.theme = None
        self.padding = Vector(0, 0)

        self.surface = pygame.Surface((0, 0))
        self.rect = self.surface.get_rect()

        self.hidden = False
        self.active = True

        self.greyscale_surface = self.surface.copy()
        self.position = Vector(0, 0)

        self.ui_container = None
        self.theme = None

        self._widget_name = self.__class__.__name__
        self._unique_widget_name = self._generate_widget_id()

        if self.widget_id is None:
            self.widget_id = self._unique_widget_name

    def _generate_widget_id(self) -> str:
        widget_count[self._widget_name] = widget_count.get(self._widget_name, 0) + 1
        return f'{self._widget_name}_{widget_count.get(self._widget_name):02}'

    def draw(self, win) -> None:
        if self.theme.changed:
            self.render()

        if not self.hidden:
            if self.active:
                win.blit(self.surface, self.rect)
            else:
                win.blit(self.greyscale_surface, self.rect)

    def hide(self) -> None:
        self.hidden = True

    def show(self) -> None:
        self.hidden = False

    def toggle_hidden(self) -> None:
        self.hidden = not self.hidden

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False
        self.greyscale_surface = convert_to_greyscale(self.surface)

    def toggle_active(self) -> None:
        self.active = not self.active
        if not self.active:
            self.greyscale_surface = convert_to_greyscale(self.surface)

    def render(self):
        pass

    def update(self):
        pass

    def handle_event(self):
        pass

    @property
    def bottom_of_padding(self):
        return self.rect.bottom + self.padding.y

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.widget_id}'
