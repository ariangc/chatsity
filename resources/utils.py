#!/usr/bin/env python

"""
    utils.py
    ----------
    This module contains utils for resources implementation.
"""

__author__ = "Arian Gallardo"

from password_strength import PasswordPolicy

password_policy = PasswordPolicy.from_names(
    length=5,  # min length: 5
    uppercase=1,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=1,  # need min. 1 special characters
    nonletters=0,  # need min. 0 non-letter characters (digits, specials, anything)
)
