import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pprintjson",
    version="0.0.4",
    author="Travis Clarke",
    author_email="travis.m.clarke@gmail.com",
    description="A json pretty printer for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/pprintjson",
    install_requires = ["pygments"],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
