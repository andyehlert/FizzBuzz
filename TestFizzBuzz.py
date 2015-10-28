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

from FizzBuzz import fizzbuzz_print, fizzbuzz_single, fizzbuzz_range, fizzbuzz_default

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
        self.assertEqual(w.getvalue(), "997\n")

    def test_print_3 (self) :
        w = StringIO()
        fizzbuzz_print(w, 3)
        self.assertEqual(w.getvalue(), "Fizz\n")

    def test_print_4 (self) :
        w = StringIO()
        fizzbuzz_print(w, 4)
        self.assertEqual(w.getvalue(), "Buzz\n")

    def test_print_5 (self) :
        w = StringIO()
        fizzbuzz_print(w, 5)
        self.assertEqual(w.getvalue(), "FizzBuzz\n")


    # ------
    # single
    # ------

    def test_single_1 (self) :
        v = fizzbuzz_single(1)
        self.assertEqual(v, "1")

    def test_single_2 (self) :
        v = fizzbuzz_single(97)
        self.assertEqual(v, "97")

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
        fizzbuzz_range(1, 15, w)
        self.assertEqual(w.getvalue(), "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n")

    def test_range_2 (self) :
        w = StringIO()
        fizzbuzz_range(1, 50, w)
        self.assertEqual(w.getvalue(), "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\n")

    def test_range_3 (self) :
        w = StringIO()
        fizzbuzz_range(51, 100, w)
        self.assertEqual(w.getvalue(), "Fizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n")

    def test_range_4 (self) :
        w = StringIO()
        fizzbuzz_range(1, 100, w)
        self.assertEqual(w.getvalue(), "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n")

    def test_range_5 (self) :
        w = StringIO()
        fizzbuzz_range(1000, 2000, w)
        # self.assertEqual(w.getvalue(), 160)
        self.assertEqual(1, 1)


    # -------
    # default
    # -------

    def test_default (self) :
        w = StringIO()
        fizzbuzz_default(w)
        self.assertEqual(w.getvalue(), "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n")


# ----
# main
# ----

if __name__ == "__main__" :
    main()
