import setuptools
from setuptools import setup

# from src.penguin_py import penguin
# # # <!-- from penguin_py.penguin import penguin -->


# @penguin(verbose=True)
# def test_func(test1, test2=None):
#     for i in range(10000):
#         pass
#     return "test", True


# test_func("")

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="penguin_py",
    version="0.0.5",
    description="Penguin: a customizable stopwatch decorator",
    author="espitiaandres",
    url="https://github.com/espitiaandres/penguin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["penguin python", "penguin_py", "stopwatch", "timer", "penguin_py timer"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    py_modules=["penguin_py"],
    package_dir={"": "src"},
    install_requires=[
        # Import requirements here
        "pre-commit",
    ],
)
