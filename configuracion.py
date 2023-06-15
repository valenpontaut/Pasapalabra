# CONSTANTES
OPCIONES = ["LONGITUD_PALABRA_MINIMA","CANTIDAD_LETRAS_ROSCO", "MAXIMO_PARTIDAS", "PUNTAJE_ACIERTO", "PUNTAJE_DESACIERTO"]
DEFAULT = [4, 10, 5, 10, 3]
OPCION, VALOR = 0, 1


def leer(archivo):
    linea = archivo.readline()
    if (not(linea)):
        linea = ""
    linea = linea.rstrip()
    return linea.split(',')



def obtener_config():
    """
    Función: obtener_config
    Salida: Devuelve una lista con los valores de la configuracion
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
