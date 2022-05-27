from re import T
import ply.lex as lex
import sys
tokens=("INICIO",
"ARSS",
"CRSS",
"RSS",
"TEXTO",
"NUMERO", 
"CODING", 
"CATEGORIA",
"ACHANNEL",
"CCHANNEL", 
"COPY",
"DESCRIPTION",
"AIMAGEN",
"CIMAGEN", 
"AITEM",
"CITEM",
"ITEM",
"ITEMS",
"LINK", 
"TITULO",  
"URL",
"HEIGHT",
"WIDTH"
) 

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)#no se que hace esto
def t_s(t):
    r'\ '

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
 
def t_TITULO(t):
    '<title>[\s\S]*</title>'
    return t  

def t_LINK(t):  
    r'<link>(\S)*:(\S)*<\/link>'
    return t 
def t_CATEGORIA(t):
    r'<category>.*</category>'
    return t

def t_COPY(t):
    '<copyright>[\s\S]*</copyright>'
    return t 

def t_DESCRIPTION(t):
    r'<description>[\s\S]*</description>'
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
def t_URL(t):
    r'<url>[\ ]*(\S)*:(\S)*[\ ]*</url>'
    
    return t

def t_HEIGHT(t):
    '<height>[\ ]*\d*[\ ]*</height>'
    return t
    
def t_WIDTH(t):
    '<width>[\ ]*\d*[\ ]*</width>'
    return t


notrecognized=list()
def t_error(t):
    notrecognized.append(t.value[0])
    t.lexer.skip(1)


lexer= lex.lex() #debug=1 si queremos ver q hace internamente
 


#si empieza en espacios vacios es invalido el RSS
#si encuentra los siguientes caracteres es invalido: & < >

lexer.input('''
<?xml version="1.0" encoding="UTF-8" ?>
<?xml?>
<rss version="2.0"> 
<rss>       
<channel>
<title>RSS de la cátedra de Sintaxis y Semántica de Lenguajes </title>
<link>tox:DFB4958A86122ACF81BB852DBC767DB8A3A7281A8EDBC83121B30C294E295869121B298FEEA2</link>
<description>Sintaxis y Semántica de Lenguajes de la U.T.N.F.R.Resistencia. </description>
<category>Practica</category>

<image>
<url>https://frre.cvg.utn.edu.ar/pluginfile.php/29750/theme_snap/coverimage/1584391474/course-image.gif</url>
<title>encabez&ado imagen SSL</title>
<link>https://frre.cvg.utn.edu.ar/course/view.php?id=399</link>
<height>250 </height>
<width>120 </width>
</image>
<item>
<title>Planificacion 2022</title>
<link>https://</link>
<description>Planificacion de catedra, con cronograma de clases y
evaluaciones</description>
</item>
<item>
<title>Guia de Trabajos practicos</title>
<link>https://</link>
<description>Guía de ejercicios propuestos a resolver en clase
practica</description>
</item>
<item>
<title>Enunciado TPI</title>
<link>https://wl</link>
<description>Trabajo práctico integrador</description>
<category>Practica</category>

</item> 
</channel>      
</rss>

''')
 


 

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
print(notrecognized)