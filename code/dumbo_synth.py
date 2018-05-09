import ply.yacc as yacc
from dumbo_lex import tokens
from grammar import *

dico = {}

def p_programme_Text(p):
    '''programme : TXT 
                 | TXT programme'''
    if(len(p) == 2):
        p[0] = Programme(Text(p[1]), None)
    elif(len(p) == 3):
        p[0] = Programme(Text(p[1]), p[2])


def p_programme_dumboBloc(p):
    '''programme : dumboBloc
                 | dumboBloc programme'''
    if(len(p) == 2):
        p[0] = Programme(p[1], None)
    elif(len(p) == 3):
        p[0] = Programme(p[1], p[2])


def p_dumboBloc_expressionList(p):
    '''dumboBloc : BLOC_BEGIN expressionList BLOC_END'''
    p[0] = p[2]

def p_expressionList_expression(p):
    '''expressionList : expression DOT_COMMA
                      | expression DOT_COMMA expressionList'''
    if(len(p) == 3):
        p[0] = ExpressionList(p[1], None)
    elif(len(p) == 4):
        p[0] = ExpressionList(p[1], p[3])

def p_expression_variable(p):
    '''expression : variableN ASSIGNEMENT stringExpression
                  | variableN ASSIGNEMENT stringList'''
    dico[p[1]] = p[3]

def p_expression_print(p):
    '''expression : PRINT stringExpression'''
    p[0] = Eprint(p[2])

def p_expression_forList(p):
    '''expression : FOR variableN IN stringList DO expressionList ENDFOR
                  | FOR variableN IN variable DO expressionList ENDFOR'''
    p[0] = ForExpression(p[2], p[4], p[6])

def p_stringExpression(p):
    '''stringExpression : variable
                        | string
                        | stringExpression DOT stringExpression'''
    if(len(p) == 2):
        p[0] = StringExpression(p[1], None)
    elif(len(p) == 4):
        p[0] = StringExpression(p[1], p[3])

def p_stringList_int(p):
    '''stringList : PAR_OUVR stringListInterior PAR_FERM'''
    p[0] = p[2]

def p_stringListInterior(p):
    '''stringListInterior : string
                          | string COMMA stringListInterior'''
    if(len(p) == 2):
        p[0] = StringList(p[1], None)
    elif(len(p) == 4):
        p[0] = StringList(p[1], p[3])

def p_variable_dico(p):
    '''variable : VAR'''
    p[0] = EVariable(p[1])

#on doit differencier les variables qui doivent etre remplacees de celles qui prennent une valeurs. 
def p_variable_name(p):
    '''variableN : VAR'''
    p[0] = p[1]

def p_string_seString(p):
    '''string : APO STRING APO'''
    p[0] = EString(p[2])



def p_error(p):
    print("Syntax error in line {}".format(p.lineno))
    yacc.error()

yacc.yacc(outputdir='generated')

if __name__ == '__main__':
    import sys
    input1 = open(sys.argv[1]).read()
    input2 = open(sys.argv[2]).read()
    yacc.parse(input1)
    result2 = yacc.parse(input2)
    result2.evaluate(dico)
