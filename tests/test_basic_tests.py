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
