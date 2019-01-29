import setuptools, os

from pprintjson import __version__

with open(f"{os.path.abspath(os.path.dirname(__file__))}/README.md", "r") as fh:
    long_description = fh.read()

install_requires = ["pygments>=1.6"]

extras_require = {"simplejson": ["simplejson>=2.0.9"]}


setuptools.setup(
    name="pprintjson",
    version=__version__,
    author="Travis Clarke",
    author_email="travis.m.clarke@gmail.com",
    description="A json pretty printer for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/pprintjson",
    install_requires=install_requires,
    extras_require=extras_require,
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["pprintjson=pprintjson.pprintjson:cli"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
