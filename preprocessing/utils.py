""" Utils

This file contains general helper functions for pre-processing.

"""

import pandas as pd


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

