import argparse
parent_parser = argparse.ArgumentParser(add_help=False)
# most parent parsers will specify add_help = False
parent_parser.add_argument('--parent', type=int)

foo_parser = argparse.ArgumentParser(parents=[parent_parser])
foo_parser.add_argument('foo')
foo_parser.parse_args(['--parent', '2', 'xxx'])

bar_parser = argparse.ArgumentParser(parents=[parent_parser])
bar_parser.add_argument('--bar')
bar_parser.parse_args(['--parent', 'yyy'])
