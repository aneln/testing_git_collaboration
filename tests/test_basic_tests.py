#!/usr/bin/env python3
"""
Basic tests using pytest

Created: March 2020
Author: p-robot
"""

import numpy as np

def test_summation():
    """
    test that 2-2 is zero
    """
    np.testing.assert_equal(2-2, 0)

def test_smth_else():
    """
    test that 2-3 is -1
    """
    np.testing.assert_equal(2-3, -1)



def test_string():
    """
    Test that strings are equivalent
    """
    np.testing.assert_equal("AB", "A" + "B")


def test_fail():
    """
    Illustration of a failing test
    """
    np.testing.assert_equal(9, 16)

def test_fail_another():
"""
Illustration of a failing test
"""
np.testing.assert_equal(2, 16)
