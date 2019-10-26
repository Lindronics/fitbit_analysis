""" Get burned calories

This file is an easy command line program to pre-process calory data.
"""

import argparse
from time import time

from preprocessing.calories import preprocess_burned_calories


parser = argparse.ArgumentParser(description="Convert minutely to daily calory data.")
parser.add_argument("path")
parser.add_argument("out_path")
args = vars(parser.parse_args())

t0 = time()
preprocess_burned_calories(**args)
print(f"Elapsed: {time()-t0}s")