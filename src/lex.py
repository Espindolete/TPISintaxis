from re import T
import ply.lex as lex
import sys
#aclaraciones:
#una URL puede tener el siguiente formato y seguir siendo valido
#TEXTO:TEXTO es valido

#rss no acepta en todo el documento un '&', se podria llegar a tomar si fuera '&amp' pero sigue sin validarlo el validador de w3
#un TEXTO no acepta los siguientes caracteres < > en cualquier parte
#una URL parte de la expresion de TEXTO y esta no permite tampoco <,> ni & segun las especificaciones de RSS
#LOS TAGS DE RSS SON CASE SENSITIVE OSEA QUE TODOS VAN EN MINUSCULA

tokens=("INICIO",
"ARSS","CRSS",
"RSS",
"TEXTO",
"NUMERO", 
"CODING", 
"ACATEGORIA","CCATEGORIA", 
"ACHANNEL","CCHANNEL", 
"ACOPY","CCOPY", 
"ADESCRIPTION","CDESCRIPTION", 
"AIMAGEN","CIMAGEN", 
"AITEM","CITEM",
"ITEM",
"ITEMS",
"ALINK","CLINK", 
"ATITULO", "CTITULO",   
"AURL", "CURL",  
"HEIGHT",
"WIDTH",
"URI"
) 

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)#no se que hace esto

def t_s(t):
    r'\ '  
    #no devolvemos este token porque no nos afecta al leer

    
def t_URI(t) :
    '(http|ftp)(s)?://[^<>&]*([[^<>&]+:[^<>&]+?]?[[\\[^<>&]]+?[#[^<>&]+]?])?'
    return t
    
def t_TEXTO(t):
    '[^<>&]+'
    #EL TEXTO ENCUENTRA TODO SALVO ESTOS CARACTERES QUE SON INVALIDOS PARA CUALQUIER TEXTO Y URL DE RSS
    return t

def t_ARSS(t):
    '\<rss([\ ]+version[\ ]*=[\ ]*"\d.\d"[\ ]*)?>'
    return t

def t_CRSS(t):
    r'</rss>'
    return t 


def t_INICIO(t):
    '\<\?xml([\ ]+version[\ ]*=[\ ]*"\d.\d"[\ ]+encoding[\ ]*=[\ ]*"UTF-8"[\ ]*)?\?\>'            
    return t

def t_ACHANNEL(t):
    r'<channel>'
    return t

def t_CCHANNEL(t):
    r'</channel>'
    return t
 
def t_ATITULO(t):
    '<title>'
    return t  

def t_CTITULO(t): 
    '</title>'
    return t  
 
def t_ALINK(t):  
    r'<link>'
    return t  
    
def t_CLINK(t):  
    r'</link>'
    return t 


def t_ACATEGORIA(t):
    r'<category>'
    return t

def t_CCATEGORIA(t):
    r'</category>'
    return t

def t_ACOPY(t):
    '<copyright>'
    return t 
    
def t_CCOPY(t):
    '</copyright>'
    return t 

def t_ADESCRIPTION(t):
    '<description>'
    return t

def t_CDESCRIPTION(t):
    '</description>'
    return t

def t_AIMAGEN(t):
    '<image>'
    return t 

def t_CIMAGEN(t):
    '</image>'
    return t

def t_AITEM(t):
    '<item>'
    return t 

def t_CITEM(t):
    '</item>'
    return t

#una URL por definicion puede tener el siguiente formato
def t_AURL(t):
    r'<url>'
    return t
def t_CURL(t):
    r'</url>'
    return t
    

def t_HEIGHT(t):
    '<height>[\ ]*\d*[\ ]*</height>'
    return t
    
def t_WIDTH(t):
    '<width>[\ ]*\d*[\ ]*</width>'
    return t


notrecognized=list()
def t_error(t):
    print("se encontró el siguiente token no reconocible ",t.value[0])
    t.lexer.skip(1)


lexer= lex.lex() #debug=1 si queremos ver q hace internamente
 


#si empieza en espacios vacios es invalido el RSS
#si encuentra los siguientes caracteres es invalido: & < >1

entradaRSS=""
if (len(sys.argv) > 1):#se ingreso un comando agregado con este programa
    f=open(sys.argv[1],'r')
    entradaRSS=(f.read())
else:
    print("Ingrese 1 para ingresar un RSS por consola y 2 para ingresarlo por archivo")
    opcion=int(input())
    if opcion==1:
        print("empiece a escribir nomas")
        entra=input()
        while(entra!='</rss>'):
            entradaRSS+=entra
            entra=input()
    elif opcion==2:
        print("ingrese el nombre del archivo")
        entra=input()
        f=open(entra,"r")
        entradaRSS=f.read()
        pass
    else:
        print("ingrese una opcion valida")
        quit()



lexer.input(entradaRSS)
 


 

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

input("presione enter para salir")