def validar_confirmacion(confirmacion):
    """ 
    Función: validar_confirmacion
    Parámetros: 
        confirmacion: es un string proveniente de un input en donde el usuario expresa deseo de jugar de nuevo o no
    Salidas: 
        confirmacion: "si" si el jugador desea jugar nuevamente, "no" si el jugador desea no jugar más
    Precondiciones: Se debe haber jugado al menos todo un juego (o rosco)
    Postcondiciones: Valida que la respuesta del usuario sea estrictamente si o no
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
        intento: es un string proveniente de un input en donde el usuario intenta adivinar la palabra a la que su definición refiere
        largo_palabra: es un integer que representa el largo de la palabra correcta a adivinar
    Salidas: 
        intento: string validado para poder ser posible intento de adivinar la palabra correcta
    Precondiciones: Se debe estar jugando y que sea el turno de una letra para adivinar su palabra
    Postcondiciones: Valida que el intento ingresado sea compuesto unicamente por letras, no están permitidos los números, espacios ni ningún carácter especial, y que sea de la longitud correcta para el turno
    Autor: Valentina Llanos Pontaut
    """
    es_valido = True
    error = ""
    i = 0
    while es_valido == True and i < largo_palabra:
        if len(intento) == largo_palabra:
            for caracter in intento:
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
        else:
            error = f"\nError: El intento ingresado debe tener una longitud de {largo_palabra} letras"
            es_valido = False
    print(error)
    if es_valido == False:
        intento = input("Por favor ingrese nuevamente la palabra: ")
        intento = validar_intento(intento,largo_palabra)
    return intento.lower()

def comparar_intento(intento,palabra,resultados,letra,aciertos,errores):   
    """ 
    Función: comparar_intento
    Parámetros: 
        intento: es un string proveniente de un input en donde el usuario intenta adivinar la palabra a la que su definición refiere
        palabra: es un string que representa la palabra correcta a adivinar del turno actual
        resultados: es un diccionario que guarda como clave cada letra participante y como valor si el participante acertó ("a") o si le erró ("e")
        letra: es un string que representa la letra participante del turno actual
        aciertos: es un integer que va acumulando la cantidad de aciertos
        errores: es un integer que va acumulando la cantidad de errores
    Salidas: 
        resultados: diccionario actualizado que guarda como clave cada letra participante y como valor si el participante acertó ("a") o si le erró ("e")
        aciertos: integer actualizado con la cantidad de aciertos acumulados
        errores: integer actualizado con la cantidad de errores acumulados
    Precondiciones: Se debe estar jugando y que sea el turno de una letra para adivinar su palabra. El usuario debe ingresar un intento válido
    Postcondiciones: Compara que el intento ingresado por el usuario coincida con la palabra a adivinar, en el caso favorable guarda en el diccionario 'resultados' el acierto como "a" y el error como "e"
    Autor: Valentina Llanos Pontaut
    """
    if (intento == palabra):
        resultados[letra] = "a"
        aciertos += 1
        print("¡Correcto!")
    else:
        resultados[letra] = "e"
        errores += 1
        print(f"Incorrecto :( La palabra correcta es: {palabra}")
    return resultados,aciertos,errores

def imprimir_rosco(letras,resultados):
    """ 
    Función: imprimir_rosco
    Parámetros: 
        letras: es una lista con las letras participantes del rosco ordenadas
        resultados: es un diccionario que guarda como clave cada letra participante y como valor si el participante acertó ("a") o si le erró ("e")
    Salidas: -
    Precondiciones: Se debe estar jugando
    Postcondiciones: Muestra en pantalla el tablero con las letras participantes y los aciertos/errores de cada una
    Autor: Valentina Llanos Pontaut
    """
    print("")
    for letra in letras:
        print(f"[{letra.upper()}]", end = "")
    print("")
    for letra in letras:
        if letra in resultados.keys():
            print(f"[{resultados[letra]}]",end = "")
        else:
            print("[ ]",end = "")

def agregar_resultado_final(resultado_final,letra,intento,palabra,resultados):
    """ 
    Función: agregar_resultado_final
    Parámetros: 
        resultado_final: es un string que concatena los respectivos resultados de cada turno indicando su acierto o error
        letra: es un string que representa la letra participante del turno actual
        intento: es un string proveniente de un input en donde el usuario intenta adivinar la palabra a la que su definición refiere
        palabra: es un string que representa la palabra correcta a adivinar del turno actual
        resultados: es un diccionario que guarda como clave cada letra participante y como valor si el participante acertó ("a") o si le erró ("e")
    Salidas: 
        resultado_final: es un string que concatena los respectivos resultados de cada turno indicando su acierto o error
    Precondiciones: Terminar el turno de la letra que se está jugando
    Postcondiciones: Concatena una linea nueva a 'resultado_final' que indica lo correspondiente a si fue un acierto o un error
    Autor: Valentina Llanos Pontaut
    """
    resultado_final += f"Turno letra {letra.upper()} - {intento} - "
    if resultados[letra] == "a":
        resultado_final += "acierto\n"
    else: 
        resultado_final += f"error - Palabra Correcta: {palabra}\n"
    return resultado_final

