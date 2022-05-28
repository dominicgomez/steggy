import argparse as argp


class CommandLineParser:
    @classmethod
    def _setup_parser(cls):
        par = argp.ArgumentParser(description=r'CLI steganography tool')
        par.add_argument('-f', '--force', help=r'overwrite existing files')
        par.add_argument('-l', '--license', help=r'show license info and quit')
        par.add_argument('-q', '--quiet', action='store_true', help=r'''
            suppress all output''')
        par.add_argument('-v', '--verbose', action='store_true', help=r'''
            display detailed output''')
        par.add_argument('-V', '--version', action='version', help=r'''
            show version info and quit''')
        subpars = par.add_subparsers(dest='subcmd')

        scan_par = subpars.add_parser('scan')
        scan_par.add_argument('suspect', type=argp.FileType('rb'), help=r'''
            examine a file''')

        embed_par = subpars.add_parser('embed')
        embed_par.add_argument('payload', type=argp.FileType('rb'), help='''
            the data to hide''')
        embed_par.add_argument('carrier', type=argp.FileType('rb'), help='''
            the data to conceal the payload within''')
        embed_par.add_argument('pkg', type=argp.FileType('wb'), help='''
            the created stegofile''')
        embed_par.add_argument('--compression', '-c', choices=[''], help='''
            none doe''')

        extract_par = subpars.add_parser('extract')
        extract_par.add_argument('pkg', type=argp.FileType('rb'), help=r'''
            ''')

        return par

    @classmethod
    def parse_args(cls, args):
        cls.parser.parse_args(args)


parser = CommandLineParser._setup_parser()
