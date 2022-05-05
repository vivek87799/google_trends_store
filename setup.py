from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.14'
DESCRIPTION = 'Google Trends Store'
LONG_DESCRIPTION = 'A simple service that gets the data from kafka and pushes it to google cloud'

# Setting up
setup(
    name="storetrends",
    version=VERSION,
    author="Nullfinders (Vivek Loganathan)",
    author_email="<vivek87799@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['faust', 'kafka-python'],
    keywords=['python', 'googel trends'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Linux :: Ubuntu 22.04",
        "Operating System :: Microsoft :: Windows",
    ]
)

