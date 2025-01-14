import argparse
import logging

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser("Print challenge details")
parser.add_argument("--mode", required=True, help="Challenge name")
parser.add_argument("--dataset", required=True, help="Dataset JSON")
args = parser.parse_args()

