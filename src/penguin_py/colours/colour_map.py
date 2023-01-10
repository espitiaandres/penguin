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


# Colours are ANSI escape sequences for the terminal to show them.


# Foreground colours are for the **text**
foreground_colours = {
    "red": "\033[91m",
    "yellow": "\033[93m",
    "green": "\033[92m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "grey": "\033[37m",
}

# Background colours are for the **text's highlight**
background_colours = {
    "red": "\033[41m",
    "yellow": "\033[43m",
    "green": "\033[42m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "grey": "\033[37m",
    "black": "\033[40m",
    "white": "\033[107m",
}

colour_map = {
    "foreground": foreground_colours,
    "background": background_colours,
}
