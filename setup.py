import setuptools, os

from pprintjson import __version__

with open(f"{os.path.abspath(os.path.dirname(__file__))}/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pprintjson",
    version=__version__,
    author="Travis Clarke",
    author_email="travis.m.clarke@gmail.com",
    description="A json pretty printer for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/pprintjson",
    install_requires=["pygments"],
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["pprintjson=pprintjson.pprintjson:cli"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
