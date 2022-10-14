from penguin import penguin


@penguin(verbose=True)
def test_func():
    for i in range(1000000000):
        pass
    return "test"


if __name__ == "__main__":
    test = test_func()
