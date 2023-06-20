import random
from login import mensaje_de_inicio, crear_root, crear_frame
from rosco import obtener_letras_particip, obtener_palabras_definiciones_particip
from configuracion import obtener_config
from palabras_y_definiciones import obtener_lista_palabra_definicion, obtener_palabras_por_letra

def validar_confirmacion(confirmacion):
    """ 
    Función: validar_confirmacion
    Parámetros: 
        confirmacion: Es un string proveniente de un input en donde el/los usuario/s expresa/n deseo de jugar de nuevo o no
    Salidas: 
        confirmacion: "si" si el/los jugador/es desea/n jugar nuevamente, "no" si el/los jugador/es desea/n no jugar más
    Precondiciones: Se debe haber jugado al menos toda una partida (o rosco)
    Postcondiciones: Valida que la respuesta sea estrictamente si o no
    Autor: Valentina Llanos Pontaut
    """
    while confirmacion.lower() != "si" and confirmacion.lower() != "no":
        print("\nRespuesta inválida. Inténtelo de nuevo")
        confirmacion = input("¿Desea jugar nuevamente? (si/no): ")
    return confirmacion.lower()

def validar_intento(intento,largo_palabra):
    """ 
    Función: validar_intento
    Parámetros: 
        intento: Es un string proveniente de un input en donde el usuario intenta adivinar la palabra a la que su definición refiere
        largo_palabra: Es un integer que representa el largo de la palabra correcta a adivinar
    Salidas: 
        intento: String validado para poder ser posible intento de adivinar la palabra correcta
    Precondiciones: Se debe estar jugando y que sea el turno de una letra para adivinar su palabra
    Postcondiciones: Valida que el intento ingresado sea compuesto unicamente por letras, no están permitidos los números, espacios ni ningún carácter especial, y que sea de la longitud correcta para el turno
    Autor: Valentina Llanos Pontaut
    """
    es_valido = True
    error = ""
    i = 0
    if len(intento) != largo_palabra:
        error = f"\nError: El intento ingresado debe tener una longitud de {largo_palabra} letras"
        es_valido = False
    while es_valido == True and i < largo_palabra:
        caracter = intento[i]
        if caracter.isspace():
            error = "\nError: El intento iongresado no puede contener espacios"
            es_valido = False
        elif caracter.isnumeric():
            error = "\nError: El intento ingresado no puede contener numeros"
            es_valido = False
        elif not caracter.isalpha():
            error = "\nError: El intento ingresado no puede contener caracteres especiales"
            es_valido = False
        i += 1  
    print(error)
    if es_valido == False:
        intento = input("Por favor ingrese nuevamente la palabra: ")
        intento = validar_intento(intento,largo_palabra)
    return intento.lower()

def comparar_intento(intento,palabra,resultados,letra,jugador_nombre,jugador_indice,puntaje_por_jugador):   
    """ 
    Función: comparar_intento
    Parámetros: 
        intento: Es un string proveniente de un input en donde el usuario intenta adivinar la palabra a la que su definición refiere
        palabra: Es un string que representa la palabra correcta a adivinar del turno actual
        resultados: Es un diccionario tipo {"letra1":[indice_jugador,"a" / "e"], "letra2":[... , ...], ... } que guarda el participante con el resultado de su intento por cada letra
        letra: Es un string que representa la letra participante del turno actual
        jugador_nombre: Es un string que representa el nombre del jugador que juega en el intento actual
        jugador_indice: Es un integer que representa el número de turno del jugador actual
        puntaje_por_jugador: Es un diccionario tipo {"jugador_1":[cant_aciertos,cant_errores], "jugador_2":[ ... , ... ], ... } donde se guardan y acumulan los aciertos y errores de cada jugador durante la partida actual
    Salidas: 
        resultados: Mismo diccionario explicado anteriormente pero con valores actualizados
        puntaje_por_jugador: Mismo diccionario explicado anteriormente pero con valores actualizados
        errores_cometidos: Devuelve un 0 si el jugador acertó a la palabra, un 1 si falló
    Precondiciones: Se debe estar jugando y que sea el turno de una letra para adivinar su palabra. El usuario debe ingresar un intento válido
    Postcondiciones: Compara que el intento ingresado por el usuario coincida con la palabra a adivinar, en el caso favorable guarda en el diccionario 'resultados' el acierto como "a" y el error como "e"
    Autor: Valentina Llanos Pontaut
    """
    ACIERTOS = 0
    ERRORES = 1
    if (intento == palabra):
        resultados[letra] = [jugador_indice,"a"]
        puntaje_por_jugador[jugador_nombre][ACIERTOS] += 1
        errores_cometidos = 0
        print("¡Correcto!\n")
    else:
        resultados[letra] = [jugador_indice,"e"]
        puntaje_por_jugador[jugador_nombre][ERRORES] += 1
        errores_cometidos = 1
        print(f"Incorrecto :( La palabra correcta es: {palabra}\n")
    return resultados,puntaje_por_jugador,errores_cometidos

