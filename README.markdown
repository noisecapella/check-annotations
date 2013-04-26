check-annotations
=================

Tool to do static analysis using Python 3 function annotations.

This is a work in progress. The end goal is to analyze code like this:

    def fib(n : int) -> int:
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    
    fib("xyz")

And fail the analysis because "xyz" is not of type 'int'.
