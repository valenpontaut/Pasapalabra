from etapa1_etapa5 import iniciar_juego 
from etapa2 import crear_diccionario, total_de_palabras
from etapa3 import crear_lista_letras, seleccionar_palabra

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
    while confirmacion == "si":
        letras_participantes = crear_lista_letras(letras)
        definiciones = seleccionar_palabra(diccionario_palabras, letras_participantes, cant_por_letra)
        confirmacion,puntaje_final = iniciar_juego(letras_participantes,definiciones,puntaje_final)
    print("\n¡Gracias por participar!")

main()