# 🐧 Penguin_py 🐧

Penguin is a lightweight, customizable stopwatch ⏱ decorator that helps you determine how long it takes for your functions to run.

<img
    src="/img/penguin_py_logo.jpg"
    alt="Peter the penguin, penguin_py's mascot."
    title="Peter the penguin, penguin_py's mascot."
    width="200"
/>

Meet Peter, `penguin_py's` beloved mascot!
<!--
Link: https://www.freepik.com/free-vector/cute-happy-penguin-cartoon-icon-illustration-animal-nature-icon-concept-isolated-flat-cartoon-style_10717963.htm#query=penguin%20logo&position=1&from_view=keyword

Credits go to catalystuff on freepik.com
 -->

# Source code

The source code of this package lives here: https://github.com/espitiaandres/penguin

# Installation

## With Command Line

To install `penguin_py` with the command line, run this command:

`pip install penguin_py`.

## With a `requirements.txt` file

To install `penguin_py` using a `requirements.txt` file, add this line to your `requirements.txt` file.

`penguin-py==0.1.1`

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

This will output the following to your logger:

![Sample penguin output](/img/sample_output.png)

✅ To run with **user specified kwargs**:

```
@penguin(
    verbose=True,
    show_args=True,
    show_return=True,
)
def test_func(test1, test2=None):
    # NOTE: this function can be anything!
    for i in range(10000000):
        pass
    return "test", True


test = test_func("", test2=":")
```

This will output the following to your logger:

![Sample penguin output kwargs](/img/sample_output_kwargs.png)

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

**Note:** by default, all kwargs are set to `False`.

- `verbose`: When `True`, it shows all logs that are described by the other kwargs. When `False`,
  each kwarg would determine if that specific log is shown.
- `show_args`: When `True`, it shows the function's signature, with the `*args` and `**kwargs` being passed in.
- `show_return`: When `True`, it shows the function's return value(s).

# Documentation

Documentation of `penguin_py` can be found here: https://github.com/espitiaandres/penguin/blob/master/README.md

# Bugs/Requests

If you find any bugs or have any suggestions to `penguin_py`, submit them in the issues tab in the Github repo. This can be found here: https://github.com/espitiaandres/penguin/issues

# License

Distributed under the terms of the MIT license, `penguin_py` is free and open source software.
