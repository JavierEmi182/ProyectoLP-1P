import ply.yacc as yacc
from AnalisisLexico import tokens

global listerr
listerr = []

#JAVIER VERGARA
def p_program(p):
    '''
    program : statements
    '''

#JAVIER VERGARA
def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''

#JAVIER VERGARA
def p_statement(p):
    '''
    statement : assignment_statement
              | assignment_statement_type
              | print_statement
              | if_statement
              | function_general
              | function_call
              | function_init
              | while_statement
              | switch_statement
              | import_statement
              | for_statement 
              | comment
    '''

#JOSSELINE ASTUDILLO
def p_functionstatements(p):
    '''
    functionstatements : functionstatements functionbody
                        | functionbody
    '''
#JOSSELINE ASTUDILLO
def p_functionbody(p):
    '''
    functionbody : assignment_statement
                | assignment_statement_type
                | print_statement
                | if_statement
                | while_statement
                | switch_statement
                | import_statement
                | for_statement
                | empty
                | comment
    '''

#JAVIER VERGARA
def p_assignment_statement(p):
    '''
    assignment_statement : variable_declarator VARIABLE ASSIGN expression
                        |  variable_declarator VARIABLE ASSIGN READLN
                        | variable_declarator VARIABLE COLON data_collection_type ASSIGN collection_block
                        | variable_declarator VARIABLE COLON SET data_diamond_type ASSIGN collection_block 
                        | variable_declarator VARIABLE COLON SET ASSIGN collection_block
                        | variable_declarator VARIABLE COLON DICTIONARYTYPE ASSIGN collection_block
                        | VARIABLE ASSIGN expression
                        | VARIABLE ASSIGN READLN
    '''
#JAVIER VERGARA
def p_assignment_statement_type(p):
    '''
    assignment_statement_type : variable_declarator VARIABLE COLON data_type
                                | variable_declarator VARIABLE COLON data_type OPTIONALVARIABLE
                                | variable_declarator multiple_variables COLON data_type
                                | variable_declarator VARIABLE COLON data_type ASSIGN expression
                                | variable_declarator VARIABLE COLON data_type ASSIGN READLN
                                 
    '''

def p_multiple_assign(p):
    '''
    multiple_assign : multiple_assign assignment_statement
                    | assignment_statement
    '''
def p_import_statement(p):
    '''
    import_statement : IMPORT VARIABLE
    '''
def p_for_statement(p):
    '''
    for_statement : FOR VARIABLE IN NUMBER RANGE NUMBER LBRACES statements RBRACES
                    | FOR VARIABLE IN VARIABLE LBRACES statements RBRACES
    '''

#JAVIER VERGARA
def p_multiple_variables(p):
    '''
    multiple_variables : multiple_variables COMMA VARIABLE
                        | VARIABLE
                        
    '''
#JAVIER VERGARA
def p_collection_block(p):
    '''
    collection_block : LSQUAREBRACKET types RSQUAREBRACKET
    '''
#JAVIER VERGARA
def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN expression RPAREN
    '''

#JAVIER VERGARA
def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN LBRACES statements RBRACES
                 | IF LPAREN expression RPAREN LBRACES statements RBRACES ELSE LBRACES statements RBRACES
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

def p_function_general(p):
    '''
    function_general : function_declaration
                    | function_declaration_empty
                    

    '''
#JAVIER VERGARA
def p_function_declaration(p):
    '''
    function_declaration : FUNC VARIABLE LPAREN function_parameters RPAREN function_return_type LBRACES functionstatements return_statement RBRACES
    '''

def p_function_declaration_empty(p):
    '''
    function_declaration_empty : FUNC VARIABLE LPAREN empty  RPAREN function_return_type LBRACES functionstatements return_statement RBRACES
    '''

#JAVIER VERGARA
def p_function_parameters(p):
    '''
    function_parameters : function_parameters COMMA VARIABLE COLON data_type
                        | VARIABLE COLON data_type
                        
    '''
#JAVIER VERGARA
def p_function_return_type(p):
    '''
    function_return_type : ARROW data_type
                         | ARROW LPAREN function_parameters RPAREN
                         | empty
    '''
#JAVIER VERGARA
def p_return_statement(p):
    '''
    return_statement : RETURN expression
    '''
def p_function_init(p):
    '''
    function_init : INIT LPAREN function_parameters RPAREN LBRACES statements RBRACES
                    | INIT LPAREN empty RPAREN LBRACES statements RBRACES
    '''
#JAVIER VERGARA
def p_variable_declarator(p):
    '''
    variable_declarator : LET
                        | VAR
    '''
#JAVIER VERGARA
def p_data_type(p):
    '''
    data_type : INTEGER
              | STRING
              | BOOLEAN
              | DOUBLE
              | FLOAT
              | INT
    '''
#JAVIER VERGARA
def p_data_collection_type(p):
    '''
    data_collection_type : LSQUAREBRACKET INTEGER RSQUAREBRACKET
                        | LSQUAREBRACKET STRING RSQUAREBRACKET
                        | LSQUAREBRACKET BOOLEAN RSQUAREBRACKET
                        | LSQUAREBRACKET DOUBLE RSQUAREBRACKET
                        | LSQUAREBRACKET INT RSQUAREBRACKET
                        | LSQUAREBRACKET DICTIONARYTYPE RSQUAREBRACKET
    '''
def p_data_diamond_type(p):
    '''
    data_diamond_type : LESSTHAN INTEGER GREATERTHAN
                       | LESSTHAN STRING GREATERTHAN
                       | LESSTHAN BOOLEAN GREATERTHAN
                       | LESSTHAN DOUBLE GREATERTHAN
                       | LESSTHAN INT GREATERTHAN
    '''

def p_break_statement(p):
    '''
    break_statement : BREAK
    '''

#JAVIER VERGARA
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
               | function_call
               
    '''
#JAVIER VERGARA
def p_types(p):
    '''
    types : types COMMA type
          | key_value COMMA types
          | key_value
          | type
    '''
#JAVIER VERGARA
def p_type(p):
    '''
    type : TRUE
        | FALSE
        | DECIMAL
        | WSTRING
        | NUMBER
    '''

def p_key_value(p):
    '''
    key_value : type COLON type
    '''

def p_function_call(p):
    '''
    function_call : VARIABLE LPAREN function_arguments RPAREN
    '''
#JAVIER VERGARA
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
    str = f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    parser.errok()
    listerr.append(str)

def getErrors():
  #parser.lineno=1
  return listerr

# Build the parser
parser = yacc.yacc()
#parser.lineno=1
##sintactico =  yacc.yacc()
# Test data
data = '''
let x = 5 + 3 * 2
print(x)
if ( x > 10 ) {
    print("x is greater than 10")
} else {
    print("x is less than or equal to 10")
}

var numbers: [Int] = [1,2,3,4,5]

func add(a: int, b: int) -> int {
    return a + b
}

var y = add(1 + 1)

var favoriteGenres: set  = ["hola","chao"]
var favorite: set = [1,2,3,4]
func add() -> Int {
    return a + b
}

'''

# Parsing
#parser.parse(data)
"""
while True:
  try:
    s = input('swift > ')
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  if result != None: print(result)

while (True):
    print("hola")
"""


data =  """
let numero = 0
switch prueba {
    case "1":
        print("caso 1")
    case "2":
        numero = 9
    default:
        print("default")
}


var diccionario: [Int:String] = [1:"Uno", 2:"Dos", 3:"Tres"]

func minMax(a: int, b: int) -> (min:int, max:int) {
    return (a, b)
}
"""
parser.parse(data)