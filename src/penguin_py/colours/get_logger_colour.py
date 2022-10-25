from typing import Literal

from .colour_map import colour_map


def get_logger_colour(
    colour: str, colour_type: Literal["background_colours", "foreground_colours"]
):
    """
    Gets the logger foreground and background colours using the colour_map dictionary in colour_map.py
    """
    all_possible_colours = list(colour_map[colour_type].keys())

    if colour not in all_possible_colours:
        colour_dict = colour_map[colour_type]

        if colour_type == "foreground_colours":
            return colour_dict["grey"]
        else:
            return colour_dict["black"]

    return colour_map[colour_type][colour]
