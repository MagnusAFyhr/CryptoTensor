#!/usr/bin/env python

"""
docstring:
"""

import pandas

import data.driver.data_builder as builder

"""

"""

db = builder.DataBuilder("TEST", "ETH", "USD")

df = db.read_data()
with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)
