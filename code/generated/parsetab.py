
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftDOTleftADD_OPleftMUL_OPleftBINOPERATORleftOPERATORADD_OP APO ASSIGNEMENT BINOPERATOR BLOC_BEGIN BLOC_END BOOLEAN COMMA DO DOT DOT_COMMA ELSE ENDFOR ENDIF FOR IF IN INTEGER MUL_OP OPERATOR PAR_FERM PAR_OUVR PRINT STRING TXT VARprogramme : TXT \n                 | TXT programmeprogramme : dumboBloc\n                 | dumboBloc programmedumboBloc : BLOC_BEGIN expressionList BLOC_END\n                 | BLOC_BEGIN BLOC_ENDexpressionList : expression DOT_COMMA\n                      | expression DOT_COMMA expressionListexpression : variableN ASSIGNEMENT globalExpression\n                  | variableN ASSIGNEMENT listexpression : PRINT globalExpressionexpression : FOR variableN IN list DO expressionList ENDFOR\n                  | FOR variableN IN variable DO expressionList ENDFORexpression : IF globalExpression DO expressionList ENDIF\n                  | IF globalExpression DO expressionList ELSE expressionList ENDIFglobalExpression : string\n                        | integerVar\n                        | variable\n                        | booleanVar\n                        | globalExpression BINOPERATOR globalExpression\n                        | globalExpression OPERATOR globalExpression\n                        | globalExpression ADD_OP globalExpression\n                        | globalExpression MUL_OP globalExpression\n                        | globalExpression DOT globalExpressionlist : PAR_OUVR stringListInterior PAR_FERM\n            | PAR_OUVR integerListInterior PAR_FERMstringListInterior : string\n                          | string COMMA stringListInteriorintegerListInterior : integerVar\n                           | integerVar COMMA integerListInteriorvariable : VARvariableN : VARstring : APO STRING APOintegerVar : INTEGERbooleanVar : BOOLEAN'
    
