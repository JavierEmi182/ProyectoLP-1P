import ply.lex as lex

#Diccionario de palabras reservadas
reserved = {
  #JAVIER VERGARA
  'and': 'AND',
  'or': 'OR',
  'print': 'PRINT',
  'func':'FUNC',
  'string':'STRING',
  'boolean':'BOOLEAN',
  'bool':'BOOL',
  'integer':'INTEGER',
  'guard':'GUARD',
  'else':'ELSE',
  'return':'RETURN',
  'false':'FALSE',
  'let':'LET',
  'var':'VAR',
  'array':'ARRAY',
  'true':'TRUE',
  'whike':'WHILE',
  'if':'IF',
  #
}

#Sequencia de tokens, puede ser lista o tupla
tokens = (
  'NUMBER',
  'PLUS',
  'MINUS',
  'DIVIDE',
  'LPAREN',
  'RPAREN',
  'VARIABLE',
  'COMMA',
  'MAYORQUE',
  'MENORQUE',
  'EQUALS',
  #JAVIER VERGARA
  'COMMENTANIDADO',
  'CADENA',
  'MULTIPLY',
  'NOT',
  'NOTEQUALS',
  'OFTYPE',
  'RETURNVALUE',
  'LLLAVE',
  'RLLAVE',
  'COMMENT',
  'CALLMETHOD',
  'ASSIGN',
  'LCHORCHETE',
  'RCHORCHETE',
  'PLUSONE',
  'MINUSONE',
) + tuple(reserved.values())

#Exp Regulares para tokens de símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+'
t_COMMA = r','
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_EQUALS = r'=='
#JAVIER VERGARA
t_LCHORCHETE = r'\['
t_RCHORCHETE = r'\]'
t_ASSIGN = r'='
t_CALLMETHOD = r'\.[A-Za-z]*'
t_NOT = r'!'
t_NOTEQUALS= r'!='
t_OFTYPE = r'\:'
t_RETURNVALUE = r'->'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_CADENA = r'"[^".]*"'
t_MULTIPLY = r'\*'
t_PLUSONE = r'\+='
t_MINUSONE = r'\-='

#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_VARIABLE(t):
  r'[a-zA-Z]\w*'
  t.type = reserved.get(t.value, 'VARIABLE')
  return t

# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


#ignorar comments
def t_COMMENT(t):
  r'\/\*.*'
  t.type = reserved.get(t.value, 'COMMENT')
  return t
def t_COMMENTANIDADO(t):
  r'\/\*.*\*\/$'
  t.type = reserved.get(t.value, 'COMMENTANIDADO')
  return t

#Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)


#Contruir analizador
lexer = lex.lex()

#Testeando JAVIER VERGARA
dataJV = '''/*abc
/*  ASDASD */
  func isPalindrome(str: String) -> Bool {
    guard !str.isEmpty else {
        return false
    }
    
    let characters = Array(str)
    var left = 0
    var right = characters.count - 1
    while left < right {
        let leftCharacter = characters[left].lowercased()
        let rightCharacter = characters[right].lowercased()
        if leftCharacter != rightCharacter {
            return false
        }
        left += 1
        right -= 1
    }
    return true
}
    '''.lower()

data= '''

'''.lower()
#Datos de entrada
lexer.input(dataJV)

# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break  #Rompe
  print(tok)
