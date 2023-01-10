# -*- coding: utf-8 -*-

#
# penguin_py - A lightweight, customizable stopwatch  decorator
#
# Andres Espitia
# espitiaandres.com
# espitiaandres123@gmail.com
#
# License: MIT
#

from typing import Literal

from .colour_map import colour_map


def get_logger_colour(colour: str, colour_type: Literal["background", "foreground"]):
    """
    Gets the logger foreground and background colours using the colour_map dictionary in colour_map.py

    Foreground colours are for the **text**
    Background colours are for the **text's highlight**
    """
    all_possible_colours = list(colour_map[colour_type].keys())

    if colour in all_possible_colours:
        return colour_map[colour_type][colour]

    colour_dict = colour_map[colour_type]

    if colour_type == "foreground":
        return colour_dict["grey"]
    else:
        return colour_dict["black"]
