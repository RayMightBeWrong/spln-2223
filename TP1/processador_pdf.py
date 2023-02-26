import pdftotext, re
from actions import *

rfile = open("medicina.xml", 'r')
wfile = open("medicina2.xml", "w")

patterns = [(r'<!', pass_f), (r'<pdf2xml', intro), (r'</pdf2xml>', end), (r'^\s*<fontspec', pass_f), 
            (r'^<text[^>]*>(\s+|<i>\s+</i>|<b>\s+</b>)</text>', pass_f), (r'font="2">(\d+)<', pass_f), 
            (r'^<page number="(\d+)', pass_f), (r'^</page>', pass_f), (r'<text[^>]+>(V|ocabulario)<\/text>', pass_f),
            (r'font="6"><i>\s*([^<]+)\s*</i><', matter), (r'font="9">', pass_f), (r'font="0">;\s*<', comma), 
            (r'font="0">\s*(es|en|pt|la)\s*<', lang), (r'font="(12|2)">(<b>)?\s*([^<]*)', entry_nr),
            (r'<text[^>]*>\s*SIN.-\s*([^>]*)</text>', synonym), (r'<text[^>]*>([^V]+)?VAR.-\s*([^>]*)</text>', variant),
            (r'font="1(3|4|5)">(<b>)?([^<]*)', formula_nr), (r'font="\d+">(<i>)?<b>\s*([^<]+)', doc_entry), (r'">\s*Vid.-?\s*([^<]+)', remissive),
            (r'font="5">;?\s+([^<]*)', join_previous), (r'font="7"><i>\s*([^<]*)', word),
            # 2 casos especiais que não tinha sido capturados
            (r'font="0"> (\(sg\);) <', special1), (r'font="0">  (REL \(sg\)) <', special1)]

for line in rfile:
    matched = False
    for i in range(0, len(patterns)):
        match = re.search(patterns[i][0], line)
        if match:
            patterns[i][1](wfile, match)
            matched = True
            break
    if not matched:
        wfile.write(line)

rfile.close()
wfile.close()