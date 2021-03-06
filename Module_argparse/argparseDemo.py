import argparse

parser = argparse.ArgumentParser(description='Processs some integers.'
                                 epilog="A text description for the Demo")
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers(default: find the max)')
args = parser.parse_args()
print args.accumulate(args.integers)
