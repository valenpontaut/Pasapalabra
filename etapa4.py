from etapa1_etapa5 import iniciar_juego
from etapa2 import crear_diccionario, total_de_palabras
from etapa3 import crear_lista_letras, seleccionar_palabra

def volver_a_jugar(confirmacion,puntaje_final,letras,diccionario_palabras,cant_por_letra):
    """ 
    Función: volver_a_jugar
    Parámetros: 
        confirmacion: es un string proveniente de un input en donde el usuario expresa deseo de jugar de nuevo o no
        puntaje_anterior: es un integer que representa el puntaje acumulado de juegos anteriores
        letras: es una lista con todas las letras del abecedario
        diccionario_palabras: Es un diccionario tipo {"palabra1":"def palabra1", "palabra2":"def palabra2", ... }
        cant_por_letra: Es una lista que tiene sublista con cada letra del abecedario y la cantidad de palabras que hay con esa letra en diccionario_palabras
    Salidas: -
    Precondiciones: Se debe haber jugado al menos una partida completa
    Postcondiciones: si el jugador desea jugar otra partida, crea aleatoriamente un nuevo rosco e inicia un nuevo juego con el.
    Autor: Valentina Llanos Pontaut
    """
    while confirmacion == "si":    
        letras_participantes = crear_lista_letras(letras)
        definiciones = seleccionar_palabra(diccionario_palabras, letras_participantes, cant_por_letra)
        confirmacion,puntaje_final = iniciar_juego(letras_participantes,definiciones,puntaje_final)

def main():
    """ 
    Función: main
    Parámetros: - 
    Salidas: -
    Precondiciones: Se debe correr el programa
    Postcondiciones: Es la funcion principal, por acá comienza a correr el código. Inicia el juego
    Autores: Francisco Albinati, Renato Samuel Villalba Manoslavas, Valentin Marturet, Valentin Valle, Valentina Llanos Pontaut
    """
    print("¡Bienvenido al juego Pasapalabra!\n\nA continuación le mostraremos una serie de letras participantes de las cuales deberá intentar adivinar a qué palabra se está refiriendo leyendo su definición.\nDebajo de las letras podrá observar cuáles va acertando \"a\" o cuales va errando \"e\".\n\n¡Mucha suerte!")
    letras = ['a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # 1. Generación del diccionario de palabras
    diccionario_palabras = crear_diccionario()
    cant_por_letra = total_de_palabras(diccionario_palabras)
    cant_por_letra = sorted(cant_por_letra.items(), key = lambda x:x[0])
    # 2. Selección de las 10 letras participantes
    letras_participantes = crear_lista_letras(letras)
    # 3.  Selección al azar de la lista de palabras a adivinar por el jugador
    definiciones = seleccionar_palabra(diccionario_palabras, letras_participantes, cant_por_letra)
    # 4. Armado del tablero y comienzo de la partida
    confirmacion,puntaje_final = iniciar_juego(letras_participantes,definiciones)
    volver_a_jugar(confirmacion,puntaje_final,letras,diccionario_palabras,cant_por_letra)
    print("\n¡Gracias por participar!")

main()