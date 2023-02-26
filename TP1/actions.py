import re

def pass_f(file, match):
    pass

def intro(file, match):
    file.write('<doc>\n')

def end(file, match):
    file.write('</doc>\n')

def matter(file, match):
    file.write('<matter>' + match.group(1) +'</matter>\n')

def comma(file, match):
    file.write('<comma/>\n')

def lang(file, match):
    file.write('<lang>' + match.group(1) + '</lang>\n')

def synonym(file, match):
    match2 = re.search(r'([^V]+)VAR.-\s*(.+)', match.group(1))
    if match2:
        file.write('<synonym>' + match2.group(1) + '</synonym>\n')
        file.write('<variant>' + match2.group(2) + '</variant>\n')
    else:
        file.write('<synonym>' + match.group(1) + '</synonym>\n')
        if match.group(1) == '':
            file.write('<!-- next is synonym -->\n')

def formula_nr(file, match):
    file.write('<formula nr=\"' + match.group(1) + '\"/>\n')

def doc_entry(file, match):
    file.write('<entry word=\"' + match.group(2) + '\"/>\n')

def remissive(file, match):
    file.write('<remissive ref=\"' + match.group(1) + '\"/>\n')

def entry_nr(file, match):
    file.write('<entry nr=\"' + match.group(3) + '\"/>\n')

def variant(file, match):
    if match.group(1):
        file.write('<synonym>' + match.group(1) + '</synonym>\n')
    file.write('<variant>' + match.group(2) + '</variant>\n')

def join_previous(file, match):
    file.write('<join_previous>' + match.group(1) + '</join_previous>\n')

def word(file, match):
    file.write('<word>' + match.group(1) + '</word>\n')

def special1(file, match):
    file.write('<join_previous>' + match.group(1) + '</join_previous>\n')