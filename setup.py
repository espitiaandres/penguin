from setuptools import setup
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='penguin_py',
    version='0.0.1',
    description='Penguin: a customizable stopwatch decorator',
    author= 'espitiaandres',
    url = 'https://github.com/espitiaandres/penguin',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['penguin python', 'penguin_py', 'stopwatch', 'timer', 'penguin_py timer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    py_modules=['penguin_py'],
    package_dir={'':'src'},
    install_requires = [
      # Import requirements here
    ]
)