def imprimir_turnos_jugadores(jugadores):
    """ 
    Función: imprimir_turnos_jugadores
    Parámetros: 
        jugadores: Es una lista con los nombres de los jugadores participantes ordenados aleatoriamente
    Salidas: -
    Precondiciones: Se deben haber logeado los participantes
    Postcondiciones: Muestra en pantalla el turno que se le asignó a cada participante
    Autor: Valentina Llanos Pontaut
    """
    print("Los turnos fueron asignados de la siguiente manera: ")
    random.shuffle(jugadores)
    for jugador_indice in range(1,len(jugadores)+1):
        print(f"{jugador_indice} - {jugadores[jugador_indice-1]}")

def imprimir_rosco(letras,resultados):
    """ 
    Función: imprimir_rosco
    Parámetros: 
        letras: Es una lista con las letras participantes del rosco ordenadas
        resultados: Es un diccionario tipo {"letra1":[indice_jugador,"a" / "e"], "letra2":[... , ...], ... } que guarda el participante con el resultado de su intento por cada letra
    Salidas: -
    Precondiciones: Se debe estar jugando
    Postcondiciones: Muestra en pantalla el tablero con las letras participantes, el índice de los jugadores que han intentado adivinar la palabra en cada turno y los aciertos/errores de cada una
    Autor: Valentina Llanos Pontaut
    """
    JUGADOR = 0
    RESULTADO = 1
    print("--------------------------------------------------------------------------------------------------------------\n")
    for letra in letras:
        print(f"[{letra.upper()}]", end = "")
    print("")
    for letra in letras:
        if letra in resultados.keys():
            print(f"[{resultados[letra][JUGADOR]}]",end = "")
        else:
            print("[ ]",end = "")
    print("")
    for letra in letras:
        if letra in resultados.keys():
            print(f"[{resultados[letra][RESULTADO]}]",end = "")
        else:
            print("[ ]",end = "")

def imprimir_puntos_jugadores(jugadores, puntaje_por_jugador):
    """ 
    Función: imprimir_puntos_jugadores
    Parámetros: 
        jugadores: Es una lista de strings que representan el nombre de cada jugador participante tipo ["jugador1","jugador2", ... ]
        puntaje_por_jugador: Es un diccionario tipo {"jugador_1":[cant_aciertos,cant_errores], "jugador_2":[ ... , ... ], ... } donde se guardan y acumulan los aciertos y errores de cada jugador durante la partida actual
    Salidas: -
    Precondiciones: Se debe estar jugando
    Postcondiciones: Muestra en pantalla los aciertos y errores de cada jugador en cada turno a medida que evoluciona la partida
    Autor: Valentina Llanos Pontaut
    """
    ACIERTOS = 0
    ERRORES = 1
    print("\n\n\nJugadores:")
    for i in range (len(jugadores)):
        jugador = jugadores[i]
        print(f"{i+1}. {jugador} - Aciertos: {puntaje_por_jugador[jugador][ACIERTOS]} - Errores: {puntaje_por_jugador[jugador][ERRORES]}")

