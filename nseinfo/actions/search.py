import os
import re
import prettytable

from sys import stderr
from glob import glob
from nseinfo.parsing.NseScriptParser import NseScriptParser

COLOR_RED= '\033[91m'
COLOR_RESET = '\033[0m'
COLOR_BOLD = '\033[1m'

CATEGORY_SHOW_ALL = 'show scripts from all categories'

def build_nse_scripts_list(args):
    nse_scripts = glob(args.nse_location + '/*.nse')
    if len(nse_scripts) == 0:
        stderr.write('There does not seem to be any NSE script in {}\n'.format(args.nse_location))

    scripts = []
    parser = NseScriptParser()

    for nse_script_file in nse_scripts:
        with open(nse_script_file, 'r') as file:
            try:
                parsed_script = parser.parse(os.path.basename(nse_script_file), file.read())
                scripts.append(parsed_script)
            except Exception as e:
                stderr.write('Unable to parse NSE file {}: {}\n'.format(nse_script_file, e.message))
                exit(1)

    return scripts

def get_script_score(script, query):
    score = 0
    keywords = re.compile("\s*").split(query)
    for keyword in keywords:
        if keyword.lower() in script.name:
            score += 4

        if keyword.lower() in script.short_description.lower():
            score += 2
        elif keyword.lower() in script.full_description.lower():
            score += 1

    return score

def rank_nse_scripts(scripts, query):
    # Keep a list of scripts with their ranking
    rankings = []
    for script in scripts:
        score = get_script_score(script, query)
        if score > 0:
            rankings.append( (script, score) )

    return sorted(rankings, reverse = True, key = lambda el: el[1])


def get_displayable_description(description):
    MAX_COL_LEN = 60
    words = re.compile("\s*").split(description)
    parts = [""]
    curr_part = 0

    for word in words:
        if len(parts[curr_part] + word) <= MAX_COL_LEN:
            parts[curr_part] += word + " "
        else:
            parts.append(word+" ")
            curr_part += 1

    return "\n ".join(parts)

def color_matches(str, query):
    if query is None or len(query.strip()) is 0:
        return str

    keywords = re.compile("\s*").split(query)
    for keyword in keywords:
        regxp = re.compile("("+re.escape(keyword)+")", re.IGNORECASE)
        str = regxp.sub(COLOR_RED + COLOR_BOLD + "\\1" + COLOR_RESET, str)

    return str

def print_result(args, matched_scripts):
    query = args.search_query
    num_matches = len(matched_scripts)
    if num_matches == 0:
        filter_msg = "in categorie(s) {}".format(', '.join(args.category_filter)) if len(args.category_filter) > 0 else ''
        print 'No match found for "{}"{}'.format(query, filter_msg)
        return

    if num_matches == 1:
        msg = '1 match found.'
    else:
        msg = '{} matches found.'.format(num_matches)

    print msg
    print ''

    table = prettytable.PrettyTable([
        'Script name',
        'Description',
        'Categories'
    ], hrules=prettytable.ALL)

    for script_match in matched_scripts:
        script = script_match[0]
        table.add_row([
            color_matches(script.name, query),
            color_matches(get_displayable_description(script.short_description), query),
            ', '.join(script.categories) if script.categories else ''
        ])

    print table


def filter_category(args, ranked_scripts):
    # Filter out by category if needed
    if len(args.category_filter) == 0:
        return ranked_scripts

    matched_scripts = []
    for script in ranked_scripts:
        if len(set(script[0].categories).intersection(args.category_filter)) > 0:
            matched_scripts.append(script)

    return matched_scripts

def do_search(args):
    nse_scripts = build_nse_scripts_list(args)
    ranked_scripts = rank_nse_scripts(nse_scripts, args.search_query)
    matched_scripts = filter_category(args, ranked_scripts)

    if args.limit > 0:
        matched_scripts = matched_scripts[0:args.limit]

    print_result(args, matched_scripts)

def do_show_all(args):
    nse_scripts = build_nse_scripts_list(args)
    nse_scripts = [ (s, 1) for s in nse_scripts]
    matches = filter_category(args, nse_scripts)

    if args.limit > 0:
        matches = matches[0:args.limit]

    print_result(args, matches)