def sort_in_area(dic):
    res = {}
    for entry in dic:
        areas = dic[entry]['Area']
        translations = dic[entry]['Translations']
        for area in areas:
            if area not in res:
                res[area] = [translations]
            else:
                res[area].append(translations)

    return res

def add_lang(terms, lang):
    if lang == 'la':
        lang = 'Latin'
    if lang == 'pt':
        lang = 'Portuguese'
    if lang == 'es':
        lang = 'Spanish'
    if lang == 'ga':
        lang = 'Galician'
    if lang == 'en':
        lang = 'English'
    res = f'''
                            <h4>{lang}</h4>
                                <ul>'''
    for term in terms:
        res += f'''
                                    <li><p>{term}</h6></p>'''

    res += '''
                                </ul>'''

    return res

def page_creator(dic):
    res = '''<!DOCTYPE html>
<html>
    <head>
        <title>Dictionary of Medicine</title>
        <meta charset="utf-8"/>
    </head>
    <body>
        <table>
            <tr>
                <td width="30%" valign="top">
                    <a name="#indice">
                    <h4>Specialties Index (in galician)</h4>
                    <ul>'''

    #print(sort_in_area(dic))
    dic = sort_in_area(dic)

    for area in dic:
        res += f'''
                        <li><a href="#{area}">{area}</a></li>'''

    res += '''
                    </ul>
                <td width="70%" valign="top">
                    <h1>Dictionary</h1>'''

    for area in dic:
        res += f'''
                        <h2><a href="#{area}">{area}</a></h2>'''
        terms = dic[area]
        for term in terms:
            print(term)
            res += '''
                            <table>
                            <tr>
                                <td width="25%" valign="top"><h4>-</h4></td>
                                <td width="75%" valign="top">'''
            if term['la'] != []:
                res += add_lang(term['la'], 'la')
            if term['en'] != []:
                res += add_lang(term['en'], 'en')
            if term['es'] != []:
                res += add_lang(term['es'], 'es')
            if term['ga'] != []:
                res += add_lang(term['ga'], 'ga')
            if term['pt'] != []:
                res += add_lang(term['pt'], 'pt')

            res += '''          
                                </td>
                            </tr>
                            </table>'''


    res += '''
                </td>
            </tr>
        </table>
    </body>
</html>
'''

    return res
