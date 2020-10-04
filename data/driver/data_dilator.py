#!/usr/bin/env python

"""
docstring: expands a single OHLCV data set into fibonacci time periods (1,2,3,5...) with custom technical analysis
"""

# imports

import pandas

import data.driver.data_calculator as calc

"""     !   !   !
        USE TRAILING MOVING AVERAGES FOR TIME PERIODS GREATER THAN AS TO AVOID EMPTY CELLS
"""

_INDICATOR_ENCODING = "{}({})"
_INDICATOR_FORMAT = _INDICATOR_ENCODING.format(".*", ".*")


def dilate_data(dataframe: pandas.DataFrame, timeperiod: int = 1) -> pandas.DataFrame:
    # form new OHLCV, if necessary (timeperiod > 1)
    updated_ohlcv_df = _form_new_ohlcv(dataframe, timeperiod)

    # calculate and append technical analysis to ohlcv
    dilated_df = calc.calculate_technical_analysis(updated_ohlcv_df)

    # rename all columns to add timeperiod to head of column name
    updated_column_names = list([])
    column_names = list(dilated_df.columns.values)
    for column_name in column_names:
        if column_name is not "Unix Timestamp":
            updated_column_names.append(f"[{timeperiod}]{column_name}")
        else:
            updated_column_names.append("Unix Timestamp")
    dilated_df.columns = updated_column_names

    # return populated data frame
    return dilated_df


def _form_new_ohlcv(dataframe: pandas.DataFrame, timeperiod: int) -> pandas.DataFrame:
    # create a new pandas data frame
    new_df = pandas.DataFrame(columns=[
        'Unix Timestamp',
        'Date',
        'Symbol',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume'])
    # create a temporary dataframe to hold rows used in multiple period OHLCV aggregation
    temp_df = pandas.DataFrame(columns=[
        'Unix Timestamp',
        'Date',
        'Symbol',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume'])

    # for each row of original data
    index = 0
    for _, row in dataframe.iterrows():
        temp_df = temp_df.append(row, ignore_index=True)

        if index % 100 == 0:
            print(index)
        index += 1

        if len(temp_df.index) == timeperiod:
            #       perform calculations...
            unix_timestamp = temp_df['Unix Timestamp'][timeperiod-1]
            date = "Date"  # f"{temp_df['Date'][0]}-{temp_df['Date'][-1]}"
            symbol = temp_df['Symbol'][0]
            open_ = temp_df['Open'][0]
            high = temp_df['High'].max()
            low = temp_df['Low'].min()
            close = temp_df['Close'][timeperiod-1]
            volume = sum(temp_df['Volume'])

            # make a new row
            new_row_data = {
                'Unix Timestamp': unix_timestamp,
                'Date': date,
                'Symbol': symbol,
                'Open': open_,
                'High': high,
                'Low': low,
                'Close': close,
                'Volume': volume,
            }
            # append row to new_df
            new_df = new_df.append(new_row_data, ignore_index=True)
            # drop oldest
            temp_df = temp_df[1:]
            temp_df = temp_df.reset_index(drop=True)
        else:
            empty_row_data = {
                'Unix Timestamp': row['Unix Timestamp'],
                'Date': None,
                'Symbol': None,
                'Open': None,
                'High': None,
                'Low': None,
                'Close': None,
                'Volume': None,
            }
            new_df = new_df.append(empty_row_data, ignore_index=True)

    return new_df
