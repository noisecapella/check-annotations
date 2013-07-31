check-annotations
=================

Tool to do static analysis using Python 3 function annotations.

TODO: accomplish similar goal using type hints in docstrings

This is a work in progress. The end goal is to analyze code like this:

    def fib(n : int) -> int:
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    
    fib("xyz")

And fail the analysis because "xyz" is not of type 'int'.

Installation
------------

Current steps:
- Create a Python 3 virtualenv and activate it
- Install logilab-common from source: http://www.logilab.org/848
- Get astroid source: https://bitbucket.org/logilab/astroid/
- Before installing astroid, cd to the astroid directory and run `patch -p1 < /path/to/check-annotations/astroid-function-annotations.patch`
- Install astroid using `python setup.py install`
- Now you can run `python check-annotations.py --check filename.py`, or use `--help` to list other options 