import ply.lex as lex

#Probleme
#Dans l'état code, si on fait une variable 'blablaforblabla'
#il va considérer for comme le token FOR

states = (
    ('inCode', 'exclusive'),
    ('inString', 'exclusive'),
    )

tokens = (
    'BLOC_BEGIN',
    'BLOC_END',
    'FOR',
    'IN',
    'DO',
    'INTEGER',
    'ADD_OP',
    'MUL_OP',
    )


#INITIAL STATE
def t_BLOC_BEGIN(t):
    r'{{'
    t.lexer.begin('inCode')
    return t

#IN_CODE STATE
def t_inCode_BLOC_END(t):
    r'}}'
    t.lexer.begin('INITIAL')
    return t

def t_inCode_FOR(t):
    r'for'
    return t

def t_inCode_IN(t):
    r'in'
    return t

def t_inCode_DO(t):
    r'do'
    return t

def t_inCode_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_inCode_ADD_OP(t):
    r'\+|\-'
    return t

def t_inCode_MUL_OP(t):
    r'\*|\/'
    return t

def t_inCode_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    #print("Illegalcharacter '%s'" %t.value[0])
    t.lexer.skip(1)

if __name__ == '__main__':
    import sys
    lexer = lex.lex()
    lexer.input(sys.stdin.read())
    for token in lexer:
        print("line %d : %s (%s) " %(token.lineno, token.type, token.value))