#!/usr/bin/env python

"""
docstring:
"""

import pandas

import data.driver.databook as databook

"""

"""

db = databook.DataBook("Kraken", "ETH", "USD")

df = db.read_data()
with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)
