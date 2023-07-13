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
              | assignment_to_type_collection_set
              | variable_declarator VARIABLE ASSIGN expression
              | ifComp
              | print_statement
              | while_statement
              | switch_statement
              | import_statement
              | for_statement 
              | function_general
              | function_call
              | function_init
              | comment
    '''


def p_variable_declarator(p):
    '''
    variable_declarator : LET
                        | VAR
    '''
def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN expression RPAREN
    '''

def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
               | expression GREATERTHAN expression
               | expression LESSTHAN expression
               | expression EQUALS expression
               | expression NOTEQUALS expression
               | expression AND expression
               | expression OR expression
               | expression COMMA expression
               | expression COLON expression
               | LPAREN expression RPAREN
               | NOT expression
               | VARIABLE
               | type
               | comparacion
               | boolean_expresion
               
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

#JOSSELINE ASTUDILLO
# que se comparen valores del mismo tipo entre sí
def p_comparacion(p):
   '''
   comparacion : VARIABLE operadorComp VARIABLE
               | DECIMAL operadorComp DECIMAL
               | WSTRING operadorComp WSTRING
               | NUMBER operadorComp NUMBER
               | VARIABLE operadorComp DECIMAL  
               | DECIMAL operadorComp VARIABLE
               | WSTRING operadorComp VARIABLE
               | VARIABLE operadorComp WSTRING
               | NUMBER operadorComp VARIABLE
               | VARIABLE operadorComp NUMBER
   '''


def p_operadorComp(p):

  '''operadorComp :  GREATERTHAN
                     | LESSTHAN
                     | EQUALS
                     | NOTEQUALS
  '''

#dentro del if que se establezca una comparación
def p_ifComp(p):
   '''
   ifComp : IF LPAREN comparacion RPAREN LBRACES statements RBRACES
         | IF LPAREN comparacion RPAREN LBRACES statements RBRACES ELSE LBRACES statements RBRACES
   '''



def p_type(p):
    '''
    type : TRUE
        | FALSE
        | DECIMAL
        | WSTRING
        | NUMBER
    '''

#Victor Peña
def p_assignment_to_type_collection_set(p):
  '''
  assignment_to_type_collection_set : variable_declarator VARIABLE COLON SET LESSTHAN integer_options GREATERTHAN ASSIGN LSQUAREBRACKET mul_integuer RSQUAREBRACKET
                                    | variable_declarator VARIABLE COLON SET LESSTHAN STRING GREATERTHAN ASSIGN LSQUAREBRACKET mul_string RSQUAREBRACKET
                                    | variable_declarator VARIABLE COLON SET LESSTHAN BOOLEAN GREATERTHAN ASSIGN LSQUAREBRACKET mul_booleano RSQUAREBRACKET
                                    | variable_declarator VARIABLE COLON SET LESSTHAN FLOAT GREATERTHAN ASSIGN LSQUAREBRACKET mul_float RSQUAREBRACKET
  '''

def p_boolean_expresion(p):
  '''
  boolean_expresion : LPAREN boolean_option logical_operator boolean_option RPAREN boolean_expresion
                    | boolean_expresion LPAREN boolean_option logical_operator boolean_option RPAREN 
                    | boolean_option logical_operator boolean_option
                    | logical_operator boolean_option
                    | boolean_option logical_operator
  ''' 

def p_logical_operator(p):
  '''
  logical_operator : AND
                   | OR  
  '''

#SINTACTICO
def p_import_statement(p):
    '''
    import_statement : IMPORT VARIABLE
    '''
def p_for_statement(p):
    '''
    for_statement : FOR VARIABLE IN NUMBER RANGE NUMBER LBRACES statements RBRACES
                    | FOR VARIABLE IN VARIABLE LBRACES statements RBRACES
    '''
def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN expression RPAREN LBRACES statements RBRACES
                    | REPEAT LBRACES statements RBRACES WHILE LPAREN expression RPAREN                   
    '''

def p_switch_statement(p):
    '''
    switch_statement : SWITCH VARIABLE LBRACES caso RBRACES
    '''

def p_caso(p):
    '''
    caso : CASE expression COLON cuerpo_caso caso
         | CASE expression COLON cuerpo_caso DEFAULT COLON cuerpo_caso
    '''

def p_cuerpo_caso(p):
    '''
    cuerpo_caso : expression 
                | statement
    '''

def p_functionstatements(p):
    '''
    functionstatements : functionstatements functionbody
                        | functionbody
    '''
def p_functionbody(p):
    '''
    functionbody : assignment_to_type
                | print_statement
                | ifComp
                | while_statement
                | switch_statement
                | import_statement
                | for_statement
                | empty
                | comment
    '''

def p_function_general(p):
    '''
    function_general : function_declaration
                    | function_declaration_empty
                    

    '''
def p_function_declaration(p):
    '''
    function_declaration : FUNC VARIABLE LPAREN function_parameters RPAREN function_return_type LBRACES functionstatements return_statement RBRACES
    '''

def p_function_declaration_empty(p):
    '''
    function_declaration_empty : FUNC VARIABLE LPAREN empty  RPAREN function_return_type LBRACES functionstatements return_statement RBRACES
    '''
def p_data_type(p):
    '''
    data_type : INTEGER
              | STRING
              | BOOLEAN
              | DOUBLE
              | FLOAT
              | INT
    '''
def p_function_parameters(p):
    '''
    function_parameters : function_parameters COMMA VARIABLE COLON data_type
                        | VARIABLE COLON data_type
                        
    '''

def p_function_return_type(p):
    '''
    function_return_type : ARROW data_type
                         | ARROW LPAREN function_parameters RPAREN
                         | empty
    '''
def p_return_statement(p):
    '''
    return_statement : RETURN expression
    '''
def p_function_init(p):
    '''
    function_init : INIT LPAREN function_parameters RPAREN LBRACES statements RBRACES
    '''
def p_function_call(p):
    '''
    function_call : VARIABLE LPAREN function_arguments RPAREN
    '''
def p_function_arguments(p):
    '''
    function_arguments : function_arguments COMMA expression
                       | expression
                       | empty
    '''
def p_empty(p):
    '''
    empty :
    '''
def p_comment(p):
    '''
    comment : COMMENT
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

data = '''
   let var : integer = 45
   let arreglo : [integer] = [1,2,3,4] 

   let variable = "hola"
   let variable = 5 > 10
   if (10>8){
      print("hola")
   }else{
      print("no")
   }

   var conjunto : Set<String> = ["prueba", "hola"]
   let prueba = (true && false) || false
'''

#parser.parse(data)