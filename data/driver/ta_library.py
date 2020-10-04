#!/usr/bin/env python

"""
docstring:

credit: https://mrjbq7.github.io/ta-lib/doc_index.html
"""

# imports
import pandas
import talib as ta

""" 
Volume Indicators 
"""


def AD(data_frame: pandas.DataFrame):
    """ Chaikin A/D Line

    :param data_frame: pandas data frame containing OHLCV columns

    """
    return ta.AD(data_frame.High.values,
                 data_frame.Low.values,
                 data_frame.Close.values,
                 data_frame.Volume.values)


def ADOSC(data_frame: pandas.DataFrame,
          fast_period: int = 3,
          slow_period: int = 10):
    """ Chaikin A/D Oscillator

    :param data_frame: pandas data frame containing OHLCV columns
    :param fast_period:
    :param slow_period:

    """
    return ta.ADOSC(data_frame.High.values,
                    data_frame.Low.values,
                    data_frame.Close.values,
                    data_frame.Volume.values.astype(float),
                    fast_period,
                    slow_period)


def OBV(data_frame: pandas.DataFrame):
    """ On Balance Volume

    :param data_frame: pandas data frame containing OHLCV columns

    """
    return ta.OBV(data_frame.Close.values,
                  data_frame.Volume.values.astype(float))


""" 
Momentum Indicators 
"""


def ADX(data_frame: pandas.DataFrame,
        timeperiod: int = 14):
    """ Average Directional Index
    info : https://www.investopedia.com/articles/trading/07/adx-trend-indicator.asp

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.ADX(data_frame.High.values,
                  data_frame.Low.values,
                  data_frame.Close.values,
                  timeperiod)


def ADXR(data_frame: pandas.DataFrame,
         timeperiod: int = 14):
    """ Average Directional Movement Index Rating
    info : https://www.marketvolume.com/technicalanalysis/adxr.asp

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.ADXR(data_frame.High.values,
                   data_frame.Low.values,
                   data_frame.Close.values,
                   timeperiod)


def APO(data_frame: pandas.DataFrame,
        fast_period: int = 12,
        slow_period: int = 26,
        ma_type: int = 0):
    """ Absolute Price Oscillator
    info : https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/apo

    :param data_frame: pandas data frame containing OHLCV columns
    :param fast_period:
    :param slow_period:
    :param ma_type:

    """
    return ta.APO(data_frame.Close.values,
                  fast_period,
                  slow_period,
                  ma_type)


def BOP(data_frame: pandas.DataFrame):
    """ Balance Of Power

    :param data_frame: pandas data frame containing OHLCV columns

    """
    return ta.BOP(data_frame.Open.values,
                  data_frame.High.values,
                  data_frame.Low.values,
                  data_frame.Close.values)


def CCI(data_frame: pandas.DataFrame,
        timeperiod: int = 14):
    """ Commodity Channel Index

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.CCI(data_frame.High.values,
                  data_frame.Low.values,
                  data_frame.Close.values,
                  timeperiod)


def CMO(data_frame: pandas.DataFrame,
        timeperiod: int = 14):
    """ Chande Momentum Oscillator
    info : https://tradingsim.com/blog/chande-momentum-oscillator-cmo-technical-indicator/

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.CMO(data_frame.Close.values,
                  timeperiod)


def DX(data_frame: pandas.DataFrame,
       timeperiod: int = 14):
    """ Directional Index

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.DX(data_frame.High.values,
                 data_frame.Low.values,
                 data_frame.Close.values,
                 timeperiod)


def MFI(data_frame: pandas.DataFrame,
        timeperiod: int = 14):
    """ Money Flow Index
    info : https://www.investopedia.com/terms/m/mfi.asp

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:
    :return:
    """
    return ta.MFI(data_frame.High.values,
                  data_frame.Low.values,
                  data_frame.Close.values,
                  data_frame.Volume.values.astype(float),
                  timeperiod)


def MINUS_DI(data_frame: pandas.DataFrame,
             timeperiod: int = 14):
    """ Minus Directional Indicator

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.MINUS_DI(data_frame.High.values,
                       data_frame.Low.values,
                       data_frame.Close.values,
                       timeperiod)


def MINUS_DM(data_frame: pandas.DataFrame,
             timeperiod: int = 14):
    """ Minus Directional Movement

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.MINUS_DM(data_frame.High.values,
                       data_frame.Low.values,
                       timeperiod)


def MOM(data_frame: pandas.DataFrame,
        timeperiod: int = 14):
    """ Momentum

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.MOM(data_frame.Close.values,
                  timeperiod)


def PLUS_DI(data_frame: pandas.DataFrame,
            timeperiod: int = 14):
    """ Plus Directional Indicator

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.PLUS_DI(data_frame.High.values,
                      data_frame.Low.values,
                      data_frame.Close.values,
                      timeperiod)


def PLUS_DM(data_frame: pandas.DataFrame,
            timeperiod: int = 14):
    """ Plus Directional Movement

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.PLUS_DM(data_frame.High.values,
                      data_frame.Low.values,
                      timeperiod)


