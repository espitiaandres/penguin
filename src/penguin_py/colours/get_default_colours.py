from .colour_map import colour_map


def get_default_colours():
    grey_foreground_colour = colour_map["foreground_colours"]["grey"]
    black_background_colour = colour_map["background_colours"]["black"]

    return grey_foreground_colour, black_background_colour
