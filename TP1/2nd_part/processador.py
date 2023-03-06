import re, json

rfile = open("medicina.txt", 'r')
wfile = open("medicina.json", 'w')

def remissive(dict, entry, lang, match):
    dict['remissives'][match.group(1)] = entry
    return (dict, entry, lang)

def entry(dict, entry, lang, match):
    dict['direct'][match.group(1)] = {}
    return (dict, match.group(1), '')

def matter(dict, entry, lang, match):
    if 'matter' not in dict['direct'][entry]:
        dict['direct'][entry]['matter'] = [match.group(1)]
    else:
        dict['direct'][entry]['matter'].append(match.group(1))
    return (dict, entry, lang)

def lang(dict, entry, lang, match):
    dict['direct'][entry][match.group(1)] = []
    return (dict, entry, match.group(1))

def word(dict, entry, lang, match):
    if lang != '':
        dict['direct'][entry][lang].append(match.group(1))
    return (dict, entry, lang)

def synonym(dict, entry, lang, match):
    if 'synonyms' not in dict['direct'][entry]:
        dict['direct'][entry]['synonyms'] = [match.group(1)]
    else:
        dict['direct'][entry]['synonyms'].append(match.group(1))
    return (dict, entry, lang)

def variant(dict, entry, lang, match):
    if 'variants' not in dict['direct'][entry]:
        dict['direct'][entry]['variants'] = [match.group(1)]
    else:
        dict['direct'][entry]['variants'].append(match.group(1))
    return (dict, entry, lang)


patterns = [(r'##([^\n]+)', remissive), (r'#\d+ ([^\n]+)', entry),
            (r'<matter>([^\n]+)', matter), (r'@([^\n]+)', lang),
            (r'\+([^\n]+)', word), (r'<synonym>([^\n]+)', synonym),
            (r'<variant>([^\n]+)', variant)]

dict = {
    'direct': {},
    'remissives': {}
}
entry = ''
lang = ''

for line in rfile:
    matched = False
    for i in range(0, len(patterns)):
        match = re.search(patterns[i][0], line)
        if match:
            dict, entry, lang = patterns[i][1](dict, entry, lang, match)
            matched = True
            break

json.dump(dict, wfile)

rfile.close()
wfile.close