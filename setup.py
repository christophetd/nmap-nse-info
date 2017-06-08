import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nse-info",
    version = "0.1",
    author = "Christophe Tafani-Dereeper",
    author_email = "christophe@tafani-dereeper.me",
    description = ("An interactive command-line tool to search and browse NMAP NSE scripts"),
    keywords = "nse nmap script",
    packages=['nseinfo', 'nseinfo/actions', 'nseinfo/parsing'],
    entry_points={
        "console_scripts": ['nseinfo = nseinfo.nseinfo:main']
    },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)