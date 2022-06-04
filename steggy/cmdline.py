import argparse as arg


def parse(args):
    par = arg.ArgumentParser(add_help=False)
    par.add_argument('-l', '--license', help='show license info and exit')
    par.add_argument(
        '-v', '--verbose', action='store_true', help='show detailed output')

    subpars = par.add_subparsers(title='sub-commands', dest='subcmd')

    scan_par = subpars.add_parser(
        'scan', parents=[par],
        help='detect whether a file is a stegofile created with steggy')
    scan_par.add_argument(
        'suspect', type=arg.FileType('rb'),
        help='the file suspected of being a steggy stegofile')

    embed_par = subpars.add_parser(
        'embed', parents=[par], help='embed a payload in a carrier')
    embed_par.add_argument(
        'payload', type=arg.FileType('rb'),
        help='the data to covertly communicate')
    embed_par.add_argument(
        'carrier', help='data to hide the payload')
    embed_par.add_argument(
        'stegofile', type=arg.FileType('wb'),
        help='the created file containing the payload')

    extract_par = subpars.add_parser(
        'extract', parents=[par], help='extract a payload from a stegofile')
    extract_par.add_argument(
        'stegofile', help='the file containing an embedded payload')
    extract_par.add_argument(
        'payload', type=arg.FileType('wb'),
        help='the data covertly communicated')

    return par.parse_args(args)
