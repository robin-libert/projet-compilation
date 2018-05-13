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
    '''dumboBloc : BLOC_BEGIN expressionList BLOC_END
                 | BLOC_BEGIN BLOC_END'''
    if(len(p) == 4):
        p[0] = p[2]
    elif(len(p) == 3):
        p[0] = ElementVAR(None)

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
    '''expression : variableN ASSIGNEMENT globalExpression
                  | variableN ASSIGNEMENT list'''
    p[0] = VariableASS(p[1], p[3])

def p_expression_print(p):
    '''expression : PRINT globalExpression'''
    p[0] = Eprint(p[2])

def p_expression_forList(p):
    '''expression : FOR variableN IN list DO expressionList ENDFOR
                  | FOR variableN IN variable DO expressionList ENDFOR'''
    p[0] = ForExpression(p[2], p[4], p[6])

def p_expression_boolean(p):
    '''expression : IF globalExpression DO expressionList ENDIF
                  | IF globalExpression DO expressionList ELSE expressionList ENDIF'''
    if(len(p) == 6):
        p[0] = IfExpression(p[2], p[4], None)
    elif(len(p) == 8):
        p[0] = IfExpression(p[2], p[4], p[6])

#global Expression
def p_globalExpression(p):
    '''globalExpression : string
                        | integerVar
                        | variable
                        | booleanVar
                        | globalExpression BINOPERATOR globalExpression
                        | globalExpression OPERATOR globalExpression
                        | globalExpression ADD_OP globalExpression
                        | globalExpression MUL_OP globalExpression
                        | globalExpression DOT globalExpression'''
    if(len(p) == 2):
        p[0] = globalExpression(p[1], None, None)
    elif(len(p) == 4):
        p[0] = globalExpression(p[1], p[2], p[3])

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
    '''integerListInterior : integerVar
                           | integerVar COMMA integerListInterior'''
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
    p[0] = ElementVAR(p[2])

#integer Variable
def p_integerVar(p):
    '''integerVar : INTEGER'''
    p[0] = ElementVAR(p[1])

#boolean var
def p_booleanVar(p):
    '''booleanVar : BOOLEAN'''
    p[0] = BooleanVAR(p[1])

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
    ("left","OPERATOR"),
)

yacc.yacc(outputdir='generated')

if __name__ == '__main__':
    os.makedirs('generated', exist_ok=True)
    import sys
    dico['+'] = ''
    fichier1 = open(sys.argv[1])
    input1 = fichier1.read()
    fichier1.close()
    fichier2 = open(sys.argv[2])
    input2 = fichier2.read()
    fichier2.close()
    result1 = yacc.parse(input1)
    dico = result1.evaluate(dico)
    result2 = yacc.parse(input2)
    dico = result2.evaluate(dico)
    with open(sys.argv[3], "w") as fichier:
        fichier.write(dico['+'])
