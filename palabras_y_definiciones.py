from configuracion import obtener_config
config = obtener_config()
LONG_PALABRA_MIN = config["LONGITUD_PALABRA_MINIMA"]


def crear_archivo_palabras_seleccionadas(lista_palabra_definicion):
    """
    Funcion: crear_archivo_palabras_seleccionadas
    parametros: 
        lista_palabra_definicion: lista retornada por la funcion obtener_lista_palabra_definicion().
    Salidas:
        no tiene, la funcion solo genera un archivo.
    Precondicion: Se debe proporcionar una lista generado por la obtener_lista_palabra_definicion().
    Postcondiciones: Genera un archivo el cual en cada linea tiene una palabra con su respectiva definicion, separadas por una ",".
    autores: Valle Valentin y Francisco Albinati 
    """
    PALABRA = 0
    DEFINICION = 1            
    with open("diccionario.csv", "w", encoding='utf-8') as palabras_filtradas:
        for palabra in lista_palabra_definicion:
            palabras_filtradas.write(f"{palabra[PALABRA]}, '{palabra[DEFINICION]}'\n")

def quitar_acento(letra):
    """
    Funcion: quitar_acento
    parametros:
        letra: Caracter proveniente de la primer letra de una palabra.
    Salidas:
        letra: Retorna siempre la letra ingresada pero sin acento.
    Precondiciones: El caracter letra tiene que ser valido y pertenecer a las primer letra de una palabra.
    Postcondiciones: si la letra tiene tilde se le quita y nos devuelve la letra modificada, de no ser asi nos devuelve la misma letra
    autores: Valle Valentin y Francisco Albinati 
    """
    DICCIONARIO_TILDES = {'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u'}
    if letra in DICCIONARIO_TILDES:
        letra = DICCIONARIO_TILDES[letra]

    return letra    
    
def obtener_lista_palabra_definicion(ruta_palabras, ruta_definiciones,LONG_PALABRA_MIN):
    """
    Funcion: obtener_lista_palabra_definicion
    parametros:
        ruta_palabras: ruta donde se encuentra un archivo que contiene palabras.
        ruta_definiciones: ruta donde se encuentra un archivo que contiene las definiciones de las palabras encontradas en "ruta_palabras".
    Salidas: 
        lista_palabras_definicion: Lista de listas que en su primera posicion se encuentra el nombre de las palabras y en la segunda la definicion de las mismas.
    Precondiciones: Tener los 2 archivos que pasamos por parametro.
    Postcondiciones: retorna una lista ordenada alfabeticamente de palabras y definiciones, las palabras tienen que ser mayores a LONG_MAX y ademas tienen que estar solo compuestas por letras.
    autores: Valle Valentin y Francisco Albinati 
    """    
    diccionario_palabra_definicion = {}
    try:
        with open(ruta_palabras, "r", encoding='utf-8') as palabras:
            with open(ruta_definiciones, "r", encoding='utf-8') as definiciones:
                palabra = palabras.readline().rstrip("\n")
                definicion = definiciones.readline().rstrip("\n")

                while palabra != "":
                    if len(palabra) > LONG_PALABRA_MIN and palabra.isalpha():
                        diccionario_palabra_definicion[palabra] = definicion
                    palabra = palabras.readline().rstrip("\n")
                    definicion = definiciones.readline().rstrip("\n")
    except FileNotFoundError:
        ruta_palabras = "palabras.txt"
        ruta_definiciones = "definiciones.txt"
        return obtener_lista_palabra_definicion(ruta_palabras, ruta_definiciones,LONG_PALABRA_MIN)

    lista_palabras_definicion = sorted(diccionario_palabra_definicion.items(), key=lambda clave: quitar_acento(clave[0][0]))
    crear_archivo_palabras_seleccionadas(lista_palabras_definicion)
    return lista_palabras_definicion

def obtener_palabras_por_letra(lista_palabras_definicion):
    """
    Funcion: obtener_palabras_por_letra
    parametros: 
        lista_palabras_definicion: lista proveniente de la funcion obtener_lista_palabra_definicion().
    Salidas:
        palabras_por_letra: Lista de listas que en su primer posicion estan todas las letras disponibles para jugar y en su segunda posicion esta la cantidad de palabras que tiene cada letra.
    Precondicion: Se debe proporcionar una lista generada por la funcion obtener_lista_palabra_definicion()
    Postcondiciones: Retorna una lista de listas que tienen en su primer posicion una letra y en la segunda la cantidad de palabras disponibles para jugar con la misma.
    autores: Valle Valentin y Francisco Albinati 
    """
    PALABRA = 0
    PRIMER_LETRA = 0
    diccionario_cantidad_por_letra = {}
    for palabra_definicion in lista_palabras_definicion:
        primer_letra_palabra = quitar_acento(palabra_definicion[PALABRA][PRIMER_LETRA])
        if primer_letra_palabra not in diccionario_cantidad_por_letra:
            diccionario_cantidad_por_letra[primer_letra_palabra] = 1
        else:
            diccionario_cantidad_por_letra[primer_letra_palabra] += 1

    palabras_por_letra = sorted(diccionario_cantidad_por_letra.items(), key = lambda x:x[0])
            
    return palabras_por_letra

def test_unitario():
    import doctest
    """
    >>> quitar_acento('á')
    'a'
    >>> quitar_acento('é')
    'e'
    >>> quitar_acento('í')
    'i'
    >>> quitar_acento('ó')
    'o'
    >>> quitar_acento('ú')
    'u'
    >>> quitar_acento('a')
    'a'
    >>> quitar_acento('e')
    'e'
    >>> quitar_acento('i')
    'i'
    >>> quitar_acento('o')
    'o'
    >>> quitar_acento('u')
    'u'
    """
    doctest.testmod()
# test_unitario()

#obtener_lista_palabra_definicion("palabras.txt","definiciones.txt",LONG_PALABRA_MIN)