def imprimir_puntuacion(aciertos,errores,puntaje_anterior=0,PUNTOS_POR_ACIERTO=10,PUNTOS_POR_ERROR=-3):
    """ 
    Función: imprimir_puntuacion
    Parámetros: 
        aciertos: es un integer que representa la cantidad de aciertos que el jugador realizó durante todo el juego
        errores: es un integer que representa la cantidad de errores que el jugador realizó durante todo el juego
        puntaje_anterior: es un integer que representa el puntaje acumulado de juegos anteriores. Si es la primera vez que se juega, éste vale cero.
        PUNTOS_POR_ACIERTO: es una constante de tipo integer que representa la cantidad de puntos que se reciben por acierto (etapa 5)
        PUNTOS_POR_ERROR: es una constante de tipo integer que representa la cantidad de puntos que se restan por error (etapa 5)
    Salidas: -
    Precondiciones: Se debe de haber finalizado de jugar todo un rosco
    Postcondiciones: Imprime la puntuación final obtenida por el jugador luego de haber finalizado el rosco, con los puntos correspondientes por acierto y por error
    """
    puntaje_final = puntaje_anterior + (aciertos * PUNTOS_POR_ACIERTO) + (errores * PUNTOS_POR_ERROR)
    print(f"Puntaje final: {puntaje_final}")
    return puntaje_final

def iniciar_juego(letras,definiciones,puntaje_anterior=0):
    """ 
    Función: iniciar_juego
    Parámetros: 
        letras: es una lista con las 10 letras participantes del rosco ordenadas, elegidas al azar
        definiciones: es una lista de listas en donde cada sublista contiene en la posición 0 una palabra y en la posición 1 su definición. Las palabras seleccionadas son elegidas a partir de las letras seleccionadas.
        puntaje_anterior: es un integer que representa el puntaje acumulado de juegos anteriores. Si es la primera vez que se juega, éste vale cero.
    Salidas: 
        confirmacion: "si" si el jugador desea jugar nuevamente, "no" si el jugador desea no jugar más
    Precondiciones: Se debe haber iniciado un juego nuevo
    Postcondiciones: desarrolla el juego imprimiendo el rosco, mostrando aciertos/errores, definiciones y el resultado final del juego
    Autor: Valentina Llanos Pontaut
    """
    CANT_LETRAS = len(letras)
    PALABRA = 0
    DEFINICION = 1 
    aciertos = 0
    errores = 0
    resultados = {}
    resultado_final = ""
    for i in range (CANT_LETRAS):
        letra_turno_actual = letras[i]
        palabra = definiciones[i][PALABRA]
        definicion = definiciones[i][DEFINICION]
        imprimir_rosco(letras,resultados)
        print(f"\n\nAciertos: {aciertos}\nErrores: {errores}")
        print(f"Turno letra {letra_turno_actual.upper()} - Palabra de {len(palabra)} letras")
        print(f"Definición: {definicion}")
        intento = input("Ingrese palabra: ")
        intento = validar_intento(intento,len(palabra))
        resultados,aciertos,errores = comparar_intento(intento,palabra,resultados,letra_turno_actual,aciertos,errores)
        resultado_final = agregar_resultado_final(resultado_final,letra_turno_actual,intento,palabra,resultados)
    imprimir_rosco(letras,resultados)
    print(f"\n\nAciertos: {aciertos}\nErrores: {errores}")
    print(f"\n{resultado_final}")
    # Etapa 1 ->
    # print(f"Puntaje final: {aciertos}\n")
    # Etapa 5 ->
    puntaje_final = imprimir_puntuacion(aciertos,errores,puntaje_anterior)
    confirmacion = input("\n¿Desea jugar nuevamente? (si/no): ")
    confirmacion = validar_confirmacion(confirmacion)
    return confirmacion, puntaje_final

def main():
    """ 
    Función: main
    Parámetros: - 
    Salidas: -
    Precondiciones: Se debe correr el programa
    Postcondiciones: Es la funcion principal, por acá comienza a correr el código. Inicia el juego
    Autor: Valentina Llanos Pontaut
    """
    print("¡Bienvenido al juego Pasapalabra!\n\nA continuación le mostraremos una serie de letras participantes de las cuales deberá intentar adivinar a qué palabra se está refiriendo leyendo su definición.\nDebajo de las letras podrá observar cuáles va acertando \"a\" o cuales va errando \"e\".\nRecuerde que por cada acierto obtiene 10 puntos y por cada error se le restan 3 puntos.\n\n¡Mucha suerte!")
    # Las listas "letras_participantes" y "definiciones" se crean en la etapa 3 de manera aleatoria
    letras_participantes = ["a","c","d","g","i","l","m","p","s","v"] 
    definiciones = [["arbol","def arbol"],["casa","def casa"],["dado","def dado"],["gato","def gato"],["isla","def isla"],["loco","def loco"],["manteca","def manteca"],["pescado","def pescado"],["sapo","def sapo"],["vaso","def vaso"]]
    confirmacion,puntaje_final = iniciar_juego(letras_participantes,definiciones)
    while confirmacion == "si":
        # Las listas "letras_participantes" y "definiciones" se crean en la etapa 3 de manera aleatoria
        letras_participantes = ["b","d","e","h","j","m","n","q","t","x"]
        definiciones = [["barco","def barco"],["dinero","def dinero"],["estado","def estado"],["helado","def helado"],["jaula","def jaula"],["mono","def mono"],["nacer","def nacer"],["queso","def queso"],["tomate","def tomate"],["xilofon","def xilofon"]]
        confirmacion,puntaje_final = iniciar_juego(letras_participantes,definiciones,puntaje_final)
    print("\n¡Gracias por participar!")