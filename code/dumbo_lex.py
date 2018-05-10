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
    'ENDFOR',
    'IN',
    'DO',
    'IF',
    'ELSE',
    'ENDIF',
    'PRINT',
    'INTEGER',
    'ADD_OP',
    'MUL_OP',
    'PAR_FERM',
    'PAR_OUVR',
    'DOT_COMMA',
    'COMMA',
    'DOT',
    'ASSIGNEMENT',
    'APO',
    'STRING',
    'VAR',
    'TXT',
    'OPERATOR',
    'BINOPERATOR',
    'BOOLEAN'
    )


#INITIAL STATE
def t_BLOC_BEGIN(t):
    r'{{'
    t.lexer.begin('inCode')
    return t

def t_TXT(t):
    r'[\w|;|&|<|>|\"|_|-|\.|\\|\/|\n|\p|:|\,| \t]+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#IN_STRING STATE

def t_inString_APO(t):
    r'\''
    t.lexer.begin('inCode')
    return t

def t_inString_STRING(t):
    r'[\w|;|&|<|>|\"|_|-|\.|\\|\/|\n|\p|:|\,| ]+'
    return t

def t_inString_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#IN_CODE STATE

def t_inCode_APO(t):
    r'\''
    t.lexer.begin('inString')
    return t

def t_inCode_BLOC_END(t):
    r'}}'
    t.lexer.begin('INITIAL')
    return t

def t_inCode_FOR(t):
    r' for '
    return t

def t_inCode_IN(t):
    r' in '
    return t

def t_inCode_DO(t):
    r' do '
    return t

def t_inCode_ENDFOR(t):
    r' endfor '
    return t

def t_inCode_IF(t):
    r' if '
    return t

def t_inCode_ELSE(t):
    r' else '
    return t

def t_inCode_ENDIF(t):
    r' endif '
    return t

def t_inCode_PRINT(t):
    r' print '
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

def t_inCode_PAR_FERM(t):
    r'\)'
    return t

def t_inCode_PAR_OUVR(t):
    r'\('
    return t

def t_inCode_DOT_COMMA(t):
    r';'
    return t

def t_inCode_COMMA(t):
    r','
    return t

def t_inCode_DOT(t):
    r'\.'
    return t

def t_inCode_ASSIGNEMENT(t):
    r':='
    return t

def t_inCode_BOOLEAN(t):
    r'true|false'
    return t

def t_inCode_VAR(t):
    r'[\w]+'
    return t

def t_inCode_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_inCode_OPERATOR(t):
    r'<|>|=|!='

def t_inCode_BINOPERATOR(t):
    r'or|and'

t_inCode_ignore = ' \t'

def t_inString_error(t):
    print("Illegalcharacter '%s'" %t.value[0])
    t.lexer.skip(1)

def t_inCode_error(t):
    print("Illegalcharacter '%s'" %t.value[0])
    t.lexer.skip(1)

def t_error(t):
    print("Illegalcharacter '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    import sys
    lexer.input(sys.stdin.read())
    for token in lexer:
        print("line %d : %s (%s) " %(token.lineno, token.type, token.value))
