import ply.yacc as yacc
import sys
from AnalisisLexico import tokens

global listerr
listerr = []

def p_program(p):
    '''
    program : statements
    '''
def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''
def p_statement(p):
    '''
    statement : assignment_to_type
              | assignment_to_type_collection
    '''
def p_variable_declarator(p):
    '''
    variable_declarator : LET
                        | VAR
    '''

##JAVIER VERGARA
#Que si se especifica el tipo al crear la variable, solo acepte ese tipo
def p_assignment_to_type(p):
  '''
  assignment_to_type : variable_declarator VARIABLE COLON STRING ASSIGN WSTRING
                    | variable_declarator VARIABLE COLON INTEGER ASSIGN NUMBER
                    | variable_declarator VARIABLE COLON BOOLEAN ASSIGN TRUE
                    | variable_declarator VARIABLE COLON BOOLEAN ASSIGN FALSE
                    | variable_declarator VARIABLE COLON FLOAT ASSIGN DECIMAL
  '''

#Caso coleccion tambien

def p_assignment_to_type_collection(p):
  '''
  assignment_to_type_collection : variable_declarator VARIABLE COLON LSQUAREBRACKET integer_options RSQUAREBRACKET ASSIGN LSQUAREBRACKET mul_integuer RSQUAREBRACKET
                    | variable_declarator VARIABLE COLON LSQUAREBRACKET STRING RSQUAREBRACKET ASSIGN LSQUAREBRACKET mul_string RSQUAREBRACKET
                    | variable_declarator VARIABLE COLON LSQUAREBRACKET BOOLEAN RSQUAREBRACKET ASSIGN LSQUAREBRACKET mul_booleano RSQUAREBRACKET
                    | variable_declarator VARIABLE COLON LSQUAREBRACKET FLOAT RSQUAREBRACKET ASSIGN LSQUAREBRACKET mul_float RSQUAREBRACKET
  '''
def p_integer_options(p):
   '''
   integer_options : INTEGER
                    | INT
   '''
def p_mul_integuer(p):
   '''mul_integuer : mul_integuer COMMA NUMBER
                    | NUMBER
   '''
def p_mul_string(p):
   '''mul_string : mul_string COMMA WSTRING
                    | WSTRING
   
   '''
def p_mul_booleano(p):
   '''mul_booleano : mul_booleano COMMA boolean_option
                    | boolean_option
   '''
def p_boolean_option(p):
   '''
   boolean_option : TRUE 
                  | FALSE
   '''
def p_mul_float(p):
   '''mul_float : mul_float COMMA DECIMAL
                    | DECIMAL
   '''

def p_error(p):
  if p:
    str = f"Error semantico - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    parser.errok()
    listerr.append(str)

def getErrors():
  return listerr

# Build the parser
parser = yacc.yacc()
parser.lineno = 0

def validaRegla(s):
  result = parser.parse(s, debug=False)
  print(result)
  return str(result)

#data = '''
#    let var : integer = 45
#    let arreglo : [integer] = [1,2,3,4] 
#'''

#parser.parse(data)