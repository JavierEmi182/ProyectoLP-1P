import ply.yacc as yacc
from AnalisisLexico import tokens

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
    statement : assignment_statement
              | print_statement
              | if_statement
              | function_general
              | while_statement
              | switch_statement
    '''


def p_assignment_statement(p):
    '''
    assignment_statement : variable_declarator VARIABLE ASSIGN expression
                        | variable_declarator VARIABLE COLON data_collection_type ASSIGN collection_block
                        | variable_declarator VARIABLE COLON SET ASSIGN collection_block 
                        | VARIABLE ASSIGN expression
    '''
def p_collection_block(p):
    '''
    collection_block : LSQUAREBRACKET expression RSQUAREBRACKET
    '''
def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN expression RPAREN
    '''


def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN LBRACES statements RBRACES
                 | IF LPAREN expression RPAREN LBRACES statements RBRACES ELSE LBRACES statements RBRACES
    '''

def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN expression RPAREN LBRACES statements RBRACES                   
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
def p_function_declaration(p):
    '''
    function_declaration : FUNC VARIABLE LPAREN function_parameters RPAREN function_return_type LBRACES expression return_statement RBRACES
    '''

def p_function_declaration_empty(p):
    '''
    function_declaration_empty : FUNC VARIABLE LPAREN empty  RPAREN function_return_type LBRACES expression return_statement RBRACES
    '''

def p_function_parameters(p):
    '''
    function_parameters : function_parameters COMMA VARIABLE COLON data_type
                        | VARIABLE COLON data_type
                        
    '''

def p_function_return_type(p):
    '''
    function_return_type : ARROW data_type
                        | empty
    '''
def p_return_statement(p):
    '''
    return_statement : RETURN expression
    '''
def p_variable_declarator(p):
    '''
    variable_declarator : LET
                        | VAR
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
def p_data_collection_type(p):
    '''
    data_collection_type : COLLECTIONTYPE
    '''

def p_break_statement(p):
    '''
    break_statement : BREAK
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
               | LPAREN expression RPAREN
               | NOT expression
               | VARIABLE
               | type
               | function_call
               | empty
    '''
def p_type(p):
    '''
    type : BOOL
        | DECIMAL
        | WSTRING
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
def p_error(p):
    errorFormat = ("Error sintáctico con: {0}. Sentencia errónea linea: {1}, caracter: {2}"
                   .format(p.value, p.lineno-1, p.lexpos))

    print(errorFormat)

# Build the parser
parser = yacc.yacc()
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

var numbers: [int] = [1,2,3,4,5]

func add(a: int, b: int) -> int {
    return a + b
}

var y = add(1 + 1)

var favoriteGenres: set  = ["hola","chao"]
var favorite: set = [1,2,3,4]
func add() -> int {
    return a + b
}

'''

# Parsing

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
"""
parser.parse(data)