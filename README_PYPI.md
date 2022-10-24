# 🐧 Penguin_py 🐧

Penguin is a lightweight, customizable stopwatch ⏱ decorator that helps you determine how long it takes for your functions to run.

# Source code

The source code of this package lives here: https://github.com/espitiaandres/penguin

# Installation

## With Command Line

To install `penguin_py` with the command line, run this command:

`pip install penguin_py`.

## With a `requirements.txt` file

To install `penguin_py` using a `requirements.txt` file, add this line to your `requirements.txt` file.

`penguin-py==0.2.5`

# Usage

✅ To run with **default kwargs**:

```
from penguin_py import penguin


@penguin()
def test_func(test1, test2=None):
    # NOTE: this function can be anything!
    for i in range(10000000):
        pass
    return "test", True


test = test_func("", test2=":")
```

✅ To run with **user specified kwargs**:

```
@penguin(
    verbose=True,
    show_args=True,
    show_return=True,
    foreground='cyan',
    background='yellow',
)
def test_func(test1, test2=None):
    for i in range(10000000):
        pass
    return "test", True


test = test_func("", test2=":")
```

**Note**: For a more detailed list of all kwargs and their defaults, visit this section: [List of kwargs](#kwargs_list)

❌ Since `penguin` is a decorator that takes in kwargs, do **not** call it without the brackets `()`.

```from penguin_py import penguin


@penguin
def test_func(test1, test2=None):
    # NOTE: this function can be anything!
    for i in range(10000000):
        pass
    return "test", True


test = test_func("", test2=":")
```

You'll get a `TypeError` relating to arguments.

## List of kwargs

- `verbose`: When `True`, it shows all logs that are described by the other kwargs. When `False`,
each kwarg would determine if that specific log is shown
    - default: `False`
- `show_args`: When `True`, it shows the function's signature, with the `*args` and `**kwargs` being passed in.
    - default: `False`
- `show_return`: When `True`, it shows the function's return value(s).
    - default: `False`
- `foreground`: When chosen from this list, `["red" "yellow", "green", "blue", "magenta", "cyan", "grey"]`, it colour the logger output **text** the chosen colour.
    - default: `"grey"`
- `background`: When chosen from this list, `["red" "yellow", "green", "blue", "magenta", "cyan", "grey", "black", "white"]`, it colour the logger output **background** the chosen colour.
    - default: `"black"`

# Documentation

Documentation of `penguin_py` can be found here: https://github.com/espitiaandres/penguin/blob/master/README.md

# Bugs/Requests

If you find any bugs or have any suggestions to `penguin_py`, submit them in the issues tab in the Github repo. This can be found here: https://github.com/espitiaandres/penguin/issues

# License

Distributed under the terms of the MIT license, `penguin_py` is free and open source software.