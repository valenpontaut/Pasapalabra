from etapa2 import palabra_sin_tilde, crear_diccionario, total_de_palabras
import random

ACENTOS = ("á", "é", "í", "ó", "ú")

def crear_lista_letras(letras):
    '''
    Función: crear_lista_letras
    Parámetros: -letras: Es una lista con chars representando todas las letras del abecedario.
    Salida: Genera la lista de 10 letras aleatorias.
    Autores: Valentín Marturet / Renato Villalba
    '''
    letras_seleccionadas = random.sample(letras, 10)
    letras_seleccionadas.sort()
    
    return letras_seleccionadas

def filtrar_palabras(palabras, cant_por_letra, letras_seleccionadas):
    '''
    Función: filtras_palabras
    Parametros: - palabras: Es una lista de palabras que deben estar ordenadas alfabeticamente.
                - cant_por_letra: Es una lista de listas en la que el primer valor es la letra y el segundo la cantidad de palabras con esa letra en el diccionario.
                - letras_seleccionadas: Es una lista de las letras seleccionadas sobre las cuales se deben filtrar las palabras.
    Autores: Valentín Marturet / Renato Villalba
    '''
    CANT = 1
    lista_filtrada = []
    letras_filtradas = []
    index = 0
    for letra_cant in cant_por_letra:
        primer_letra = palabras[index][0] if palabras[index][0] not in ACENTOS else palabra_sin_tilde(palabras[index][0])
        if primer_letra in letras_seleccionadas:
            lista_filtrada.extend(palabras[index:(index+letra_cant[CANT])])
            letras_filtradas.append(letra_cant)
        index += letra_cant[CANT]
    return lista_filtrada, letras_filtradas

def seleccionar_palabra(diccionario_palabras, letras_participantes, cant_por_letra):
    '''
    Función: seleccionar_palabra
    Pre: La lista y el diccionario deben estar cargados previamente.
    Parámetros: - diccionario_palabras: Diccionario cargado con las palabras como claves y sus difiniciones como valores.
                - letras_participantes: Lista de 10 letras aleatorias.
                - cant_por_letra: Lista que contiene sublistas con cada letra del abecedario y la cantidad de palabras que comiencen con esa letra.
    Salida: Devolverá palabras aleatorias con su definición que empiecen con cada letra de la lista de letras al azar.
    Autores: Valentín Marturet / Renato Villalba
    '''

    palabras_seleccionadas = []

    claves = sorted(diccionario_palabras.keys(), key=(lambda clave: palabra_sin_tilde(clave[0]) if clave[0] in ACENTOS else clave[0]))
    claves_filtradas, letras_filtradas = filtrar_palabras(claves, cant_por_letra, letras_participantes)
    CANT = 1
    indice = 0

    for cant in letras_filtradas:
        rand = random.randrange(indice, indice+cant[CANT])
        palabra = [claves_filtradas[rand], diccionario_palabras[claves_filtradas[rand]]]
        palabras_seleccionadas.append(palabra)
        indice += cant[CANT]

    # palabras_seleccionadas.sort()
    return palabras_seleccionadas


def etapa3_test():

    lista_letras = ['a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    diccionario_palabras = crear_diccionario()
    cant_por_letra = total_de_palabras(diccionario_palabras)
    cant_por_letra = sorted(cant_por_letra.items(), key = lambda x:x[0])

    for i in range(0,100):
        letras_seleccionadas = crear_lista_letras(lista_letras)
        palabras_definiciones = seleccionar_palabra(diccionario_palabras, letras_seleccionadas, cant_por_letra)

        print(letras_seleccionadas)
        for palabra in palabras_definiciones:
            print(palabra[0] + ",", end="")
        print("")

etapa3_test()
