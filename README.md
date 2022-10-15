# Penguin

Penguin: a customizable stopwatch decorator

https://github.com/espitiaandres/penguin

More details to follow :)

To install:

`pip install penguin_py`

To run:

```
from src.penguin_py.penguin import penguin
<!-- from penguin_py.penguin import penguin -->


@penguin(verbose=True)
def test_func(test1, test2=None):
    for i in range(10000):
        pass
    return "test", True


test = test_func("", test2=":")
```