def crear_dicc_puntaje_por_jugador(jugadores):
    """ 
    Función: crear_dicc_puntaje_por_jugador
    Parámetros: 
        jugadores: Es una lista de strings que representan el nombre de cada jugador participante tipo ["jugador1","jugador2", ... ]
    Salidas:
        puntaje_por_jugador: Es un diccionario tipo {"jugador_1":[0,0], "jugador_2":[0,0], ... } donde se van a guardar y acumular los aciertos y errores de cada jugador durante la partida actual
    Precondiciones: Debe estar jugándose la primer partida o ya se debe haber finalizado una partida anterior
    Postcondiciones: Crea un diccionario puntaje_por_jugador seteado con valores de aciertos y errores en 0 para el comienzo de una nueva partida
    Autor: Valentina Llanos Pontaut
    """
    puntaje_por_jugador = {}
    for jugador in jugadores:
        puntaje_por_jugador[jugador] = [0,0]
    return puntaje_por_jugador

def agregar_resultado_final(resultado_final,letra,intento,palabra,resultados,jugador_indice,jugador_nombre):
    """ 
    Función: agregar_resultado_final
    Parámetros: 
        resultado_final: Es un string que concatena los respectivos resultados de cada turno indicando su acierto o error
        letra: Es un string que representa la letra participante del turno actual
        intento: Es un string proveniente de un input en donde el usuario intenta adivinar la palabra a la que su definición refiere
        palabra: Es un string que representa la palabra correcta a adivinar del turno actual
        resultados: Es un diccionario tipo {"letra1":[indice_jugador,"a" / "e"], "letra2":[... , ...], ... } que guarda el participante con el resultado de su intento por cada letra
        jugador_indice: Es un integer que representa el número de turno del jugador actual
        jugador_nombre: Es un string que representa el nombre del jugador que juega en el intento actual
    Salidas: 
        resultado_final: Mismo concepto que el explicado anteriormente pero con valores actualizados
    Precondiciones: Terminar el turno de la letra que se está jugando
    Postcondiciones: Concatena una linea nueva a 'resultado_final' que indica lo correspondiente a si fue un acierto o un error
    Autor: Valentina Llanos Pontaut
    """
    RESULTADO = 1
    resultado_final += f"Turno letra {letra.upper()} - Jugador {jugador_indice} {jugador_nombre} - {intento} - "
    if resultados[letra][RESULTADO] == "a":
        resultado_final += "acierto\n"
    else: 
        resultado_final += f"error - Palabra Correcta: {palabra}\n"
    return resultado_final

