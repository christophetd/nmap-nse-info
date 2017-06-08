import argparse

# https://nmap.org/nsedoc/index.html
categories = [
    'auth',
    'broadcast',
    'brute',
    'default',
    'discovery',
    'dos',
    'exploit',
    'external',
    'fuzzer',
    'intrusive',
    'malware',
    'safe',
    'version',
    'vuln',
]

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '-l', '--nse-location',
    metavar = 'location',
    help = 'The location in which the NSE scripts are located',
    default = '/usr/share/nmap/scripts/',
    dest = 'nse_location'
)

parser.add_argument(
    '-c', '--category',
    metavar = 'category',
    help = 'Only show NSE scripts belonging to specific categories (OR matching).',
    choices = categories,
    default = [],
    action = 'append',
    dest = 'category_filter'
)

parser.add_argument(
    '--limit',
    metavar = 'limit',
    help = 'Limit the number of search results',
    default = 0,
    type = int
)

parser.add_argument(
    '--show-all',
    action = 'store_true',
    dest = 'show_all'
)

parser.add_argument(
    'action',
    help = 'The action to perform',
    choices = ['search', 'usage'],
    nargs = '?'
)

parser.add_argument(
    'search_query',
    help = 'Search query (or NSE script name depending on the action)',
    nargs = '?'
)