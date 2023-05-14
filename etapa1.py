""" 
Función: validar_confirmacion
Parámetros: confirmacion
Precondiciones: ??
Postcondiciones: Valida que la respuesta del usuario sea estrictamente si o no
@author: Valentina Llanos Pontaut
"""
def validar_confirmacion(confirmacion):
    while confirmacion.lower() != "si" and confirmacion.lower() != "no":
        print("\nRespuesta inválida. Inténtelo de nuevo")
        confirmacion = input("¿Desea jugar nuevamente? (si/no): ")
    return confirmacion

""" 
Función: validar_intento
Parámetros: intento,largo_palabra
Precondiciones: ??
Postcondiciones: Valida que el intento ingresado sea compuesto unicamente por letras, no están permitidos los números, espacios ni ningún carácter especial, y que sea de la longitud correcta para el turno
@author: Valentina Llanos Pontaut
"""
def validar_intento(intento,largo_palabra):
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
    return intento

""" 
Función: comparar_intento
Parámetros: intento,palabra,resultados,letra,aciertos,errores
Precondiciones: ??
Postcondiciones: Compara que el intento ingresado por el usuario coincida con la palabra a adivinar, en el caso favorable guarda en el diccionario 'resultados' el acierto como "a" y el error como "e"
@author: Valentina Llanos Pontaut
"""
def comparar_intento(intento,palabra,resultados,letra,aciertos,errores):   
    if (intento == palabra):
        resultados[letra] = "a"
        aciertos += 1
        print("¡Correcto!")
    else:
        resultados[letra] = "e"
        errores += 1
        print(f"Incorrecto :( La palabra correcta es: {palabra}")
    return resultados,aciertos,errores

""" 
Función: imprimir_rosco
Parámetros: letras,resultados
Precondiciones: ??
Postcondiciones: muestra en pantalla el tablero con las letras participantes y los aciertos/errores de cada una
@author: Valentina Llanos Pontaut
"""
def imprimir_rosco(letras,resultados):
    print("")
    for letra in letras:
        print(f"[{letra.upper()}]", end = "")
    print("")
    for letra in letras:
        if letra in resultados.keys():
            print(f"[{resultados[letra]}]",end = "")
        else:
            print("[ ]",end = "")

""" 
Función: agregar_resultado_final
Parámetros: resultado_final,letra,intento,palabra,resultados
Precondiciones: ??
Postcondiciones: Agrega una linea nueva a 'resultado_final' que indica lo correspondiente a si fue un acierto o un error
@author: Valentina Llanos Pontaut
"""
def agregar_resultado_final(resultado_final,letra,intento,palabra,resultados):
    resultado_final += f"Turno letra {letra.upper()} - {intento} - "
    if resultados[letra] == "a":
        resultado_final += "acierto\n"
    else: 
        resultado_final += f"error - Palabra Correcta: {palabra}\n"
    return resultado_final

""" 
Función: desarrollar_juego
Parámetros: letras,definiciones
Precondiciones: ??
Postcondiciones: desarrolla el juego imprimiendo el rosco, mostrando aciertos/errores, definiciones y el resultado final del juego
@author: Valentina Llanos Pontaut
"""
def desarrollar_juego(letras,definiciones):
    CANT_LETRAS = len(letras) 
    aciertos = 0
    errores = 0
    resultados = {}
    resultado_final = ""
    for i in range (CANT_LETRAS):
        letra_turno_actual = letras[i]
        palabra = definiciones[i][0]
        definicion = definiciones[i][1]
        imprimir_rosco(letras,resultados)
        print(f"\n\nAciertos: {aciertos}\nErrores: {errores}")
        print(f"Turno letra {letra_turno_actual.upper()} - Palabra de {len(palabra)} letras")
        print(f"Definición: {definicion}")
        intento = input("Ingrese palabra: ")
        intento = validar_intento(intento,len(palabra))
        resultados,aciertos,errores = comparar_intento(intento,palabra,resultados,letra_turno_actual,aciertos,errores)
        resultado_final = agregar_resultado_final(resultado_final,letra_turno_actual,intento,palabra,resultados)
    imprimir_rosco(letras,resultados)
    print(f"\n\n{resultado_final}")
    print(f"Puntaje final: {aciertos}\n")

""" 
Función: iniciar_juego
Parámetros: -
Precondiciones: ??
Postcondiciones: desarrolla todo el juego y devuelve si el usuario desea o no seguir participando 
@author: Valentina Llanos Pontaut
"""
def iniciar_juego():
    letras_participantes = ["a","c","d","g","i","l","m","p","s","v"] #Traer letras de Etapa3
    definiciones = [["arbol","def arbol"],["casa","def casa"],["dado","def dado"],["gato","def gato"],["isla","def isla"],["loco","def loco"],["manteca","def manteca"],["pescado","def pescado"],["sapo","def sapo"],["vaso","def vaso"]] #Traer definiciones de Etapa3
    desarrollar_juego(letras_participantes,definiciones)
    confirmacion = input("¿Desea jugar nuevamente? (si/no): ")
    confirmacion = validar_confirmacion(confirmacion)
    return confirmacion

""" 
Función: main
Parámetros: - 
Precondiciones: ???
Postcondiciones: Es la funcion principal, por acá comienza a correr el código. Inicia el juego
@author: Valentina Llanos Pontaut
"""
def main():
    print("¡Bienvenido al juego Pasapalabra!\n\nA continuación le mostraremos una serie de letras participantes de las cuales deberá intentar adivinar a qué palabra se está refiriendo leyendo su definición.\nDebajo de las letras podrá observar cuáles va acertando \"a\" o cuales va errando \"e\".\n\n¡Mucha suerte!")
    confirmacion = iniciar_juego()
    while confirmacion == "si":
        confirmacion = iniciar_juego()
    print("\n¡Gracias por participar!")

main()


