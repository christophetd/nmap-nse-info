#!/usr/bin/env python

import os
from sys import stderr
from actions import search, usage
import cli

def main():
    args = cli.parser.parse_args()
    if not os.path.isdir(args.nse_location):
        stderr.write('Invalid NSE scripts location: {}\n'.format(args.nse_location))
        exit(1)

    if args.show_all:
        search.do_show_all(args)
    elif args.action == 'search' and args.search_query:
        search.do_search(args)

    elif args.action == 'usage' and args.search_query:
        usage.do_usage(args)
    else:
        cli.parser.print_help()