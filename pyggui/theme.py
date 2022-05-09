import json
import os
import pygame

pygame.font.init()

_DEFAULT_THEME_PATH = 'assets/default_theme.json'
_DEFAULT_THEME_PATH = os.path.join(os.path.dirname(__file__), _DEFAULT_THEME_PATH)


class Theme:
    def __init__(self, file=None, dict_=None):
        self.name = None
        self.colours = None
        self.font = None

        if file is None and dict_ is None:
            _ = self.from_file(_DEFAULT_THEME_PATH)
        elif file is not None:
            _ = self.from_file(file)
        elif dict_ is not None:
            self.dict_ = self.from_dict(dict_)

    def from_file(self, file):
        with open(file, 'r') as theme_file:
            theme_json = json.load(theme_file)
            self.from_dict(theme_json)

        return self

    def from_dict(self, theme_dict):
        self.name = theme_dict.get('name', None)
        self.font = theme_dict.get('font', None)

        colours = theme_dict.get('colours', None)
        if colours is not None:
            for colour_name, colour in colours.items():
                if colour is None:
                    colour = (0,0,0,0)

                setattr(self, colour_name, colour)
        else:
            raise Exception("No colours found in theme")

        if self.font is not None:
            self.font = self._get_font(self.font)

        return self

    @staticmethod
    def _get_font(font):
        name = font.get('name')
        size = font.get('size')

        try:
            font_ = pygame.font.Font(name, size)
        except FileNotFoundError:
            font_ = pygame.font.SysFont(name, size)

        font_.set_bold(font.get('bold', False))
        font_.set_italic(font.get('italic', False))
        font_.set_underline(font.get('underline', False))

        return font_


if __name__ == '__main__':
    theme = Theme()
    theme.from_file(_DEFAULT_THEME_PATH)