def imprimir_puntaje_parcial(jugadores,puntaje_por_jugador_actual,puntaje_por_jugador_anterior,PUNTOS_ACIERTO,PUNTOS_DESACIERTO):
    """ 
    Función: imprimir_puntaje_parcial
    Parámetros:
        jugadores: Es una lista de strings que representan el nombre de cada jugador participante tipo ["jugador1","jugador2", ... ]
        puntaje_por_jugador_actual: Es un diccionario tipo {"jugador_1":[cant_aciertos,cant_errores], "jugador_2":[ ... , ... ], ... } donde se guardan y acumulan los aciertos y errores de cada jugador durante la partida actual
        puntaje_por_jugador_anterior: Es un diccionario tipo {"jugador_1":[cant_aciertos,cant_errores], "jugador_2":[ ... , ... ], ... } donde se guardan y acumulan los aciertos y errores de cada jugador durante todas las partidas que se hayan jugado previamente a la actual
        PUNTOS_ACIERTO: Es una constante de tipo integer que representa la cantidad de puntos que se reciben por acierto (proviene de configuracion.csv)
        PUNTOS_DESACIERTO: Es una constante de tipo integer que representa la cantidad de puntos que se restan por error (proviene de configuracion.csv)
    Salidas: 
        puntaje_por_jugador_anterior: Mismo diccionario explicado anteriormente pero suma sus valores a los del diccionario puntaje_por_jugador_actual
    Precondiciones: Se debe de haber finalizado de jugar una partida (o rosco)
    Postcondiciones: Imprime la puntuación de la partida de cada jugador y si ya se jugó mas de una partida imprime el puntaje parcial de cada jugador de todas las partidas jugadas hasta el momento
    """
    ACIERTOS = 0
    ERRORES = 1
    print("\nPuntaje de la partida:")
    for jugador_indice in range(1,len(jugadores)+1):
        jugador_nombre = jugadores[jugador_indice-1]
        aciertos = puntaje_por_jugador_actual[jugador_nombre][ACIERTOS]
        errores = puntaje_por_jugador_actual[jugador_nombre][ERRORES]
        print(f"{jugador_indice}. {jugador_nombre} - {aciertos * PUNTOS_ACIERTO - errores * PUNTOS_DESACIERTO} puntos")
    if puntaje_por_jugador_anterior != 0:
        print("\n\nPuntaje parcial:")
        for jugador_indice in range(1,len(jugadores)+1):
            jugador_nombre = jugadores[jugador_indice-1]
            puntaje_por_jugador_anterior[jugador_nombre][ACIERTOS] += puntaje_por_jugador_actual[jugador_nombre][ACIERTOS]
            puntaje_por_jugador_anterior[jugador_nombre][ERRORES] += puntaje_por_jugador_actual[jugador_nombre][ERRORES]
            aciertos = puntaje_por_jugador_anterior[jugador_nombre][ACIERTOS]
            errores = puntaje_por_jugador_anterior[jugador_nombre][ERRORES]
            print(f"{jugador_indice}. {jugador_nombre} - {aciertos * PUNTOS_ACIERTO - errores * PUNTOS_DESACIERTO} puntos")
    else:
        puntaje_por_jugador_anterior = puntaje_por_jugador_actual
    return puntaje_por_jugador_anterior

def imprimir_reporte_final(partidas_jugadas,jugadores,puntaje_por_jugador,PUNTOS_ACIERTO,PUNTOS_DESACIERTO):
    """ 
    Función: imprimir_reporte_final
    Parámetros:
        partidas_jugadas: Es un integer que representa el numero de partidas jugadas hasta el momento
        jugadores: Es una lista de strings que representan el nombre de cada jugador participante tipo ["jugador1","jugador2", ... ]
        puntaje_por_jugador: Es un diccionario tipo {"jugador_1":[cant_aciertos,cant_errores], "jugador_2":[ ... , ... ], ... } donde se guardan y acumulan los aciertos y errores de cada jugador durante todas las partidas que se hayan jugado
        PUNTOS_ACIERTO: Es una constante de tipo integer que representa la cantidad de puntos que se reciben por acierto (proviene de configuracion.csv)
        PUNTOS_DESACIERTO: Es una constante de tipo integer que representa la cantidad de puntos que se restan por error (proviene de configuracion.csv)
    Salidas: -
    Precondiciones: El/los jugador/es no desean jugar más partidas o se alcanzaron el máximo de partidas configuradas
    Postcondiciones: Imprime el número de partidas jugadas y la puntuación final de la/s partida/s jugada/s de cada jugador
    """
    ACIERTOS = 0
    ERRORES = 1
    print("\n\nReporte final:")
    print(f"Partidas jugadas: {partidas_jugadas}\n\n")
    print("Puntaje Final:")
    for jugador_indice in range(1,len(jugadores)+1):
        jugador_nombre = jugadores[jugador_indice-1]
        aciertos = puntaje_por_jugador[jugador_nombre][ACIERTOS]
        errores = puntaje_por_jugador[jugador_nombre][ERRORES]
        print(f"{jugador_indice}. {jugador_nombre} - {aciertos * PUNTOS_ACIERTO - errores * PUNTOS_DESACIERTO} puntos")

