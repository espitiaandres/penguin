# Penguin_py

Penguin: a customizable stopwatch decorator

<img
  src="/img/penguin_py_logo.jpg"
  alt="Peter the penguin, penguin_py's mascot."
  title="Peter the penguin, penguin_py's mascot."
  style="display: inline-block; margin: 0 auto; max-width: 200px">

https://github.com/espitiaandres/penguin

More details to follow soon! :)

To install:

`pip install penguin_py`

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
