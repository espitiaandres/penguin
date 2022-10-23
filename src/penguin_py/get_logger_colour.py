from .colour_map import colour_map


def get_logger_colour(colour: str):
    all_possible_colours = list(colour_map.keys())

    if colour not in all_possible_colours:
        return colour_map["grey"]

    return colour_map[colour]