def iniciar_juego(jugadores,lista_palabra_definicion,palabras_por_letra,PUNTOS_ACIERTO,PUNTOS_DESACIERTO,CANT_LETRAS,MAX_PARTIDAS,errores_cometidos = 1,jugador_indice = 0,puntaje_por_jugador_anterior=0,partidas_jugadas=1):
    """ 
    Función: iniciar_juego
    Parámetros: 
        jugadores: Es una lista de strings que representan el nombre de cada jugador participante tipo ["jugador1","jugador2", ... ] 
        lista_palabra_definicion: Es una lista tipo [("palabra1","def palabra1"),("palabra2","def palabra2"),( ... ), ... ]
        palabras_por_letra: Es un diccionario que tiene como clave cada letra del abecedario y como valor la cantidad de palabras que hay con esa letra en lista_palabra_definicion
        PUNTOS_ACIERTO: Es una constante de tipo integer que representa la cantidad de puntos que se reciben por acierto (proviene de configuracion.csv)
        PUNTOS_DESACIERTO: Es una constante de tipo integer que representa la cantidad de puntos que se restan por error (proviene de configuracion.csv)
        CANT_LETRAS: Es una constante de tipo integer que representa la cantidad de letraS que van a conformar el rosco (proviene de configuracion.csv)
        MAX_PARTIDAS: Es una constante de tipo integer que representa la cantidad máxima de partidas que el/los participante/s pueden jugar (proviene de configuracion.csv)
        errores_cometidos: Es un integer que vale 0 si el jugador acertó a la palabra y 1 si falló (para la primer partida este valor vale 1)
        jugador_indice: Es un integer que representa el número de turno del jugador actual (para la primer partida este valor vale 0)
        puntaje_por_jugador_anterior: Es un diccionario tipo {"jugador_1":[cant_aciertos,cant_errores], "jugador_2":[ ... , ... ], ... } donde se guardan y acumulan los aciertos y errores de cada jugador durante todas las partidas que se hayan jugado previamente a la actual (para la primer partida este valor vale 0)
        partidas_jugadas: Es un integer que representa el numero de partidas jugadas hasta el momento (para la primer partida este valor vale 1)
    Salidas: 
        partidas_jugadas: mismo concepto que lo explicado anteriormente
        puntaje_por_jugador_anterior: Es un diccionario tipo {"jugador_1":[cant_aciertos,cant_errores], "jugador_2":[ ... , ... ], ... } donde se guardan y acumulan los aciertos y errores de cada jugador durante todas las partidas que se hayan jugado
    Precondiciones: Se debe haber iniciado una partida nueva
    Postcondiciones: Desarrolla el juego imprimiendo el rosco, mostrando aciertos/errores, definiciones y el resultado final del juego
    Autor: Valentina Llanos Pontaut
    """
    PALABRA = 0
    DEFINICION = 1 
    letras = obtener_letras_particip(CANT_LETRAS)
    palabras_y_definiciones = obtener_palabras_definiciones_particip(lista_palabra_definicion, letras, palabras_por_letra)
    puntaje_por_jugador_actual = crear_dicc_puntaje_por_jugador(jugadores)
    resultados = {}
    resultado_final = ""
    for i in range (CANT_LETRAS):
        if errores_cometidos:
            if jugador_indice == len(jugadores):
                jugador_indice = 0
            jugador_nombre = jugadores[jugador_indice]
            jugador_indice += 1 
        else:
            jugador_nombre = jugadores[jugador_indice - 1]
        letra_turno_actual = letras[i]
        palabra = palabras_y_definiciones[i][PALABRA]
        definicion = palabras_y_definiciones[i][DEFINICION]
        imprimir_rosco(letras,resultados)
        imprimir_puntos_jugadores(jugadores,puntaje_por_jugador_actual)
        print(f"\n\nTurno Jugador {jugador_indice} {jugador_nombre} - letra {letra_turno_actual.upper()} - Palabra de {len(palabra)} letras")
        print(f"Definición: {definicion}")
        intento = input("Ingrese palabra: ")
        intento = validar_intento(intento,len(palabra))
        resultados,puntaje_por_jugador_actual,errores_cometidos = comparar_intento(intento,palabra,resultados,letra_turno_actual,jugador_nombre,jugador_indice,puntaje_por_jugador_actual)
        resultado_final = agregar_resultado_final(resultado_final,letra_turno_actual,intento,palabra,resultados,jugador_indice,jugador_nombre)
    imprimir_rosco(letras,resultados)
    imprimir_puntos_jugadores(jugadores,puntaje_por_jugador_actual)
    print(f"\n{resultado_final}")
    puntaje_por_jugador_anterior = imprimir_puntaje_parcial(jugadores,puntaje_por_jugador_actual,puntaje_por_jugador_anterior,PUNTOS_ACIERTO,PUNTOS_DESACIERTO)
    if partidas_jugadas < MAX_PARTIDAS:
        confirmacion = input("\n¿Desea jugar nuevamente? (si/no): ")
        confirmacion = validar_confirmacion(confirmacion)
        if confirmacion == "si":
            partidas_jugadas += 1
            iniciar_juego(jugadores,lista_palabra_definicion,palabras_por_letra,PUNTOS_ACIERTO,PUNTOS_DESACIERTO,CANT_LETRAS,MAX_PARTIDAS,errores_cometidos,jugador_indice,puntaje_por_jugador_anterior,partidas_jugadas)
    return partidas_jugadas,puntaje_por_jugador_anterior

