import pandas as pd
import requests

STOOQ_URL = 'http://stooq.com/q/l/?s='

def process_stock(stock_code):
    host = STOOQ_URL + stock_code

    r = requests.get(
        STOOQ_URL + stock_code, 
        allow_redirects = True
    )

    row = r.content.decode('ascii').split(sep = ",")

    print(row)
    return "{} quote is ${} per share".format(row[0], row[3])