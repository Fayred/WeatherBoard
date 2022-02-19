import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true", help="enable debug mode (not about flask)")
arguments = parser.parse_args()