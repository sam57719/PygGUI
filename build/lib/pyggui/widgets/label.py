import pygame
from pygame.math import Vector2 as Vector
from pyggui.widgets.widget import Widget


class Label(Widget):
    def __init__(self, widget_id: str = None, text: str = ''):
        super().__init__(widget_id)

        self.text = text
        self.text_surface = None

    def render(self) -> None:
        i_padding = Vector(self.theme['i-padding'])
        e_padding = Vector(self.theme['e-padding'])
        self.theme.changed = False
        self.text_surface = self.theme.font.render(self.text, True, self.theme['text-col'])
        self.surface = pygame.Surface((self.text_surface.get_size() + (i_padding * 2))).convert_alpha()

        # Render Background/Text with internal padding
        self.surface.fill(self.theme['bg-col'])
        self.surface.blit(self.text_surface, i_padding)

        # External Positioning/Padding
        self.rect.size = self.surface.get_size()
        self.rect.topleft += e_padding
