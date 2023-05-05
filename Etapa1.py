""" Inicialmente, comenzaremos por mostrar el tablero con las letras parti-
cipantes, debajo de cada letra se mostrará el resultado de haber adivinado 
la palabra de dicha letra, siendo “a” de acierto, o bien “e” de error.
    Al usuario se le debe indicar el turno actual, la cantidad de letras de
la palabra a adivinar y la definición de la misma.
    Una vez que el usuario ingrese la palabra se le indicará si fue correcta
o no , y en el caso de ser incorrecta se le muestra la palabra correcta, y 
luego se pasa al siguiente turno de letra.
    Cuando la palabra es ingresada por el usuario debe validarse que esté 
compuesta sólo por letras, no están permitidos los números, espacios ni nin-
gún carácter especial, y que sea de la longitud correcta para el turno.
(ver imgs)
    Una vez que finalizaron los turnos se debe indicar todo el resumen de la
 partida con el puntaje final:
 """

""" 
Función:
Parámetros:
Precondiciones:
Postcondiciones:
@author: Valentina Llanos Pontaut
"""

letras_participantes = ["A","C","D","G","I","L","M","P","S","V"]

resultados = {}
for letra in letras_participantes:
    print(f"[{letra}]", end = "")

