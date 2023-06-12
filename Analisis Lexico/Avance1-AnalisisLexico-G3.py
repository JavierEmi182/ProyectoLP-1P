import ply.lex as lex

#Diccionario de palabras reservadas
reserved = {
  #JAVIER VERGARA
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
  'while':'WHILE',
  'if':'IF',
  #JOSSELINE ASTUDILLO
  'import':'IMPORT',
  'class':'CLASS',
  'switch':'SWITCH',
  'for':'FOR',
  'continue':'CONTINUE',
  'break':'BREAK',
  'struct':'STRUCT',
  'enum':'ENUM',
  'public':'PUBLIC',
  'private':'PRIVATE',
  'character':'CHARACTER',
  'static':'STATIC',
  'typealias':'TYPEALIAS',
  'case':'CASE',
  'double': 'DOUBLE',
  'in':'IN',
  'init':'INIT',
  'default':'DEFAULT',
  'repeat':'REPEAT',
  #VICTOR PEÑA
  'int':'INTEGER',
  'float':'FLOAT',
  'set':'SET'

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
  #JOSSELINE ASTUDILLO
  'SETVARIABLE',
  'AND',
  'OR',
  'RANGO',
  'OPTIONALVARIABLE',
  #VICTOR PEÑA
  'COLLECTIONTYPE',
  'DICTIONARYTYPE',
  'VALUESTYPE'
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
t_CALLMETHOD = r'\.[A-Za-z]*(\(.+?\))'
t_NOT = r'!'
t_NOTEQUALS= r'!='
t_OFTYPE = r'\:'
t_RETURNVALUE = r'->'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
#t_CADENA = r'"[^"].*"'
t_CADENA= r'("[^"]*")'
t_MULTIPLY = r'\*'
t_PLUSONE = r'\+='
t_MINUSONE = r'\-='
#JOSSELINE ASTUDILLO
t_SETVARIABLE=r'\.[A-Za-z0-9]+'
t_AND=r'\&\&'
t_OR=r'\|\|'
t_RANGO=r'\.\.\.'
t_OPTIONALVARIABLE=r'\?'
#VICTOR PEÑA
t_COLLECTIONTYPE = r'<(int|string|bool|double|float)+>'
t_DICTIONARYTYPE = r'\[(int|string)\:\ ?(int|string|bool|double|float)\]'
t_VALUESTYPE = r'\[(int|string|bool|double|float)\]'

#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_VARIABLE(t):
  r'`[a-zA-Z]+`|([a-zA-Z]+[\w\d]*)'
  #r'[a-zA-Z]+[\w\d]*'
  t.type = reserved.get(t.value, 'VARIABLE')
  return t

# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'

def t_COMMENT(t):
        r'(\/\*(.|\n)*?\*\/)|(\/\/.*)'
        #t.lineno -= t.value.count('\n')
        t.type = reserved.get(t.value,'COMMENT')
        return t

#Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)


#Contruir analizador
lexer = lex.lex()

#Testeando JAVIER VERGARA
dataJV = '''//abc
/*  ASDASD
   asdasd
 */
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

dataJA= '''
  //prueba: usar keyword como identificador 
  let `let` = 3
  //for 
  for i in 1...4 { print(i) }

  // clases - atributos
    class Person: CustomStringConvertible {
      let name: String
      var address: String
      let age :Int?

      init(name: String, address: String) {
      self.name = name
      self.address = address

    }
    //switch
   let vegetable = "red pepper \n "
   switch vegetable {
   case "celery":
        let vegetableComment = "Add some raisins and make ants on a log."
   case "cucumber", "watercress":
        let vegetableComment = "That would make a good tea sandwich."
   case let x where x.hasSuffix("pepper"):
        let vegetableComment = "Is it a spicy \(x)?"
   default:
        let vegetableComment = "Everything tastes good in soup."
 }

'''.lower()

dataVP = '''
// Conjuntos (Sets)
var fruits: Set<String> = ["apple", "banana", "orange"]
fruits.insert("pear")
fruits.remove("banana")

if fruits.contains("apple") {
    print("El conjunto de frutas contiene una manzana.")
}

// Arreglos (Arrays)
var numbers: [Int] = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.remove(at: 3)

for number in numbers {
    print(number)
}

// Diccionarios (Dictionaries)
var ages: [String: Int] = ["John": 25, "Emily": 30, "Tom": 35]
ages["Sarah"] = 28
ages.removeValue(forKey: "Emily")

for (name, age) in ages {
    print("\(name) tiene \(age) años.")
}
'''.lower()
#Datos de entrada
#lexer.input(dataJV)
#lexer.input(dataJA)
lexer.input(dataVP)

# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break  #Rompe
  print(tok)
