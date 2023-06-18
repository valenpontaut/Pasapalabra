from configuracion import obtener_config
config = obtener_config()
LONG_PALABRA_MIN = config["LONGITUD_PALABRA_MINIMA"]


def crear_archivo_palabras_seleccionadas(lista_palabra_definicion):
    """
    parametros: 
        lista_palabra_definicion: lista retornada por la funcion obtener_dicc_palabra_definicion() .
    Precondicion: Se debe proporcionar una lista generado por la obtener_dicc_palabra_definicion().
    Postcondiciones: Genera un archivo el cual en cada linea tiene una palabra con su respectiva definicion, separadas por una ",".
    autores: Valle Valentin y Francisco Albinati 
    """
    PALABRA = 0
    DEFINICION = 1            
    with open("diccionario.csv", "w", encoding='utf-8') as palabras_filtradas:
        for palabra in lista_palabra_definicion:
            palabras_filtradas.write(f"{palabra[PALABRA]}, '{palabra[DEFINICION]}'\n")

def palabra_sin_tilde(letra):
    """
    parametros:
        letra: Es un carácter proveniente de todas las primeras letras que tienen las claves del diccionario que retorna crear_diccionario.}
    Precondiciones: El caracter letra tiene que ser valido y pertenecer a las primeras letras que tienen las claves del diccionario generado por crear_diccionario().
    Postcondiciones: si la letra tiene tilde se le quita y nos devuelve la letra modificada, de no ser asi nos devuelve la misma letra
    autores: Valle Valentin y Francisco Albinati 
    """
    DICCIONARIO_TILDES = {'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u'}
    if letra in DICCIONARIO_TILDES:
        letra = DICCIONARIO_TILDES[letra]

    return letra
    
def obtener_lista_palabra_definicion(ruta_palabras, ruta_definiciones,long_palabra_min):
    """
    parametros:
        ruta_palabras: ruta donde se encuentra un archivo que contiene palabras.
        ruta_definiciones: ruta donde se encuentra un archivo que contiene las definiciones de las palabras encontradas en "ruta_palabras".
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
                    if len(palabra) > long_palabra_min and palabra.isalpha():
                        diccionario_palabra_definicion[palabra] = definicion
                    palabra = palabras.readline().rstrip("\n")
                    definicion = definiciones.readline().rstrip("\n")
    except FileNotFoundError:
        ruta_palabras = "palabras.txt"
        ruta_definiciones = "definiciones.txt"
        return obtener_lista_palabra_definicion(ruta_palabras, ruta_definiciones,long_palabra_min)

    lista_palabras_definicion = sorted(diccionario_palabra_definicion.items(), key=lambda clave: palabra_sin_tilde(clave[0][0]))
    crear_archivo_palabras_seleccionadas(lista_palabras_definicion)
    return lista_palabras_definicion

def obtener_palabras_por_letra(diccionario_de_palabras):
    """
    parametros: 
        diccionario_de_palabras: diccionario proveniente de la funcion crear_diccionario().
    Precondicion: Se debe proporcionar un diccionario generado por la funcion crear_diccionario()
    Postcondiciones: Retorna una lista de listas que tienen en su primer posicion una letra y en la segunda la cantidad de palabras disponibles para jugar con la misma.
    autores: Valle Valentin y Francisco Albinati 
    """
    PRIMER_LETRA = 0
    diccionario_cantidad_por_letra = {}
    for palabra in diccionario_de_palabras:
        primer_letra_palabra = palabra_sin_tilde(palabra[PRIMER_LETRA])
        if primer_letra_palabra not in diccionario_cantidad_por_letra:
            diccionario_cantidad_por_letra[primer_letra_palabra] = 1
        else:
            diccionario_cantidad_por_letra[primer_letra_palabra] += 1

    palabras_por_letra = sorted(diccionario_cantidad_por_letra.items(), key = lambda x:x[0])
            
    return palabras_por_letra

obtener_lista_palabra_definicion("palsabras.txt","definiciones.txt",LONG_PALABRA_MIN)