def main():
    """ 
    Función: main
    Parámetros: -
    Salidas: -
    Precondiciones: Se debe correr el programa
    Postcondiciones: Es la funcion principal, por acá comienza a correr el código. Inicia el juego
    Autor: Valentina Llanos Pontaut
    """

    # Inicialización de interfaz y login de jugadores
    root = crear_root()
    frame = crear_frame(root)
    jugadores = []
    mensaje_de_inicio(root, frame, jugadores)
    root.mainloop()
    
    if jugadores:
        # Lectura de configuración del juego
        config = obtener_config()
        LONG_PALABRA_MIN = config["LONGITUD_PALABRA_MINIMA"]
        CANT_LETRAS = config["CANTIDAD_LETRAS_ROSCO"]
        MAX_PARTIDAS = config["MAXIMO_PARTIDAS"]
        PUNTOS_ACIERTO = config["PUNTAJE_ACIERTO"]
        PUNTOS_DESACIERTO = config["PUNTAJE_DESACIERTO"]
    
        # Inicio de juego
        ARCHIVO_PALABRAS = "palabras.txt"
        ARCHIVO_DEFINICIONES = "definiciones.txt" 
        print("¡Bienvenido al juego Pasapalabra!\n\nA continuación le mostraremos una serie de letras participantes de las cuales deberá intentar adivinar a qué palabra se está refiriendo leyendo su definición.\nDebajo de las letras podrá observar cuáles va acertando \"a\" o cuales va errando \"e\".")
        print(f"Recuerde que por cada acierto obtiene {PUNTOS_ACIERTO} puntos y por cada error se le restan {PUNTOS_DESACIERTO} puntos.\n")
        imprimir_turnos_jugadores(jugadores)
        print("\n¡Mucha suerte!")        
        lista_palabra_definicion = obtener_lista_palabra_definicion(ARCHIVO_PALABRAS,ARCHIVO_DEFINICIONES,LONG_PALABRA_MIN)
        palabras_por_letra = obtener_palabras_por_letra(lista_palabra_definicion) 
        partidas_jugadas,puntaje_por_jugador_anterior = iniciar_juego(jugadores,lista_palabra_definicion,palabras_por_letra,PUNTOS_ACIERTO,PUNTOS_DESACIERTO,CANT_LETRAS,MAX_PARTIDAS)
        imprimir_reporte_final(partidas_jugadas,jugadores,puntaje_por_jugador_anterior,PUNTOS_ACIERTO,PUNTOS_DESACIERTO) 
        print("\n¡Gracias por participar!")
    
main()