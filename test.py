from penguin import penguin


@penguin(verbose=True)
def test_func():
  for i in range(100000):
    pass
  return "lmfaooo"


if __name__ == "__main__":
  treast = test_func()
