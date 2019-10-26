""" Calories

This file contains helper functions for working with calory data.

"""

import os
import pandas as pd

from preprocessing.io import load_json_file_flatten, load_files
from preprocessing.utils import group_by_date
from preprocessing import food


def get_burned_calories(path: str) -> pd.DataFrame:
    """ Loads and pre-processes burned calory data.

    Arguments:
        path:       input path for data (usually "[...]/user-site-export")
    """
    data = load_files(path, "calories")

    data["dateTime"] = pd.to_datetime(data.dateTime, format="%m/%d/%y %H:%M:%S")
    data["value"] = data["value"].astype("float")

    print("Grouping...")
    data = group_by_date(data, column='dateTime')
    data = data.rename(columns={"value": "burned"})
    return data


def preprocess_burned_calories(path: str, out_path: str):
    """ Loads, processes and saves burned calory data.

    Pre-processing and saving the data might be desirable due to the
    large amount of data and the resulting computation times.

    Arguments:
        path:       input path for data (usually "[...]/user-site-export")
        out_path:   output path for processed data
    """
    data = get_burned_calories(path)

    data = data.set_index("dateTime")

    print("Saving...")
    data.to_csv(path_or_buf=out_path)

    print("Saved to", out_path)


def calory_difference(path: str, preprocessed_path: str = None) -> pd.DataFrame:
    """ Calculates calory difference based on food logs and burned calory data.

    Arguments:
        path:               input path for data (usually "[...]/user-site-export")
        preprocessed_path:  input path for preprocessed burned calory data 
                            (if not provided, falls back to loading and pre-processing raw data)

    Returns:
        a pandas dataframe with columns for burned calories, consumed calories,
        and the difference consumed - burned
    """
    consumed = food.get_logs(path)
    consumed = consumed[["dateTime", "calories"]]
    consumed = group_by_date(consumed, "dateTime")
    consumed = consumed.set_index("dateTime")

    burned = pd.read_csv(preprocessed_path) \
        if preprocessed_path \
        else get_burned_calories(path)

    burned["dateTime"] = pd.to_datetime(burned.dateTime, format="%Y-%m-%d")
    burned = burned.set_index("dateTime")

    # Join eaten and burned calories and calculate difference
    total = burned.join(consumed, how="inner")
    total = total.rename(columns={"calories":"consumed"})
    total["difference"] = total["consumed"] - total["burned"]

    return total
    
