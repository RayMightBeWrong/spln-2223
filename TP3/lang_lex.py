import ply.lex as lex

tokens = ['LB', 'VAL', 'ID_LING', 'ID_ATTR', 'AREA']
literals = [':', '\n', '-', '+', '.', ';']

def t_LB(t):
    r'\n\n'
    return t

def t_AREA(t):
    r'[ \t]*area[ \t]*'
    t.value = str(t.value).strip(' ')
    return t

def t_ID_ATTR(t):
    r'[ \t]*(var|sin)[ \t]*'
    t.value = str(t.value).strip(' ')
    return t

def t_ID_LING(t):
    r'(en|es|la|pt|ga)[ \t]*'
    t.value = str(t.value).strip(' ')
    return t

def t_VAL(t):
    r'[ \t]*([\w ]+)[ \t]*'
    t.value = str(t.value).strip(' ')
    return t


t_ignore = "\t"

def t_error(t):
    print(t)

lexer = lex.lex()
