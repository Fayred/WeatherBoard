import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true", help="enable debug mode (not about flask)")
parser.add_argument("-D", "--deploy", action="store_true", help="enable connection to dashboard from other device in local network")
arguments = parser.parse_args()