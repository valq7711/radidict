import re
from setuptools import setup

import radidict

setup(
    name="radidict",
    version=radidict.__version__,
    url="https://github.com/valq7711/radidict",
    license=radidict.__license__,
    author=radidict.__author__,
    author_email="valq7711@gmail.com",
    maintainer=radidict.__author__,
    maintainer_email="valq7711@gmail.com",
    description="radix-tree dict - the base for routers",
    py_modules=['radidict'],
    platforms="any",
    scripts=['radidict.py'],
    keywords='radix tree python routing http router',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers"
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

)
