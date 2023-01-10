from .colour_map import colour_map


def get_default_colours():
    """
    Gets default colours to display in the terminal.

    These being:
    - Foreground: grey
    - Background: black
    """
    grey_foreground_colour = colour_map["foreground"]["grey"]
    black_background_colour = colour_map["background"]["black"]

    return grey_foreground_colour, black_background_colour
