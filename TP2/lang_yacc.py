from lang_lex import tokens, literals
import ply.yacc as yacc

def parse_term(term):
    return term[0]

def parse_translation(translations):
    res = []
    for term in translations:
        res.append(parse_term(term))
    return res

def parse_entry(entry):
    res = {
            "Area" : [], 
            "Translations" : {
                "la" : [],
                "pt" : [],
                "ga" : [],
                "es" : [],
                "en" : [],
        }
    }

    for elem in entry:
        if elem[0] == 'area':
            res['Area'].append(elem[1])
        elif elem[0] == 'ga':
            res['Translations']['ga'].append(parse_translation(elem[1]))
        elif elem[0] == 'la':
            res['Translations']['la'].append(parse_translation(elem[1]))
        elif elem[0] == 'pt':
            res['Translations']['pt'].append(parse_translation(elem[1]))
        elif elem[0] == 'es':
            res['Translations']['es'].append(parse_translation(elem[1]))
        elif elem[0] == 'en':
            res['Translations']['en'].append(parse_translation(elem[1]))

    return res

def parse_dictionary(dic):
    res = {}
    i = 1
    for entry in dic:
        res[i] = parse_entry(entry)
        i += 1

    return res

def p_1(p): 
    r'dic : es'
    print(parse_dictionary(p[1]))

def p_2(p): 
    r'es : e LB es'
    p[0] = [p[1]] + p[3]

def p_3(p): 
    r'es : e'
    p[0] = [p[1]]

def p_4(p): 
    r'e : items'
    #print('4')
    p[0] = p[1]

def p_5(p): 
    r'items : item "\n" items'
    #print('5')
    p[0] = [p[1]] + p[3]

def p_6(p): 
    r'items : item'
    #print('6')
    p[0] = [p[1]]

def p_7(p): 
    r'item : at_conc'
    #print('7')
    p[0] = p[1]

def p_8(p): 
    r'item : ling'
    #print('8')
    p[0] = p[1]

def p_9(p): 
    r'at_conc : AREA ":" VAL'
    #print('9')
    p[0] = (p[1], p[3])

def p_10(p): 
    r'ling : ID_LING ":" "\n" ts "\n" "."'
    #print('10')
    p[0] = (p[1], p[4])

def p_11(p): 
    r'ts : ts "\n" t'
    #print('11')
    p[0] = p[1] + [p[3]]

def p_12(p): 
    r'ts : t'
    #print('12')
    p[0] = [p[1]]

def p_13(p): 
    r't : "-" VAL at_ts ";"'
    #print('13')
    p[0] = (p[2], p[3])

def p_14(p): 
    r'at_ts : at_ts at_t'
    #print('14')
    p[0] = p[1] + [p[2]]

def p_15(p): 
    r'at_ts : '
    #print('15')
    p[0] = []

def p_16(p): 
    r'at_t : "\n" "+" ID_ATTR ":" VAL'
    #print('16')
    p[0] = (p[3], p[5])

def p_error(p):
    print("Erro sintatico ", p)
    parser.success = False

# Build the parser
parser = yacc.yacc()
parser.success = True


#parser.parse(text)

if not parser.success:
    print("Erros de parsing!")
