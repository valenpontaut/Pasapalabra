from datos import obtener_lista_definiciones

def crear_diccionario():
    """
    Función: crear_diccionario
    Parametros: no tiene
    Precondiciones: Tiene que existir una funcion llamada "obtener_lista_definiciones()" que devuelve una lista de palabras y definiciones.
    Postcondiciones: retorna un diccionario cuyas claves son las letras del abecedario y sus valores son todas las palabras que comienzan con esas mismas letras
    Autores: Valle Valentin y Francisco Albinati 
    """
    PALABRA = 0
    DEFINICION = 1
    diccionario_de_palabras = {}
    lista_de_palabras = obtener_lista_definiciones()
    for palabra_definicion in lista_de_palabras:    
        if len(palabra_definicion[PALABRA]) >= 5:
            diccionario_de_palabras[palabra_definicion[PALABRA]] = palabra_definicion[DEFINICION]
    return diccionario_de_palabras

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

def total_de_palabras(diccionario_de_palabras):
    """
    parametros: 
        diccionario_de_palabras: diccionario proveniente de la funcion crear_diccionario().
    Precondicion: Se debe proporcionar un diccionario generado por la funcion crear_diccionario()
    Postcondiciones: Retorna un diccionario que tiene como clave todas las letras del abecedario y como valor la cantidad de palabras que hay en cada una.
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
    return diccionario_cantidad_por_letra


def mostrar_total_de_palabras(diccionario_letras):
    """
    Parametros: 
        Diccionario_letras: Diccionario proveniente de la función total_de_palabras.
    Precondiciones: Se le debe dar un diccionario que tenga como clave las letras generadas por la funcion total_de_palabras() y como valor la cantidad de palabras disponibles para cada letra.
    Postcondiciones: muestra en pantalla la cantidad de palabras que hay por letra y la cantidad total de palabras que hay en el diccionario_palabras
    Aurores: Valle Valentin y Francisco Albinati
    """
    cantidad_palabras = 0
    for letra in diccionario_letras:
        print(f"la letra {letra} tiene {diccionario_letras[letra]} palabras")
        cantidad_palabras += diccionario_letras[letra]
    print(f"la cantidad total de palabras es: {cantidad_palabras}")

    
def main():
    diccionario = crear_diccionario()
    mostrar_total_de_palabras(total_de_palabras(diccionario))
