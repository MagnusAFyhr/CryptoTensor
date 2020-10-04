#!/usr/bin/env python

"""
docstring
"""

# imports
import re
import pandas

import parameters as params
import data.driver.ta_library as ta_library

_INDICATOR_ENCODING = "{}({})"
_INDICATOR_FORMAT = _INDICATOR_ENCODING.format(".*", ".*")


def calculate_technical_analysis(dataframe: pandas.DataFrame) -> pandas.DataFrame:

    indicators = _compile_technical_indicators()

    _load_technical_indicators(dataframe, indicators)

    return dataframe


def _compile_technical_indicators() -> list:
    """ Reformat and expand indicators defined in parameters. """

    technical_indicators = list([])

    # sanity check
    if not isinstance(params.TECHNICAL_INDICATORS, dict):
        raise Exception(f"failed to compile technical indicators; "
                        f"params.TECHNICAL_INDICATORS not of type 'dict'")

    for key, values in params.TECHNICAL_INDICATORS.items():
        if key not in ta_library.INDICATOR_FUNCTION_MAP:
            raise Exception(f"failed to compile technical indicators; "
                            f"unsupported indicator: {key}")
        else:
            if isinstance(values, list):
                if not values:
                    code = _INDICATOR_ENCODING.format(key, "")
                    technical_indicators.append(code)
                else:
                    for value in values:
                        if isinstance(value, int):
                            code = _INDICATOR_ENCODING.format(key, value)
                            technical_indicators.append(code)
                        elif isinstance(value, tuple):
                            value = (str(tup_val) for tup_val in value)
                            code = _INDICATOR_ENCODING.format(key, ",".join(value))
                            technical_indicators.append(code)
                        else:
                            raise Exception(f"failed to compile technical indicators; "
                                            f"invalid value in key-values: ({type(value)}){value}")
            else:
                raise Exception(f"failed to compile technical indicators; "
                                f"invalid key-value in params.TECHNICAL_INDICATORS: {values}")

    return technical_indicators


def _load_technical_indicators(data_frame: pandas.DataFrame, indicator_codes: list) -> None:
    """ Appends each indicator to the pandas data frame. """

    indicator_format = re.compile(_INDICATOR_FORMAT)
    for code in indicator_codes:

        # check format of indicator code
        if indicator_format.match(code) is None:
            raise Exception(f"failed to populate data frame; "
                            f"invalid indicator code, {code}")

        # process code
        indicator = code[:code.index("(")]
        args = code[code.index("(") + 1:len(code) - 1]
        args = args.split(",")
        temp_args = list([])
        for arg in args:
            if arg != "":
                temp_args.append(int(arg))
        args = temp_args

        # handle output
        try:
            output = _load_technical_indicator(data_frame, indicator, args)
            data_frame[code] = output
        except (IndexError, Exception) as err:
            raise Exception(f"failed to load indicator: {err})")

    return


def _load_technical_indicator(data_frame: pandas.DataFrame, indicator: str, args: list) -> pandas.Series:
    """ Tries to calculate and append the technical indicator values to the data frame. """

    # check if indicator is in function map
    if indicator not in ta_library.INDICATOR_FUNCTION_MAP:
        raise Exception(f"unsupported indicator; {indicator}")

    # attempt to calculate and append indicator
    try:
        return ta_library.INDICATOR_FUNCTION_MAP[indicator](data_frame, *args)
    except TypeError as err:
        raise Exception(f"{indicator}({args}); {err}")