def PPO(data_frame: pandas.DataFrame,
        fast_period: int = 12,
        slow_period: int = 26,
        ma_type: int = 0):
    """ Percentage Price Oscillator

    :param data_frame: pandas data frame containing OHLCV columns
    :param fast_period:
    :param slow_period:
    :param ma_type:

    """
    return ta.PPO(data_frame.Close.values,
                  fast_period,
                  slow_period,
                  ma_type)


def ROC(data_frame: pandas.DataFrame,
        timeperiod: int = 14):
    """ Rate Of Change
    info : https://www.investopedia.com/terms/p/pricerateofchange.asp

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.ROC(data_frame.Close.values,
                  timeperiod)


def RSI(data_frame: pandas.DataFrame,
        timeperiod: int = 14):
    """ Relative Strength Index
    info : https://www.investopedia.com/terms/r/rsi.asp

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.RSI(data_frame.Close.values,
                  timeperiod)


def TRIX(data_frame: pandas.DataFrame,
         timeperiod: int = 14):
    """ 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    info : https://school.stockcharts.com/doku.php?id=technical_indicators:trix

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.TRIX(data_frame.Close.values,
                   timeperiod)


def ULTOSC(data_frame: pandas.DataFrame,
           timeperiod1: int = 7,
           timeperiod2: int = 14,
           timeperiod3: int = 28):
    """ Ultimate Oscillator
    info : https://school.stockcharts.com/doku.php?id=technical_indicators:ultimate_oscillator

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod1:
    :param timeperiod2:
    :param timeperiod3:

    """
    return ta.ULTOSC(data_frame.High.values,
                     data_frame.Low.values,
                     data_frame.Close.values,
                     timeperiod1,
                     timeperiod2,
                     timeperiod3)


def WILLR(data_frame: pandas.DataFrame,
          timeperiod: int = 14):
    """ Williams' %R

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.WILLR(data_frame.High.values,
                    data_frame.Low.values,
                    data_frame.Close.values,
                    timeperiod)


""" 
Overlap Studies
"""


def DEMA(data_frame: pandas.DataFrame,
         timeperiod: int = 30):
    """ Double Exponential Moving Average

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.DEMA(data_frame.Close.values,
                   timeperiod)


def EMA(data_frame: pandas.DataFrame,
        timeperiod: int = 14):
    """ Exponential Moving Average

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.EMA(data_frame.Close.values,
                  timeperiod)


def KAMA(data_frame: pandas.DataFrame,
         timeperiod: int = 30):
    """ Kaufman Adaptive Moving Average

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.KAMA(data_frame.Close.values,
                   timeperiod)


def SAR(raw_df):
    """ Parabolic SAR """
    return ta.SAR(raw_df.High.values,
                  raw_df.Low.values)


def SMA(data_frame: pandas.DataFrame,
        timeperiod: int = 14):
    """ Simple Moving Average

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.SMA(data_frame.Close.values,
                  timeperiod)


def TEMA(data_frame: pandas.DataFrame,
         timeperiod: int = 30):
    """ Triple Exponential Moving Average

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.TEMA(data_frame.Close.values,
                   timeperiod)


def TRIMA(data_frame: pandas.DataFrame,
          timeperiod: int = 30):
    """ Triangular Moving Average

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.TRIMA(data_frame.Close.values,
                    timeperiod)


def WMA(data_frame: pandas.DataFrame,
        timeperiod: int = 30):
    """  Weighted Moving Average

    :param data_frame: pandas data frame containing OHLCV columns
    :param timeperiod:

    """
    return ta.WMA(data_frame.Close.values,
                  timeperiod)


INDICATOR_FUNCTION_MAP = {

    "AD": AD,
    "ADOSC": ADOSC,
    "OBV": OBV,

    "ADX": ADX,
    "ADXR": ADXR,
    "APO": APO,
    "BOP": BOP,
    "CCI": CCI,
    "CMO": CMO,
    "DX": DX,
    "MFI": MFI,
    "MINUS_DI": MINUS_DI,
    "MINUS_DM": MINUS_DM,
    "MOM": MOM,
    "PLUS_DI": PLUS_DI,
    "PLUS_DM": PLUS_DM,
    "PPO": PPO,
    "ROC": ROC,
    "RSI": RSI,
    "TRIX": TRIX,
    "ULTOSC": ULTOSC,
    "WILLR": WILLR,

    "DEMA": DEMA,
    "EMA": EMA,
    "KAMA": KAMA,
    "SAR": SAR,
    "SMA": SMA,
    "TEMA": TEMA,
    "TRIMA": TRIMA,
    "WMA": WMA,

}