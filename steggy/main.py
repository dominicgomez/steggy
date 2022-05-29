from command_line_parser import parser


def main(args):
    print(args)


if __name__ == '__main__':
    main(parser.parse_args())
