import random

def obtener_letras_particip(CANT_LETRAS):
    '''
    Función: obtener_letras_particip
    Parámetros: 
        - CANT_LETRAS: Es un integer constante que representa cuántas letras conformarán el rosco. Éste valor se obtiene de configuracion
    Salida: 
        - letras_particip: Es una lista de una selección aleatoria de letras del abecedario del largo indicado por parámetro
    Precondiciones: Se debe haber leido correctamente las configuraciones el juego y haber iniciado una partida nueva
    Postcondiciones: Crea una lista con las letras participantes del rosco
    Autores: Valentín Marturet / Renato Villalba / Valentina Llanos Pontaut
    '''
    LETRAS = ['a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letras_particip = random.sample(LETRAS, CANT_LETRAS)
    letras_particip.sort()    
    return letras_particip

def obtener_palabras_definiciones_particip(lista_palabra_definicion, letras_participantes, palabras_por_letra):
    '''
    Función: obtener_palabras_definiciones_particip
    Parámetros: 
        - lista_palabra_definicion: Es una lista de tuplas tipo [("palabra1","def palabra1"),("palabra2","def palabra2"),( ... ), ... ]
        - letras_participantes: Lista de letras participantes del rosco seleccionadas aleatoriamente
        - palabras_por_letra: Lista de tuplas con cada letra del abecedario en posición 0 y la cantidad de palabras que comiencen con esa letra en posición 1.
    Salida: 
        - palabras_definiciones_seleccionadas: es una lista de tuplas cuyas tuplas contienen las palabras y definiciones participantes del rosco seleccionadas aleatoriamente
    Precondiciones: Las listsa deben estar cargados previamente.
    Postcondiciones: Obtencion de las palabras y definiciones que van a pertenecer a las letras participantes del rosco
    Autores: Valentín Marturet / Renato Villalba / Valentina Llanos Pontaut
    '''
    PALABRA = 0
    DEFINICION = 1
    LETRA = 0
    CANTIDAD = 1
    indice = 0
    palabras_definiciones_seleccionadas = []
    for letra_cantidad in palabras_por_letra:
        letra = letra_cantidad[LETRA] 
        if letra in letras_participantes:
            indice_random = random.randrange(indice, indice+letra_cantidad[CANTIDAD])
            palabras_definiciones_seleccionadas.append([lista_palabra_definicion[indice_random][PALABRA], lista_palabra_definicion[indice_random][DEFINICION]])
        indice += letra_cantidad[CANTIDAD]
    return palabras_definiciones_seleccionadas