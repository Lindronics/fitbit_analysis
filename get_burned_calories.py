""" Get burned calories

This file is an easy command line program to pre-process calory data.
"""

import argparse
from time import time

from preprocessing.burned_calories import process_calories


parser = argparse.ArgumentParser(description="Convert minutely to daily calory data.")
parser.add_argument("path")
parser.add_argument("out_path")
args = vars(parser.parse_args())

t0 = time()
process_calories(**args)
print(f"Elapsed: {time()-t0}s")