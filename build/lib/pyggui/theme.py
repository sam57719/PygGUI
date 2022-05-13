import json
import os
import pygame
from pprint import pformat

from pyggui.core import TRANSPARENT

pygame.font.init()

_DEFAULT_THEME_PATH = 'assets/themes/default_theme.json'
_DEFAULT_THEME_PATH = os.path.join(os.path.dirname(__file__), _DEFAULT_THEME_PATH)

NULL_THEME_DEFAULTS = {
    "col": TRANSPARENT,
    "width": 0,
    "padding": [0, 0],
    "radius": 0,
    "font": {
      "name": "calibri",
      "size": 32
    }
}


class Theme:
    def __init__(self, file=None):
        self.file = file

        if self.file is None:
            self.file = _DEFAULT_THEME_PATH

        self.changed = False
        self._all_styles = self._load_theme_json(self.file)
        self._top_level_theme = self._all_styles.get("*")
        self._styles = self._top_level_theme.copy()

    @staticmethod
    def _load_theme_json(file):
        with open(file, mode='r') as theme_file:
            themes = json.load(theme_file)

        return themes

    def get_widget_theme(self, widget=None):
        widget_theme = self._top_level_theme.copy()

        if widget is None:
            return widget_theme

        widget_type = widget.__class__.__name__.lower()

        # Update the widget theme with the widget type level attributes
        widget_type_theme = self._all_styles.get(widget_type, {})
        widget_theme |= widget_type_theme

        new_theme = Theme()
        new_theme._styles = widget_theme.copy()

        return new_theme

    def __getitem__(self, item):
        value = self._styles.get(item, None)
        if value is None and any(key in item for key in NULL_THEME_DEFAULTS.keys()):
            value = [v for k, v in NULL_THEME_DEFAULTS.items() if k == item or k in item][0]

        return value

    def __setitem__(self, item, value):
        old_styles = self._styles.copy()
        if item in self._styles:
            self._styles["bg-col"] = value

        self.changed = self.changed or old_styles != self._styles

    def __repr__(self):
        return pformat(self._styles)

    @property
    def font(self):
        font_dict = self['font']
        name = font_dict.get('name')
        size = font_dict.get('size')

        try:
            font_ = pygame.font.Font(name, size)
        except FileNotFoundError:
            font_ = pygame.font.SysFont(name, size)

        font_.set_bold(font_dict.get('bold', False))
        font_.set_italic(font_dict.get('italic', False))
        font_.set_underline(font_dict.get('underline', False))

        return font_

    def copy(self):
        copy = Theme()
        copy._styles = self._styles.copy()

        return copy


if __name__ == '__main__':
    theme = Theme()
    print(theme)
