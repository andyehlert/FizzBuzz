#!/usr/bin/env python3

# ---------------
# FizzBuzz.py
# Scott A. Ehlert
# ---------------

import sys

# --------------
# fizzbuzz_print
# --------------

def fizzbuzz_print (w, v) :
    """
    print the value
    w a writer
    v the value to print
    """
    w.write(str(v) + "\n")

# ---------------
# fizzbuzz_single
# ---------------

def fizzbuzz_single (n) :
    """
    n the number to be evaluated
    return a string containing the proper print value
    """
    assert n > 0 
    result = ""
    # Check if the number is dividible by 3.
    if (n % 3 == 0) :
        result += "Fizz"
    # Check if the number is dividible by 5.
    if (n % 5 == 0) :
        result += "Buzz"
    # If result is still empty, append the number to the string.
    if (result == "") :
        result += str(n)
    # Ensure the result is not empty.
    assert result != ""

    return result

# --------------
# fizzbuzz_range
# --------------

def fizzbuzz_range (b, e, w = sys.stdout) :
    """
    b the beginning of the range
    e the end of the range (inclusive)
    """
    for n in range(b, (e + 1)) :
        v = fizzbuzz_single(n)
        fizzbuzz_print(w, v)

# ---------------
# fizzbuzz_static
# ---------------

def fizzbuzz_static (w = sys.stdout) :
    """
    w the number to be evaluated
    return a string containing the proper print value
    """
    for i in range(1, 101) :
        current = ""
        # Check if the number is dividible by 3.
        if (i % 3 == 0) :
            current += "Fizz"
        # Check if the number is dividible by 5.
        if (i % 5 == 0) :
            current += "Buzz"
        # If current is still empty, append the number to the string.
        if (current == "") :
            current += str(i)
        # Ensure that current is not empty.
        assert current != ""
        fizzbuzz_print(w, current)
