# 🐧 Penguin_py 🐧

Penguin: a customizable stopwatch decorator ⏱

<img
    src="/img/penguin_py_logo.jpg"
    alt="Peter the penguin, penguin_py's mascot."
    title="Peter the penguin, penguin_py's mascot."
    width="200"
/>

Meet Peter, `penguin_py's` beloved mascot!

https://github.com/espitiaandres/penguin

# Installation

## With Command Line

To install `penguin_py` with the command line, run this command:

`pip install penguin_py`.

## With a `requirements.txt` file

To install `penguin_py` using a `requirements.txt` file, add this line to your `requirements.txt` file.

`penguin-py==0.1.1`

# Usage

To run with default kwargs:

```
from penguin_py import penguin


@penguin()
def test_func(test1, test2=None):
    # NOTE: this function can be anything!
    for i in range(10000):
        pass
    return "test", True


test = test_func("", test2=":")
```

To run with user specified kwargs:

```
@penguin(
    verbose=True,
    show_args=True,
    show_return=True,
)
def test_func(test1, test2=None):
    # NOTE: this function can be anything!
    for i in range(10000):
        pass
    return "test", True


test = test_func("", test2=":")
```

# Documentation

# Bugs/Requests

# License
