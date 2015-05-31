#!/usr/bin/env python3

# Testing Python's  Standard Library
#
# Test list:
#
# \fn average(values)
# \test doctest: unit testing within docstrings
#
# \fn def multiply(a, b):
# \test unittest: testing with unittest from a separate file
#


##==============================================================================


##==============================================================================
# \fn average(values)
# \test doctest: unit testing within docstrings
#
# a) Use on interactive mode:
#
# >>> import doctest
# >>> doctest.testmod(standard_lib)
#
# success output:
# TestResults(failed=0, attempted=1)
#
# On error:
#
# Failed example:
#     print(average([20, 30, 70]))
# Expected:
#     41.0
# Got:
#     40.0
# **********************************************************************
# 1 items had failures:
#    1 of   1 in standard_lib.average
# ***Test Failed*** 1 failures.
# TestResults(failed=1, attempted=1)
#
#
#
# b) Use from shell
#
# >>> python3 -m doctest -v standard_lib.py
# On success: no output
# On error:
# 1 items had failures:
#    1 of   1 in standard_lib.average
# ***Test Failed*** 1 failures.

##==============================================================================

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))  # copy-paste the call & the result here
    41.0
    """

    return sum(values) / len(values)


##==============================================================================
# \fn def multiply(a, b):
# \test unittest: testing with unittest from a separate file
##==============================================================================


def multiply(a, b):
    return a * b


