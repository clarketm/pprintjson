import re

import setuptools, os


def open_local(paths, mode="r", encoding="utf8"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)
    return open(path, mode=mode, encoding=encoding)


# from pprintjson import __version__
with open_local(["pprintjson", "__init__.py"]) as f:
    version = re.search(r"__version__ = [\"'](\d+\.\d+\.\d+)[\"']", f.read()).group(1)

with open_local(["README.md"]) as f:
    long_description = f.read()

install_requires = ["pygments>=1.6"]

extras_require = {"simplejson": ["simplejson>=2.0.9"]}


setuptools.setup(
    name="pprintjson",
    version=version,
    author="Travis Clarke",
    author_email="travis.m.clarke@gmail.com",
    description="A json pretty printer for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/pprintjson",
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require=extras_require,
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["pprintjson=pprintjson.pprintjson:cli"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
