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
    '''


def p_assignment_statement(p):
    '''
    assignment_statement : LET VARIABLE ASSIGN expression
                        | VAR VARIABLE ASSIGN expression
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


def p_data_type(p):
    '''
    data_type : INTEGER
              | STRING
              | BOOLEAN
              | DOUBLE
              | FLOAT
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
               | LPAREN expression RPAREN
               | NOT expression
               | VARIABLE
               | BOOL
               | DECIMAL
    '''

def p_error(p):
    if p:
        print("Error de sintaxis en token:", p.type)
    #sintactico.errok()
    else:
        print("Syntax error at EOF")

# Build the parser
##parser = yacc.yacc()
sintactico =  yacc.yacc()
# Test data
data = '''
let x = 5 + 3 * 2
print(x)
'''

# Parsing
##parser.parse(data)
while True:
  try:
    s = input('swift > ')
  except EOFError:
    break
  if not s: continue
  result = sintactico.parse(s)
  if result != None: print(result)