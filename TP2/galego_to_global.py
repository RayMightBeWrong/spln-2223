import re, json

rfile = open("galego_medicina.json", 'r')
wfile = open("global_medicina.json", 'w')
wfile2 = open("global_medicina.txt", 'w')

data = json.load(rfile)
dict = {}

i = 1
for entry in data['direct']:
    dict[i] = {
        "Area": [],
        "Translations": {}
    }
    dict[i]["Translations"]['ga'] = [entry]
    if 'synonyms' in data['direct'][entry]:
        for synonym in data['direct'][entry]['synonyms']:
            dict[i]['Translations']['ga'].append(synonym)
    if 'variants' in data['direct'][entry]:
        for variant in data['direct'][entry]['variants']:
            dict[i]['Translations']['ga'].append(variant)
    if 'matter' in data['direct'][entry]:
        for matter in data['direct'][entry]['matter']:
            dict[i]['Area'].append(matter)
    if 'es' in data['direct'][entry]:
        for es in data['direct'][entry]['es']:
            if 'es' not in dict[i]['Translations']:
                dict[i]['Translations']['es'] = [es]
            else:
                dict[i]['Translations']['es'].append(es)
    if 'pt' in data['direct'][entry]:
        for pt in data['direct'][entry]['pt']:
            if 'pt' not in dict[i]['Translations']:
                dict[i]['Translations']['pt'] = [pt]
            else:
                dict[i]['Translations']['pt'].append(pt)
    if 'la' in data['direct'][entry]:
        for la in data['direct'][entry]['la']:
            if 'la' not in dict[i]['Translations']:
                dict[i]['Translations']['la'] = [la]
            else:
                dict[i]['Translations']['la'].append(la)
    if 'en' in data['direct'][entry]:
        for en in data['direct'][entry]['en']:
            if 'en' not in dict[i]['Translations']:
                dict[i]['Translations']['en'] = [en]
            else:
                dict[i]['Translations']['en'].append(en)                
        
    i += 1

for entry in dict:
    for area in dict[entry]['Area']:
        wfile2.write('area: ' + area + '\n')
    for lang in dict[entry]['Translations']:
        wfile2.write(lang + ':\n')
        for word in dict[entry]['Translations'][lang]:
            wfile2.write('- ' + word + ';\n')
        wfile2.write('.\n')
    wfile2.write('\n')
    

json.dump(dict, wfile)

rfile.close()
wfile.close()
wfile2.close()