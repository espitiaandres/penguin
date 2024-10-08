<h1 align="center">
<img
    src="/img/penguin_py_logo.jpg"
    alt="Peter the penguin, penguin-py's mascot."
    title="Peter the penguin, penguin-py's mascot."
    width="200"
/>
</h1>

Peter the penguin logo credits go to `catalyststuff` on [freepik.com](https://www.freepik.com/author/catalyststuff)

<p align="center">
  <a href="https://pypi.python.org/pypi/penguin_py"><img src="https://badge.fury.io/py/penguin_py.svg"></a>
  <a href="http://unlicense.org/"><img src="https://img.shields.io/pypi/l/penguin_py.svg"></a>
  <a href="https://pypi.python.org/pypi/penguin_py"><img src="https://img.shields.io/pypi/pyversions/penguin_py.svg"></a>
</p>

# 🐧 penguin-py 🐧

Penguin is a lightweight, customizable stopwatch ⏱ decorator that helps you determine how long it takes for your functions to run. It supports both synchronous (`@penguin`) and asynchronous (`@penguin_async`) functions.

<!--
Link: https://www.freepik.com/free-vector/cute-happy-penguin-cartoon-icon-illustration-animal-nature-icon-concept-isolated-flat-cartoon-style_10717963.htm#query=penguin%20logo&position=1&from_view=keyword

Credits go to catalystuff on freepik.com
 -->

# Getting Started 🚀

## Table of contents:

- [Source Code](#source_code)
- [Installation](#installation)
  - [With Command Line](#installation_with_cli)
  - [With a `requirements.txt` file](#installation_req_txt)
- [Usage](#usage)
  - [Synchronous Functions](#synchronous_functions)
  - [Asynchronous Functions](#asynchronous_functions)
  - [List of kwargs](#kwargs_list)
- [Documentation](#documentation)
- [Bugs/Requests](#bugs_requests)
- [License](#license)

<a name="source_code"/>

# Source code

The source code of this package lives here: https://github.com/espitiaandres/penguin

<a name="installation"/>

# Installation

<a name="installation_with_cli"/>

## With Command Line

To install `penguin-py` with the command line, run this command:

`pip install penguin-py`.

<a name="installation_req_txt"/>

## With a `requirements.txt` file

To install `penguin-py` using a `requirements.txt` file, add this line to your `requirements.txt` file.

`penguin-py==0.3.12`

<a name="Usage"/>

# Usage

<a name="synchronous_functions"/>

## Synchronous Functions

For **synchronous** functions, use the `@penguin()` decorator.

✅ To run with **default kwargs**:

```python
from penguin_py import penguin


@penguin()
def foo(test1, test2=None):
    # Note: this function can be anything!
    for i in range(10000000):
        pass
    return "test", True


test = foo("", test2="")
```

This will output the following to your logger:

![Sample penguin output](/img/sample_output.png)

✅ To run with **user specified kwargs**:

```python
@penguin(
    verbose=True,
    show_args=True,
    show_return=True,
    foreground='cyan',
    background='yellow',
)
def foo(test1, test2=None):
    for i in range(10000000):
        pass
    return "test", True


test = foo("", test2="")
```

This will output the following to your logger:

![Sample penguin output kwargs](/img/sample_output_kwargs.png)

**Note**: For a more detailed list of all kwargs and their defaults, visit this section: [List of kwargs](#kwargs_list)

❌ Since `penguin` is a decorator that takes in kwargs, do **not** call it without the brackets `()`.

```python
from penguin_py import penguin


@penguin
def foo(test1, test2=None):
    # Note: this function can be anything!
    for i in range(10000000):
        pass
    return "test", True


test = foo("", test2=":")
```

If you do this, you'll get a `TypeError` relating to arguments.

<a name="synchronous_functions"/>

## Asynchronous Functions

For **asynchronous** functions, use the `@penguin_async()` decorator.

✅ To run with **default kwargs**:

```python
from penguin_py import penguin


@penguin_async()
def foo(test1, test2=None):
    # Note: this function can be anything!
    for i in range(10000000):
        pass
    return "test", True


test = foo("", test2="")
```

This will output the following to your logger:

![Sample penguin output](/img/sample_output.png)

✅ To run with **user specified kwargs**:

```python
@penguin(
    verbose=True,
    show_args=True,
    show_return=True,
    foreground='cyan',
    background='yellow',
)
def foo(test1, test2=None):
    for i in range(10000000):
        pass
    return "test", True


test = foo("", test2="")
```

This will output the following to your logger:

![Sample penguin output kwargs](/img/sample_output_kwargs.png)

<a name="kwargs_list"/>

## List of kwargs

- `verbose`: When `True`, it shows all logs that are described by the other kwargs. When `False`,
  each kwarg would determine if that specific log is shown - default: `False`
- `show_args`: When `True`, it shows the function's signature, with the `*args` and `**kwargs` being passed in.
  - default: `False`
- `show_return`: When `True`, it shows the function's return value(s).
  - default: `False`
- `foreground`: When chosen from this list, `["red", "yellow", "green", "blue", "magenta", "cyan", "grey"]`, it colour the logger output **text** the chosen colour.
  - default: `"grey"`
- `background`: When chosen from this list, `["red", "yellow", "green", "blue", "magenta", "cyan", "grey", "black", "white"]`, it colour the logger output **background** the chosen colour.
  - default: `"black"`

<a name="documentation"/>

# Documentation

Documentation of `penguin-py` can be found here: https://github.com/espitiaandres/penguin/blob/master/README.md

<a name="bugs_requests"/>

# Bugs/Requests

If you find any bugs or have any suggestions to `penguin-py`, submit them in the issues tab in the Github repo. This can be found here: https://github.com/espitiaandres/penguin/issues

<a name="license"/>

# License

Distributed under the terms of the MIT license, `penguin-py` is free and open source software.
