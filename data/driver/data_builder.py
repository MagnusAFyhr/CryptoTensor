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
import time

import data.driver.data_dilator as dilator

_INIT_DATA_PATH = os.getcwd() + "/data/library/input/{}"
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

"""
 REMOVE ALL NANS FROM DATAFRAME

"""


class DataBuilder:
    """
    Initializes elaborated table data from locally stored historical, OHLCV csv files
    """

    def __init__(self, exchange: str, base_coin: str, quote_coin: str, use_hourly_data=True):

        self._exchange = exchange
        self._base_coin = base_coin
        self._quote_coin = quote_coin
        self._symbol = base_coin + quote_coin
        self._timeperiod = "1h"
        if not use_hourly_data:
            self._timeperiod = "1d"

        # fetch initial data
        self._init_data = self._fetch_data()

        # populate with technical analysis
        self._full_data = self._load_data()

        # save data to csv in library
        self._full_data.to_csv(_INIT_DATA_PATH.format(f"{self._exchange}_{self._symbol}_{self._timeperiod}_full.csv"),
                               index=False)

        # verify initialization
        self._verify()

        # provide some feedback

        # exit
        exit(0)

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

        # set up some timing mechanisms
        start = time.time_ns()
        buffer = 0
        index = 0
        length = float(len(_FIB_PERIODS))

        for timeperiod in _FIB_PERIODS:
            dilated_df = dilator.dilate_data(self._init_data.copy(), timeperiod)
            if full_df.empty:
                full_df = dilated_df.copy()
            else:
                del dilated_df[f"[{timeperiod}]Date"]
                del dilated_df[f"[{timeperiod}]Symbol"]
                full_df = pandas.merge(full_df, dilated_df, on='Unix Timestamp')

            # update timer
            index += 1
            end = time.time_ns()
            elapsed = end - start
            elapsed /= pow(10, 9)
            if elapsed - buffer >= 1:
                buffer += 1
                percent_done = (index / length)
                time_left = round(elapsed / percent_done, 2)
                print(f"Estimated {time_left} seconds until completion;"
                      f"processed {index}/{length} timeperiods.")

        # delete NaN values
        full_df = full_df.dropna(axis=0, how='any')

        return full_df

    def _verify(self):
        """ Verify the """
        pass

    """
    Return copy of data
    """

    def read_data(self):
        return self._full_data
