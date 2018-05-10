import ply.yacc as yacc
from dumbo_lex import tokens
from grammar import *
import os

dico = {}

#programme
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

#dumbo BLoc
def p_dumboBloc_expressionList(p):
    '''dumboBloc : BLOC_BEGIN expressionList BLOC_END'''
    p[0] = p[2]

#expression List
def p_expressionList_expression(p):
    '''expressionList : expression DOT_COMMA
                      | expression DOT_COMMA expressionList'''
    if(len(p) == 3):
        p[0] = ExpressionList(p[1], None)
    elif(len(p) == 4):
        p[0] = ExpressionList(p[1], p[3])

#expression
def p_expression_variable(p):
    '''expression : variableN ASSIGNEMENT stringExpression
                  | variableN ASSIGNEMENT list'''
    dico[p[1]] = p[3]

def p_expression_print(p):
    '''expression : PRINT stringExpression'''
    p[0] = Eprint(p[2])

def p_expression_forList(p):
    '''expression : FOR variableN IN list DO expressionList ENDFOR
                  | FOR variableN IN variable DO expressionList ENDFOR'''
    p[0] = ForExpression(p[2], p[4], p[6])

def p_expression_boolean(p):
    '''expression : IF boolean DO expressionList ENDIF
                  | IF boolean DO expressionList ELSE expressionList ENDIF'''
    if(len(p) == 6):
        p[0] = IfExpression(p[2], p[4], None)
    elif(len(p) == 8):
        p[0] = IfExpression(p[2], p[4], p[6])

#string Expression
def p_stringExpression(p):
    '''stringExpression : integer
                        | string
                        | stringExpression DOT stringExpression'''
    if(len(p) == 2):
        p[0] = StringExpression(p[1], None)
    elif(len(p) == 4):
        p[0] = StringExpression(p[1], p[3])

#List
def p_list_int(p):
    '''list : PAR_OUVR stringListInterior PAR_FERM
            | PAR_OUVR integerListInterior PAR_FERM'''
    p[0] = p[2]

#'''' de String
def p_stringListInterior(p):
    '''stringListInterior : string
                          | string COMMA stringListInterior'''
    if(len(p) == 2):
        p[0] = List(p[1], None)
    elif(len(p) == 4):
        p[0] = List(p[1], p[3])

#'''' de integer
def p_integerListInterior(p):
    '''integerListInterior : integer
                           | integer COMMA integerListInterior'''
    if(len(p) == 2):
        p[0] = List(p[1], None)
    elif(len(p) == 4):
        p[0] = List(p[1], p[3])

#variable
'''une differenciation doit être faites entre les variables qui recupere une valeur(variable) et ceux qui attribue une valeur (variableN)'''
def p_variable_dico(p):
    '''variable : VAR'''
    p[0] = EVariable(p[1])

def p_variable_name(p):
    '''variableN : VAR'''
    p[0] = p[1]

#string
def p_string_seString(p):
    '''string : APO STRING APO'''
    p[0] = EString(p[2])

#integer
def p_integer(p):
    '''integer : integerVar
               | variable
               | integer ADD_OP integer
               | integer MUL_OP integer'''
    if(len(p) == 2):
        p[0] = globalInteger(p[1], None, None)
    elif(len(p) == 4):
        p[0] = globalInteger(p[1], p[2], p[3])

#integer Variable
def p_integerVar(p):
    '''integerVar : INTEGER'''
    p[0] = IntegerVar(p[1])

#boolean
def p_boolean(p):
    '''boolean : booleanVar
               | booleanOP
               | boolean BINOPERATOR boolean'''
    if(len(p) == 2):
        p[0] = boolean(p[1], None, None)
    elif(len(p) == 4):
        p[0] = boolean(p[1], p[2], p[3])

#boolean operator
def p_booleanOP(p):
    '''booleanOP : integer OPERATOR integer'''
    p[0] = booleanExpression(p[1],p[2],p[3])

#boolean var
def p_booleanVar(p):
    '''booleanVar : BOOLEAN'''
    p[0] = booleanVAR(p[1])

#error
def p_error(p):
    print("Syntax error in line {}".format(p.lineno))
    yacc.error()

#precedence
precedence = (
    ("left","DOT"),
    ("left","ADD_OP"),
    ("left","MUL_OP"),
    ("left","BINOPERATOR"),
)

yacc.yacc(outputdir='generated')

if __name__ == '__main__':
    os.makedirs('generated', exist_ok=True)
    import sys
    input1 = open(sys.argv[1]).read()
    input2 = open(sys.argv[2]).read()
    yacc.parse(input1)
    result2 = yacc.parse(input2)
    result2.evaluate(dico)
