import os
from sys import stderr
from nseinfo.parsing.NseScriptParser import NseScriptParser
from nseinfo.parsing.NseParsingException import NseParsingException


def do_usage(args):
    try:
        path = os.path.join(args.nse_location, args.search_query + '.nse')
        with open(path) as f:
            try:
                script = NseScriptParser().parse(args.search_query, f.read())
            except NseParsingException as e:
                stderr.write('Unable to parse NSE script {}: {}\n'.format(path, e.message))
                exit(1)
    except IOError as e:
        stderr.write('Unable to find NSE script "{}" in {}\n'.format(args.search_query, args.nse_location))
        exit(1)


    print ''
    print '{}: {}\n'.format(args.search_query, script.short_description)
    num_usages = len(script.sample_usages)
    if num_usages == 0:
        print 'No sample usage found for script "{}".'.format(args.search_query)
    else:
        print '{} sample usage{} found:'.format(num_usages, 's' if num_usages > 1 else '')
        print ''
        sep = ' '
        print sep + ('\n'+sep).join(script.sample_usages)
        print ''

    print 'Run "nmap --script {} --help" for more information.'.format(args.search_query)