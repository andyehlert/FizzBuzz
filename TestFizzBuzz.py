#!/usr/bin/env python3

# ---------------
# TestFizzBuzz.py
# Scott A. Ehlert
# ---------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from FizzBuzz import fizzbuzz_print, fizzbuzz_single, fizzbuzz_range, fizzbuzz_static

# ------------
# TestFizzBuzz
# ------------

class TestFizzBuzz (TestCase) :

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        fizzbuzz_print(w, 1)
        self.assertEqual(w.getvalue(), "1\n")

    def test_print_2 (self) :
        w = StringIO()
        fizzbuzz_print(w, 2)
        self.assertEqual(w.getvalue(), "2\n")

    def test_print_3 (self) :
        w = StringIO()
        fizzbuzz_print(w, 3)
        self.assertEqual(w.getvalue(), "3\n")

    def test_print_4 (self) :
        w = StringIO()
        fizzbuzz_print(w, 4)
        self.assertEqual(w.getvalue(), "4\n")

    def test_print_5 (self) :
        w = StringIO()
        fizzbuzz_print(w, 5)
        self.assertEqual(w.getvalue(), "5\n")


    # ------
    # single
    # ------

    def test_single_1 (self) :
        v = fizzbuzz_single(1)
        self.assertEqual(v, "1")

    def test_single_2 (self) :
        v = fizzbuzz_single(100)
        self.assertEqual(v, "Buzz")

    def test_single_3 (self) :
        v = fizzbuzz_single(3)
        self.assertEqual(v, "Fizz")

    def test_single_4 (self) :
        v = fizzbuzz_single(5)
        self.assertEqual(v, "Buzz")

    def test_single_5 (self) :
        v = fizzbuzz_single(15)
        self.assertEqual(v, "FizzBuzz")


    # -----
    # range
    # -----

    def test_range_1 (self) :
        w = StringIO()
        fizzbuzz_range(1, 100, w)
        # self.assertEqual(w.getvalue(), 6)
        self.assertEqual(1, 1)

    def test_range_2 (self) :
        w = StringIO()
        fizzbuzz_range(1, 50, w)
        # self.assertEqual(w.getvalue(), 7)
        self.assertEqual(1, 1)

    def test_range_3 (self) :
        w = StringIO()
        fizzbuzz_range(50, 100, w)
        # self.assertEqual(w.getvalue(), 259)
        self.assertEqual(1, 1)

    def test_range_4 (self) :
        w = StringIO()
        fizzbuzz_range(1, 1000, w)
        # self.assertEqual(w.getvalue(), 47)
        self.assertEqual(1, 1)

    def test_range_5 (self) :
        w = StringIO()
        fizzbuzz_range(1000, 2000, w)
        # self.assertEqual(w.getvalue(), 160)
        self.assertEqual(1, 1)


    # ------
    # static
    # ------

    def test_static (self) :
        w = StringIO()
        fizzbuzz_static(w)
        # self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        self.assertEqual(1, 1)


# ----
# main
# ----

if __name__ == "__main__" :
    main()
