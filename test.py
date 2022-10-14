from penguin import penguin


@penguin(verbose=True)
def test_func(test1, test2=None):
    for i in range(10000):
        pass
    return "test", True


if __name__ == "__main__":
    test = test_func("", test2=":")
