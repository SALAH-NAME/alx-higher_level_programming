#!/usr/bin/python3
"""
This module contains a fun that mul two matrices using the NumPy module.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of the multiplication.
    """
    return np.dot(m_a, m_b)
