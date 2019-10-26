""" Food

This file contains functions for loading and processing food logs.

"""

import pandas as pd

from preprocessing.io import load_files


def get_logs(path):
    food_logs = load_files(path, "food_logs")
    keep_columns = {
        "logDate": "dateTime",
        "nutritionalValues.calories": "calories",
        "nutritionalValues.carbs": "carbs",
        "nutritionalValues.fat": "fat",
        "nutritionalValues.fiber": "fiber",
        "nutritionalValues.protein": "protein",
        "nutritionalValues.sodium": "sodium"
    }
    food_logs = food_logs[keep_columns.keys()].rename(columns=keep_columns)
    food_logs["dateTime"] = pd.to_datetime(food_logs.dateTime, format="%Y-%m-%d")
    return food_logs
    
