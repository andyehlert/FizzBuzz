#!/usr/bin/env python3

# ---------------
# FizzBuzz.py
# Scott A. Ehlert
# ---------------

# -------
# imports
# -------

import sys
from io       import StringIO


# --------------
# fizzbuzz_print
# --------------

def fizzbuzz_print (w, v) :
    """
    print the value
    w a writer
    v the value to print
    """
    # Write the value provided by the caller into the output stream. 
    w.write(str(v) + "\n")

# -------------
# fizzbuzz_read
# -------------

def fizzbuzz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    # Split the input string into a list using a blank space as a delimeter.
    a = s.split()
    # Ensure that the caller provided at least two values.
    assert len(a) > 1
    return [int(a[0]), int(a[1])]

# ---------------
# fizzbuzz_single
# ---------------

def fizzbuzz_single (n) :
    """
    n the number to be evaluated
    return a string containing the proper print value
    """
    # Initialize an IO stream for accumulating output.
    result = StringIO("")
    # Check if the number is dividible by 3.
    if (n % 3 == 0) :
        result.write("Fizz")
    # Check if the number is dividible by 5.
    if (n % 5 == 0) :
        result.write("Buzz")
    # If result is still empty, append the number to the string.
    if (result.getvalue() == "") :
        result.write(str(n))
    # Return the string value of the output stream.
    return result.getvalue()

# --------------
# fizzbuzz_range
# --------------

def fizzbuzz_custom (b, e, w = sys.stdout) :
    """
    b the beginning of the range
    e the end of the range (inclusive)
    w the output stream for the results
    """
    assert b <= e
    for n in range(b, (e + 1)) :
        v = fizzbuzz_single(n)
        fizzbuzz_print(w, v)

# ----------------
# fizzbuzz_default
# ----------------

def fizzbuzz_default (w = sys.stdout) :
    """
    w the output stream that results will be written to
    """
    for n in range(1, 101) :
        v = fizzbuzz_single(n)
        fizzbuzz_print(w, v)

# --------------
# fizzbuzz_solve
# --------------

def fizzbuzz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        # Read in two ints from the current line.
        i, j = fizzbuzz_read(s)
        # Call the custom fizzbuzz function using the two ints as the range.
        fizzbuzz_custom(i, j, w)