_lr_action_items = {'BLOC_BEGIN':([0,2,3,7,28,],[1,1,1,-6,-5,]),'DO':([15,16,17,18,20,21,22,23,41,43,44,45,46,47,48,49,58,61,],[-31,30,-34,-17,-35,-16,-18,-19,-24,-22,-23,-20,-21,-33,56,57,-26,-25,]),'INTEGER':([5,6,26,29,31,32,33,34,38,60,],[17,17,17,17,17,17,17,17,17,17,]),'MUL_OP':([15,16,17,18,20,21,22,23,24,37,41,43,44,45,46,47,],[-31,32,-34,-17,-35,-16,-18,-19,32,32,32,32,-23,-20,-21,-33,]),'PAR_OUVR':([26,36,],[38,38,]),'DOT':([15,16,17,18,20,21,22,23,24,37,41,43,44,45,46,47,],[-31,29,-34,-17,-35,-16,-18,-19,29,29,-24,-22,-23,-20,-21,-33,]),'ENDFOR':([27,40,63,64,],[-7,-8,68,69,]),'ENDIF':([27,40,42,62,],[-7,-8,54,67,]),'FOR':([1,27,30,55,56,57,],[8,8,8,8,8,8,]),'BLOC_END':([1,11,27,40,],[7,28,-7,-8,]),'$end':([2,3,4,7,13,14,28,],[-3,-1,0,-6,-4,-2,-5,]),'STRING':([19,],[35,]),'ADD_OP':([15,16,17,18,20,21,22,23,24,37,41,43,44,45,46,47,],[-31,31,-34,-17,-35,-16,-18,-19,31,31,31,-22,-23,-20,-21,-33,]),'DOT_COMMA':([10,15,17,18,20,21,22,23,24,37,39,41,43,44,45,46,47,54,58,61,67,68,69,],[27,-31,-34,-17,-35,-16,-18,-19,-11,-9,-10,-24,-22,-23,-20,-21,-33,-14,-26,-25,-15,-12,-13,]),'ELSE':([27,40,42,],[-7,-8,55,]),'VAR':([1,5,6,8,26,27,29,30,31,32,33,34,36,55,56,57,],[12,15,15,12,15,12,15,12,15,15,15,15,15,12,12,12,]),'PAR_FERM':([17,47,50,51,52,53,65,66,],[-34,-33,58,-27,-29,61,-28,-30,]),'IN':([12,25,],[-32,36,]),'OPERATOR':([15,16,17,18,20,21,22,23,24,37,41,43,44,45,46,47,],[-31,34,-34,-17,-35,-16,-18,-19,34,34,34,34,34,34,-21,-33,]),'IF':([1,27,30,55,56,57,],[5,5,5,5,5,5,]),'APO':([5,6,26,29,31,32,33,34,35,38,59,],[19,19,19,19,19,19,19,19,47,19,19,]),'PRINT':([1,27,30,55,56,57,],[6,6,6,6,6,6,]),'BOOLEAN':([5,6,26,29,31,32,33,34,],[20,20,20,20,20,20,20,20,]),'ASSIGNEMENT':([9,12,],[26,-32,]),'BINOPERATOR':([15,16,17,18,20,21,22,23,24,37,41,43,44,45,46,47,],[-31,33,-34,-17,-35,-16,-18,-19,33,33,33,33,33,-20,-21,-33,]),'TXT':([0,2,3,7,28,],[3,3,3,-6,-5,]),'COMMA':([17,47,51,52,],[-34,-33,59,60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stringListInterior':([38,59,],[53,65,]),'globalExpression':([5,6,26,29,31,32,33,34,],[16,24,37,41,43,44,45,46,]),'integerListInterior':([38,60,],[50,66,]),'list':([26,36,],[39,48,]),'integerVar':([5,6,26,29,31,32,33,34,38,60,],[18,18,18,18,18,18,18,18,52,52,]),'programme':([0,2,3,],[4,13,14,]),'variableN':([1,8,27,30,55,56,57,],[9,25,9,9,9,9,9,]),'string':([5,6,26,29,31,32,33,34,38,59,],[21,21,21,21,21,21,21,21,51,51,]),'variable':([5,6,26,29,31,32,33,34,36,],[22,22,22,22,22,22,22,22,49,]),'dumboBloc':([0,2,3,],[2,2,2,]),'expression':([1,27,30,55,56,57,],[10,10,10,10,10,10,]),'expressionList':([1,27,30,55,56,57,],[11,40,42,62,63,64,]),'booleanVar':([5,6,26,29,31,32,33,34,],[23,23,23,23,23,23,23,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> TXT','programme',1,'p_programme_Text','dumbo_synth.py',10),
  ('programme -> TXT programme','programme',2,'p_programme_Text','dumbo_synth.py',11),
  ('programme -> dumboBloc','programme',1,'p_programme_dumboBloc','dumbo_synth.py',19),
  ('programme -> dumboBloc programme','programme',2,'p_programme_dumboBloc','dumbo_synth.py',20),
  ('dumboBloc -> BLOC_BEGIN expressionList BLOC_END','dumboBloc',3,'p_dumboBloc_expressionList','dumbo_synth.py',28),
  ('dumboBloc -> BLOC_BEGIN BLOC_END','dumboBloc',2,'p_dumboBloc_expressionList','dumbo_synth.py',29),
  ('expressionList -> expression DOT_COMMA','expressionList',2,'p_expressionList_expression','dumbo_synth.py',37),
  ('expressionList -> expression DOT_COMMA expressionList','expressionList',3,'p_expressionList_expression','dumbo_synth.py',38),
  ('expression -> variableN ASSIGNEMENT globalExpression','expression',3,'p_expression_variable','dumbo_synth.py',46),
  ('expression -> variableN ASSIGNEMENT list','expression',3,'p_expression_variable','dumbo_synth.py',47),
  ('expression -> PRINT globalExpression','expression',2,'p_expression_print','dumbo_synth.py',51),
  ('expression -> FOR variableN IN list DO expressionList ENDFOR','expression',7,'p_expression_forList','dumbo_synth.py',55),
  ('expression -> FOR variableN IN variable DO expressionList ENDFOR','expression',7,'p_expression_forList','dumbo_synth.py',56),
  ('expression -> IF globalExpression DO expressionList ENDIF','expression',5,'p_expression_boolean','dumbo_synth.py',60),
  ('expression -> IF globalExpression DO expressionList ELSE expressionList ENDIF','expression',7,'p_expression_boolean','dumbo_synth.py',61),
  ('globalExpression -> string','globalExpression',1,'p_globalExpression','dumbo_synth.py',69),
  ('globalExpression -> integerVar','globalExpression',1,'p_globalExpression','dumbo_synth.py',70),
  ('globalExpression -> variable','globalExpression',1,'p_globalExpression','dumbo_synth.py',71),
  ('globalExpression -> booleanVar','globalExpression',1,'p_globalExpression','dumbo_synth.py',72),
  ('globalExpression -> globalExpression BINOPERATOR globalExpression','globalExpression',3,'p_globalExpression','dumbo_synth.py',73),
  ('globalExpression -> globalExpression OPERATOR globalExpression','globalExpression',3,'p_globalExpression','dumbo_synth.py',74),
  ('globalExpression -> globalExpression ADD_OP globalExpression','globalExpression',3,'p_globalExpression','dumbo_synth.py',75),
  ('globalExpression -> globalExpression MUL_OP globalExpression','globalExpression',3,'p_globalExpression','dumbo_synth.py',76),
  ('globalExpression -> globalExpression DOT globalExpression','globalExpression',3,'p_globalExpression','dumbo_synth.py',77),
  ('list -> PAR_OUVR stringListInterior PAR_FERM','list',3,'p_list_int','dumbo_synth.py',85),
  ('list -> PAR_OUVR integerListInterior PAR_FERM','list',3,'p_list_int','dumbo_synth.py',86),
  ('stringListInterior -> string','stringListInterior',1,'p_stringListInterior','dumbo_synth.py',91),
  ('stringListInterior -> string COMMA stringListInterior','stringListInterior',3,'p_stringListInterior','dumbo_synth.py',92),
  ('integerListInterior -> integerVar','integerListInterior',1,'p_integerListInterior','dumbo_synth.py',100),
  ('integerListInterior -> integerVar COMMA integerListInterior','integerListInterior',3,'p_integerListInterior','dumbo_synth.py',101),
  ('variable -> VAR','variable',1,'p_variable_dico','dumbo_synth.py',110),
  ('variableN -> VAR','variableN',1,'p_variable_name','dumbo_synth.py',114),
  ('string -> APO STRING APO','string',3,'p_string_seString','dumbo_synth.py',119),
  ('integerVar -> INTEGER','integerVar',1,'p_integerVar','dumbo_synth.py',124),
  ('booleanVar -> BOOLEAN','booleanVar',1,'p_booleanVar','dumbo_synth.py',129),
]
