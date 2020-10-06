#!/usr/bin/env python

"""
docstring: A class used to standardize and isolate the interaction with, and retrieval of,
        input data used for the machine learning model.

DataBook:
    __init__()      :
    _fetch_data()   : DONE
    _parse_data()   : DONE
    _verify()       :

"""

# imports
import os

import pandas

_INPUT_DATA_PATH = os.getcwd() + "/data/library/input/full/{}"
_INPUT_DATA_TITLE = "{}_{}_{}_full.csv"


class DataBook:

    def __init__(self, exchange: str,
                 base_coin: str, quote_coin: str,
                 train_period: int,
                 use_hourly_data=True):
        """ Initializes elaborated table data from locally stored historical, technical analysis csv files. """

        self._exchange = exchange
        self._base_coin = base_coin
        self._quote_coin = quote_coin
        self._symbol = base_coin + quote_coin
        self._train_period = train_period

        self._timeperiod = "1h"
        if not use_hourly_data:
            self._timeperiod = "1d"

        # obtain data
        self._full_df = self._fetch_data()

        # divide into training and testing sets
        self._train_df, self._test_df = self._parse_data()

        # verify initialization
        self._verify()

        return

    def _fetch_data(self) -> pandas.DataFrame:
        """ Fetches locally stored technical analysis data and loads it as a pandas data frame. """

        # generate file paths to locally stored 'full' data
        data_title = _FULL_INPUT_DATA_TITLE.format(self._exchange, self._symbol, self._timeperiod)
        file_path = _FULL_INPUT_DATA_PATH.format(data_title)

        # check that the full csv files exist
        if not (os.path.isfile(file_path)):
            raise Exception(f"failed to build DataBook; full data does not exist!\n"
                            f"{file_path} not found in library; try building the full dataframe first.")

        # load csv as pandas df
        df = pandas.read_csv(file_path)

        return df

    def _parse_data(self) -> (pandas.DataFrame, pandas.DataFrame):
        """ Split full data into a training set and a testing set;
        to be used by the machine learning algorithm. """
        train_df = self._full_df.iloc[:, :self._train_period]
        test_df = self._full_df.iloc[:, self._train_period:]

        return train_df, test_df

    def _verify(self):
        """ Verify the class initialization:
            - full data, training data & testing data for length, NaNs, etc.
        """
        pass

    """
    Return copy of data
    """
    def read_data(self):
        return self._full_df
