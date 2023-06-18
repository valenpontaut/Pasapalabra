# CONSTANTES
OPCIONES = ["LONGITUD_PALABRA_MINIMA","CANTIDAD_LETRAS_ROSCO", "MAXIMO_PARTIDAS", "PUNTAJE_ACIERTO", "PUNTAJE_DESACIERTO"]
DEFAULT = [4, 10, 5, 10, 3]
OPCION, VALOR = 0, 1


def leer(archivo):
    """
    Función: leer
    Parametros:
        archivo: Recibe el archivo del cual se quiere leer una linea.
    Salida: Devuelve una lista con todos los elementos de una linea del archivo dado.
    Autores: Valentín Marturet
    """
    linea = archivo.readline()
    if (not(linea)):
        linea = ""
    linea = linea.rstrip()
    return linea.split(',')



def obtener_config():
    """
    Función: obtener_config
    Parametros: -
    Salida: Devuelve una lista con los valores de la configuracion
    Precondiciones: La configuracion deseada debe haber sido establecida antes de iniciar el juego
    Postcondiciones: Si se cargaron los datos correctamente, la configuracion del juego es la establecida por el usuario, de lo contrario se utiliza la configuracion por defecto
    Autores: Valentín Marturet
    """
    config = {}
    try:
        archivo = open("./configuracion.csv", "r")
        linea = leer(archivo)
        index = 0
        while index < len(OPCIONES):
            if linea[OPCION] == OPCIONES[index] and linea[VALOR].isnumeric():
                config[linea[OPCION]] = int(linea[VALOR])
            else:
                config[OPCIONES[index]] = DEFAULT[index]
            linea = leer(archivo)
            index += 1
        archivo.close()
    except FileNotFoundError:
        print("Error: Archivo de configuracion no encontrado, leyendo opciones por defecto.")
        for index in range(len(OPCIONES)):
            config[OPCIONES[index]] = DEFAULT[index]

    return config

def test():
    dicc_config = obtener_config()
    print(dicc_config)
    for clave in dicc_config:
        print(f"{clave}: {dicc_config[clave]}")

test()
