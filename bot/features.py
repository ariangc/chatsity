#!/usr/bin/env python

"""
      features.py
      ----------
      This module contains the principal implemented features of the decoupled
      bot to process financial information.
"""

__author__ = "Arian Gallardo"

import pandas as pd
import requests

STOOQ_URL = 'http://stooq.com/q/l/?s='

def process_stock(stock_code):
    """ Calls an external API to get a CSV file to be parsed. Then, retrieves
        relevant information about such file.

        :type stock_code: str
        :param stock_code: Stock code to be analyzed.
    """
    host = STOOQ_URL + stock_code

    r = requests.get(
        STOOQ_URL + stock_code, 
        allow_redirects = True
    )
    row = r.content.decode('ascii').split(sep = ",")
    return "{} quote is ${} per share".format(row[0], row[5])