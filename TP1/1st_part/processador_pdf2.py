import re

rfile = open("medicina2.txt", 'r')
wfile = open("medicina3.txt", 'w')

def join_previous(file, match, previous):
    return previous[:-1] + ' ' + match.group(1)


patterns = [(r'<join_previous>([^<]+)', join_previous)]

previous = ''
for line in rfile:
    matched = False
    for i in range(0, len(patterns)):
        match = re.search(patterns[i][0], line)
        if match:
            previous = patterns[i][1](wfile, match, previous)
            matched = True
            break
        else:
            wfile.write(previous)
            previous = line


rfile.close()
wfile.close()