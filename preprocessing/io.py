""" IO

This file contains helper functions loading tracker data.

"""

import os
import json
from typing import Callable
import numpy
import pandas as pd
from tqdm import tqdm


def load_json_file_flatten(path: str) -> pd.DataFrame:
    """ Loads and flattens a possibly nested JSON file.

    Arguments:
        path:           the path of the JSON file
    """
    with open(path) as f:
        data = pd.io.json.json_normalize(json.loads("".join(f.readlines())))
    return data


def load_files(path: str, keyword: str, load_fn: Callable[[str], pd.DataFrame]) -> pd.DataFrame:
    """ Loads and concatenates multiple JSON files.

    Arguments:
        path:           the path of the directory containing the JSON files
        keyword:        filter keyword for filenames
        load_fn:        function to use for loading files
    """

    # Get all files with keyword in title
    filenames = list(filter(lambda name: keyword in name, os.listdir(path)))

    print("Loading files...")
    frames = [load_fn(os.path.join(path, name)) for name in tqdm(filenames)]

    print("%d files to concatenate." % len(frames))
    data = pd.concat(frames)
    print("Successfully concatenated.")

    data.reset_index(drop=True)

    return data
