#!/usr/bin/env python

"""
docstring:
"""

import pandas

import data.driver.databook as databook

"""

"""

db = databook.DataBook("TEST", "ETH", "USD")

df = db.read_data()
with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)

# saving the dataframe
df.to_csv("test_data.csv")
