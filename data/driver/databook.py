#!/usr/bin/env python

"""
docstring: DataBook

DataBook:
    __init__()      :
    _fetch_data()   : DONE
    _load_data()    :
    _parse_data()   :
    _verify()       :

"""

# imports
import os

import pandas

import data.driver.data_dilator as dilator

_INIT_DATA_PATH = os.getcwd() + "/data/library/{}"
_INIT_DATA_TITLE = "{}_{}_{}.csv"

_REQUIRED_CSV_FIELDS = [
    'Unix Timestamp',
    'Date',
    'Symbol',
    'Open',
    'High',
    'Low',
    'Close',
    'Volume'
]

_FIB_PERIODS = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]


class DataBook:

    """
    Initializes elaborated table data from locally stored historical, OHLCV csv files
    """
    def __init__(self, exchange: str, base_coin: str, quote_coin: str, use_hourly_data=True):

        self._exchange = exchange
        self._base_coin = base_coin
        self._quote_coin = quote_coin
        self._symbol = base_coin + quote_coin
        self._timeperiod = "1d"
        if use_hourly_data:
            self._timeperiod = "1h"

        # fetch initial data
        self._init_data = self._fetch_data()

        # populate with technical analysis
        self._full_data = self._load_data()

        # divide into training and testing sets
        self._train_data, self._test_data = 0, 0  # self._parse_data()

        # verify initialization

        pass

    def _fetch_data(self) -> pandas.DataFrame:
        """ Builds and populates a pandas data frame using local ticker CSV data. """

        # generate file paths to locally stored data
        data_title = _INIT_DATA_TITLE.format(self._exchange, self._symbol, self._timeperiod)
        file_path = _INIT_DATA_PATH.format(data_title)

        # check that csv files exist
        if not (os.path.isfile(file_path)):
            raise Exception(f"failed to build DataBook; "
                            f"{self._exchange}_{self._symbol}_{self._timeperiod}.csv not found in library")

        # load csv as pandas df
        df = pandas.read_csv(file_path)

        # correct volume columns to single column using quote currency
        del df[f'Volume {self._base_coin}']
        df = df.rename(columns={f'Volume {self._quote_coin}': 'Volume'})

        # check that all required fields are present
        for req_field in _REQUIRED_CSV_FIELDS:
            if req_field not in df:
                raise Exception(f"failed to build DataBook; "
                                f"invalid input csv data, "
                                f"missing required field: {req_field}")

        return df

    def _load_data(self) -> pandas.DataFrame:
        """ Use initial dataframe to populate a full dataframe;
        with technical analysis across all fibonacci time periods. """

        # make empty data frame
        full_df = pandas.DataFrame()

        for timeperiod in _FIB_PERIODS:
            print(f"Processing timeperiod : {timeperiod}")
            dilated_df = dilator.dilate_data(self._init_data.copy(), timeperiod)
            if full_df.empty:
                full_df = dilated_df.copy()
            else:
                full_df = pandas.merge(full_df, dilated_df, on='Unix Timestamp')

        return full_df

    def _parse_data(self) -> (pandas.DataFrame, pandas.DataFrame):
        """ Split full data into a training set and a testing set;
        to be used by the machine learning algorithm. """
        return

    def _verify(self):
        """ Verify the """
        pass

    """
    Return copy of data
    """
    def read_data(self):
        return self._full_data
