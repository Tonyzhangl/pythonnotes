import argparse

parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
parser.add_argument('+f')
parser.add_argument('++bar')
parser.parse_args('+f X ++bar Y'.split())
#The prefix_chars= argument defaults to '-'. Supplying a set of characters that does not include - will cause -f/--foo options to be disallowed.
