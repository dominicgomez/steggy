"""Define steggy's valid command-line opts, args, and sub-commands.

"""
import argparse


parser = argparse.ArgumentParser(description='CLI steganography tool')

parser.add_argument(
    '-f', '--force',
    help='overwrite existing files'
)
parser.add_argument(
    '-l', '--license',
    help='show license info and quit'
)
parser.add_argument(
    '-q', '--quiet',
    action='store_true',
    help='suppress all output'
)
parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    help='display detailed output'
)
parser.add_argument(
    '-V', '--version',
    action='version',
    version='0.0.0',
    help='show version info and quit'
)

subparsers = parser.add_subparsers(dest='subcmd')

scan_parser = subparsers.add_parser('scan')
scan_parser.add_argument(
    'suspect',
    type=argparse.FileType('rb'),
    help='examine a file'
)

embed_parser = subparsers.add_parser('embed')
embed_parser.add_argument(
    'payload',
    type=argparse.FileType('rb'),
    help='the data to hide')
embed_parser.add_argument(
    'carrier',
    type=argparse.FileType('rb'),
    help='the data to conceal the payload within'
)
embed_parser.add_argument(
    'stegofile',
    type=argparse.FileType('wb'),
    help='the created stegofile'
)

extract_parser = subparsers.add_parser('extract')
extract_parser.add_argument(
    'stegofile',
    type=argparse.FileType('rb'),
    help=''
)
extract_parser.add_argument(
    'payload',
    type=argparse.FileType('wb'),
    help=''
)
