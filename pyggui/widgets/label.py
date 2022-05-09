import pygame
from pygame.math import Vector2 as Vector

from pyggui import core
from pyggui.widgets.widget import Widget


class Label(Widget):
    def __init__(self, widget_id: str = None, text: str = '', padding=(0, 0), i_padding=(0, 0)):
        super().__init__(widget_id)

        self.text = text
        self.background_col = None
        self.background_col = None
        self.padding = Vector(padding)
        self.i_padding = Vector(i_padding)

        self.text_surface = None

    def render(self) -> None:
        self.text_surface = self.theme.font.render(self.text, True, self.theme.text_col)
        self.surface = pygame.Surface((self.text_surface.get_size() + (self.i_padding * 2))).convert_alpha()

        # Render Background/Text with internal padding
        self.surface.fill(self.theme.label_bg)
        self.surface.blit(self.text_surface, self.i_padding)

        # External Positioning/Padding
        self.rect = self.surface.get_rect()
        self.rect.topleft += self.padding
