import pygame
from pygame.math import Vector2 as Vector

from pyggui import core
from pyggui.widgets.widget import Widget


class Label(Widget):
    def __init__(self, widget_id: str = None, text: str = '', font: pygame.font.Font = None,
                 text_col=core.WHITE, background_col=None, padding=core.default_label_padding,
                 i_padding=core.default_label_i_padding):
        super().__init__(widget_id)

        self.text = text
        self.font = font
        self.text_col = text_col
        self.background_col = background_col
        self.padding = Vector(padding)
        self.i_padding = Vector(i_padding)

        if self.font is None:
            self.font = core.default_font

        if self.background_col is None:
            self.background_col = core.TRANSPARENT

        self.text_surface = None
        self.render()

    def render(self) -> None:
        self.text_surface = self.font.render(self.text, True, self.text_col)
        self.surface = pygame.Surface((self.text_surface.get_size() + (self.i_padding * 2))).convert_alpha()

        # Render Background/Text with internal padding
        self.surface.fill(self.background_col)
        self.surface.blit(self.text_surface, self.i_padding)

        # External Positioning/Padding
        self.rect = self.surface.get_rect()
        self.rect.topleft += self.padding
