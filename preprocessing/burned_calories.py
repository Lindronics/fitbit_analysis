""" Burned calories

This file contains helper functions for preprocessing burned calory data.

"""

import os
import pandas as pd

from preprocessing.io import load_json_file_flatten, load_files


def group_by_date(data: pd.DataFrame, column: str) -> pd.DataFrame:
    """ Groups a dataframe by date values of a column.

    Arguments:
        data:       dataframe to perform grouping on
        column:     column to group on
    """

    dates = [data[column].dt.date]
    grouped = data.groupby(dates, as_index=True).sum()
    grouped.reset_index(inplace=True)
    
    return grouped


def process_calories(path: str, out_path: str):
    """ Loads, processes and saves burned calory data.

    Arguments:
        path:       input path for data
        out_path:   output path for processed data
    """

    data = load_files(path, "calories", load_json_file_flatten)

    data["dateTime"] = pd.to_datetime(data.dateTime, format="%m/%d/%y %H:%M:%S")
    data["value"] = data["value"].astype("float")

    print("Grouping...")
    data = group_by_date(data, column='dateTime')

    print("Saving...")
    data.to_csv(path_or_buf=out_path)
    print("Saved to", out_path)
