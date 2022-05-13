import pygame
from matplotlib.colors import to_rgb


def contain_int(value, minimum: int = 0, maximum: int = 255):
    return int(min(maximum, max(minimum, value)))


def contain_ints(values, minimum: int = 0, maximum: int = 255):
    return [contain_int(i, minimum, maximum) for i in values]


def adjust_colour(colour, modifier):
    return contain_ints(pygame.math.Vector3(colour) * modifier)


def colour_to_rgb(colour):
    colour = pygame.math.Vector3(to_rgb(colour))
    return colour * 255


def convert_to_greyscale(surface):
    new_surface = surface.copy()
    width, height = new_surface.get_size()
    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = new_surface.get_at((x, y))
            luminance = 0.3 * red + 0.59 * green + 0.11 * blue

            gs_color = (luminance, luminance, luminance, alpha)
            new_surface.set_at((x, y), gs_color)

    return new_surface
