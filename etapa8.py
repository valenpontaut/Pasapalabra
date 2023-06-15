
def extraer_numero_configuracion(configuracion):
    configuracion = configuracion.split(",")
    return configuracion[1]

def cargar_valores(ruta_configuracion):
    with open(ruta_configuracion,"r",encoding='utf-8') as configuracion:
        LONG_MIN = int(extraer_numero_configuracion(configuracion.readline().rstrip("\n")))
        CANTIDAD_LETRAS_ROSCO = int(extraer_numero_configuracion(configuracion.readline().rstrip("\n")))
        MAXIMO_PARTIDAS = int(extraer_numero_configuracion(configuracion.readline().rstrip("\n")))
        PUNTAJE_ACIERTO = int(extraer_numero_configuracion(configuracion.readline().rstrip("\n")))
        PUNTAJE_DESACIERTO = int(extraer_numero_configuracion(configuracion.readline().rstrip("\n")))
    return LONG_MIN,CANTIDAD_LETRAS_ROSCO,MAXIMO_PARTIDAS,PUNTAJE_ACIERTO,PUNTAJE_DESACIERTO       
    
LONG_MIN, CANTIDAD_LETRAS_ROSCO, MAXIMO_PARTIDAS, PUNTAJE_ACIERTO, PUNTAJE_DESACIERTO = cargar_valores("configuaracion.txt")

def crear_archivo_palabras_seleccionadas(diccionario):
    PALABRA = 0
    DEFINICION = 1
    lista_palabras = list(diccionario.items())
    lista_palabras.sort(key = lambda x : x[0])                  
    with open("diccionario.csv", "w", encoding='utf-8') as palabras_filtradas:
        for palabra in lista_palabras:
            palabras_filtradas.write(f"{palabra[PALABRA]}, '{palabra[DEFINICION]}'\n")
    
def cargar_palabras_definiciones(ruta_palabras,ruta_definiciones):
    diccionario_palabras = {}

    with open(ruta_palabras, "r", encoding='utf-8') as palabras:
        with open(ruta_definiciones, "r", encoding='utf-8') as definiciones:  
                palabra = palabras.readline().rstrip("\n")
                definicion = definiciones.readline().rstrip("\n")

                while palabra != "":
                    if len(palabra) > LONG_MIN:
                        diccionario_palabras[palabra] = definicion
                    palabra = palabras.readline().rstrip("\n")
                    definicion = definiciones.readline().rstrip("\n")  
                crear_archivo_palabras_seleccionadas(diccionario_palabras)
               
    return (diccionario_palabras)

cargar_palabras_definiciones("palabras.txt","definiciones.txt")



