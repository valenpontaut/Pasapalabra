from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import csv

def crear_root():
    """ 
    Función: crear_root
    Parámetros: -
    Salidas:
        - root: raiz necesaria para la interfaz
    Precondiciones: Se debe correr el programa
    Postcondiciones: Devuelve el root necesario para la interfaz
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """
    root = Tk()
    root.title('Pasapalabra')
    root.resizable(0, 0)
    root.geometry('1000x800')
    root.iconbitmap('img/nerd.ico')
    root.config(bg= '#e74546')
    return root

def crear_frame(root):
    """ 
    Función: crear_frame
    Parámetros: 
        - root: es la raiz configurada previamente
    Salidas: 
        - frame: contendrá logo, botones y toda la información visual de la interfaz
    Precondiciones: Se debe correr el programa
    Postcondiciones: Devolverá el frame con el que se trabajará a futuro
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """
    frame = Frame(root, width = 900, height = 700)
    frame.config(bg = 'white')
    frame.pack(pady=50)
    return frame

def mensaje_de_inicio(root, frame, lista_jugadores):
    """ 
    Función: mensaje_de_inicio
    Parámetros: 
        - root: es la raiz configurada previamente
        - frame: frame configurado previamente
        - lista_jugadores: es una lista vacía a la que se le van a ir agregando los jugadores que se van ingresando
    Salidas: -
    Precondiciones: Se debe correr el programa
    Postcondiciones: Muestra el mensaje para empezar el juego con los botones iniciar y salir
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """
    
    titulo = Label(frame, text = '¡Pasapalabra!')
    titulo.config(bg = 'white', fg='#6585c2', font = ("Lucida Console", 60))
    titulo.place(x = 140, y = 100)

    img = Image.open("img/logo_pasapalabra.png")
    img = img.resize((600, 300))
    img = ImageTk.PhotoImage(img)
    logo = Label(frame, image=img, borderwidth=0, highlightthickness=0)
    logo.image = img
    logo.place(x = 150, y = 250)

    boton_inicio = Button(frame, text = 'Jugar', font = ("Lucida Console", 15), fg='white', command = lambda : login_usuarios(root, frame, lista_jugadores), bg= '#f29434')
    boton_inicio.place(x = 300, y = 600, width = 100, height = 50)

    boton_salir = Button(frame, text = 'Salir', font = ("Lucida Console", 15), fg='white', command = lambda : salir(root, lista_jugadores), bg= '#f29434')
    boton_salir.place(x = 500, y = 600, width = 100, height = 50)

def salir(root, lista_jugadores):
    """ 
    Función: salir
    Parámetros: 
        - root: es la raiz configurada previamente
        - lista_jugadores: es la lista de jugadores ingresados hasta el momento
    Salidas: -
    Precondiciones: Se debe haber clickeado el botón "salir"
    Postcondiciones: Cierra el juego
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """
    lista_jugadores.clear()
    root.destroy()

def login_usuarios(root, frame, lista_jugadores):
    """ 
    Función: login_usuarios
    Parámetros: 
        - root: es la raiz configurada previamente
        - frame: frame configurado previamente
        - lista_jugadores: es una lista vacía a la que se le van a ir agregando los jugadores que se van ingresando
    Salidas: -
    Precondiciones: Se debe elegir la opción de iniciar juego
    Postcondiciones: Muestra la ventana para acceder un usuario o crear en caso de que no exista
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """

    frame.destroy()
    
    frame_usuarios = Frame(root, width = 900, height = 700)
    frame_usuarios.config(bg = 'white')
    frame_usuarios.pack(pady=50)

    titulo_login = Label(frame_usuarios, text = 'Ingrese los jugadores\nque van a participar')
    titulo_login.config(bg = 'white', fg='#6585c2', font = ("Lucida Console", 30))
    titulo_login.place(x = 200, y = 100)

    label_usuario = Label(frame_usuarios, text = 'Usuario: ', bg = 'white', fg = "#6585c2", justify = RIGHT, font = ("Lucida Console", 15))
    label_usuario.place(x = 225, y = 300, width = 200, height = 30)
    input_usuario = Entry(frame_usuarios, bg = "white", fg = "#f29434", justify = LEFT, font = ("Lucida Console", 15))
    input_usuario.place(x = 420, y = 300, width = 200, height = 30)

    label_clave = Label(frame_usuarios, text = 'Clave: ', bg = 'white', fg = "#6585c2", justify = RIGHT, font = ("Lucida Console", 15))
    label_clave.place(x = 225, y = 350, width = 200, height = 30)
    input_clave = Entry(frame_usuarios, bg = "white", fg = "#f29434", justify = LEFT, font = ("Lucida Console", 15))
    input_clave.place(x = 420, y = 350, width = 200, height = 30)
    input_clave.config(show = '*')

    boton_de_registro = Button(frame_usuarios, text = 'Registrarse', fg = "white", font = ("Lucida Console", 13), command = lambda : registro_nuevo(root, lista_jugadores), bg= '#f29434')
    boton_de_registro.place(x = 275, y = 500, width = 150, height = 50)

    boton_ingreso = Button(frame_usuarios, text = 'Ingresar', command = lambda : validar_ingreso(root, input_usuario, input_clave, lista_jugadores), fg = "white", font = ("Lucida Console", 13), bg= '#f29434')
    boton_ingreso.place(x = 475, y = 500, width = 150, height = 50)

    boton_iniciar_partida = Button(frame_usuarios, text = 'Iniciar\npartida', fg = "white", font = ("Lucida Console", 13), command = lambda : iniciar_juego(root, lista_jugadores), bg= '#f29434')
    boton_iniciar_partida.place(x = 275, y = 570, width = 150, height = 50)

    boton_salir = Button(frame_usuarios, text = 'Salir', fg = "white", font = ("Lucida Console", 13), command = lambda : salir(root, lista_jugadores), bg= '#f29434')
    boton_salir.place(x = 475, y = 570, width = 150, height = 50)

def registro_nuevo(root, lista_jugadores):
    """ 
    Función: registro_nuevo
    Parámetros: 
        - root: es la raiz configurada previamente
        - lista_jugadores: es la lista de jugadores ingresados hasta el momento
    Salidas: -
    Precondiciones: 
    Postcondiciones: Crea un nuevo usuario con una nueva clave con sus validaciones respectivas
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """

    registro_usuario = Tk()
    registro_usuario.title('Crear nuevo usuario')
    registro_usuario.resizable(0, 0)
    registro_usuario.geometry('400x550')
    registro_usuario.config(bg = 'white')
    registro_usuario.iconbitmap('img/signin.ico')

    titulo_registro = Label(registro_usuario, text = 'Registro de\nusuarios')
    titulo_registro.config(bg = 'white', fg='#6585c2', font = ("Lucida Console", 30))
    titulo_registro.place(x = 70, y = 50)

    usuario = StringVar()
    clave = StringVar()
    confirmar_clave = StringVar()

    usuario_nuevo = Label(registro_usuario, text = 'Nuevo usuario:', bg = 'white', fg = '#6585c2', justify = "left", font = 5)
    usuario_nuevo.place(x = 75, y = 160)
    input_usuario = Entry(registro_usuario, textvariable = usuario, bg = "white", fg = "#f29434", justify = "left", font = 5)
    input_usuario.place(x = 75, y = 200, width = 250, height = 30)

    clave_nueva = Label(registro_usuario, text = 'Nueva clave:', bg = 'white', fg = '#6585c2', justify = "left", font = 5)
    clave_nueva.place(x = 75, y = 240)
    input_clave = Entry(registro_usuario, textvariable = clave, bg = "white", fg = "#f29434", justify = "left", font = 5)
    input_clave.place(x = 75, y = 280, width = 250, height = 30)
    input_clave.config(show = '*')

    confirmacion_clave = Label(registro_usuario, text = 'Confirmar clave:', bg = 'white', fg = '#6585c2', justify = "left", font = 5)
    confirmacion_clave.place(x = 75, y = 320)
    input_confirmacion_clave = Entry(registro_usuario, textvariable = confirmar_clave, bg = "white", fg = "#f29434", justify = "left", font = 5)
    input_confirmacion_clave.place(x = 75, y = 360, width = 250, height = 30)
    input_confirmacion_clave.config(show = '*')

    boton_confirmar = Button(registro_usuario, text = 'Confirmar', bg= '#f29434', font = ("Lucida Console", 13), fg = "white", command = lambda : verificar_datos(root, registro_usuario, input_usuario, input_clave, input_confirmacion_clave, lista_jugadores))
    boton_confirmar.place(x = 80, y = 450, width = 110, height = 40)

    boton_cancelar = Button(registro_usuario, text = 'Cancelar', font = ("Lucida Console", 13), fg = "white", command = registro_usuario.destroy, bg= '#f29434')
    boton_cancelar.place(x = 210, y = 450, width = 110, height = 40)


def verificar_datos(root, registro_usuario, input_usuario, input_clave, input_confirmacion_clave, lista_jugadores):
    """ 
    Función: verificar_datos
    Parámetros: 
        - root: es la raiz configurada previamente
        - registro_usuario: es el frame de regitro de usuarios
        - input_usuario: es el nombre de usuario ingresado para validación
        - input_clave: es la clave ingresada para validación
        - input_confirmacion_clave: es la confirmación de clave ingresada
        - lista_jugadores: es la lista de jugadores ingresados hasta el momento
    Salidas: -
    Precondiciones: se debe haber clickeado la opción de "confirmar" cuando se está registrando un nuevo usuario
    Postcondiciones: Si los datos ingresados tienen un error devolverá un mensaje de advertencia y si no, un mensaje de que el usuario se ha creado con éxito
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """
    LONG_USUARIO_MIN = 4
    LONG_USUARIO_MAX = 20
    LONG_CLAVE_MIN = 6
    LONG_CLAVE_MAX = 12
    MAX_JUGADORES = 4

    archivo_usuarios = open('usuarios.csv', 'a+', newline = '')
    writer = csv.writer(archivo_usuarios, delimiter = ',', skipinitialspace= True)
    usuario_1 = input_usuario.get()
    clave_1 = input_clave.get()
    clave_2 = input_confirmacion_clave.get()

    usuario_valido = True
    clave_valida = True
    numeros = 0
    mayusc = 0
    minusc = 0
    caracteres_especiales = 0
    letras_acentuadas = ['á', 'é', 'í','ó', 'ú']
    
    # Validación del nombre de usuario
    if LONG_USUARIO_MIN <= len(usuario_1) <= LONG_USUARIO_MAX:
        i = 0
        while usuario_valido == True and i < len(usuario_1):
            caracter = usuario_1[i]
            if not (caracter.isalpha() or caracter.isnumeric() or caracter == '-'):
                messagebox.showwarning('Error', 'El usuario puede estar formado sólo por letras, números y/o el guión medio')
                usuario_valido = False
            i += 1
    else:
        messagebox.showwarning('Error', 'El usuario debe tener una longitud mínima de 4 caracteres y máxima de 20')

    # Validación de clave
    if LONG_CLAVE_MIN <= len(clave_1) <= LONG_CLAVE_MAX:
        if clave_1 != clave_2:
            clave_valida = False
            messagebox.showwarning('Error', 'No coinciden las claves')
        i = 0
        while clave_valida == True and i < len(clave_1):
            if caracter.isupper():
                mayusc += 1
            elif caracter.islower():
                minusc += 1
            elif caracter.isnumeric():
                numeros += 1
            elif caracter == '#' or caracter == '!':
                caracteres_especiales += 1
            elif caracter in letras_acentuadas:
                messagebox.showwarning('Error', 'La clave no puede contener letras acentuadas')
                clave_valida = False
            else:
                messagebox.showwarning('Error', 'La clave solo puede estar compuesta por caracteres alfanuméricos no acentuados y por "#" o "!"')
                clave_valida = False
            i += 1
        if clave_valida and (mayusc == 0 or minusc == 0 or numeros == 0 or caracteres_especiales == 0):
            messagebox.showwarning('Error', 'La clave debe contener al menos una letra mayúscula, una letra minúscula, un número, y alguno de los caracteres "#" o "!"')                      
            clave_valida = False
    else:
        clave_valida = False
        messagebox.showwarning('Error', 'La clave debe tener una longitud mínima de 6 caracteres y máxima de 12')

    # Validar existencia de usuario en 'usuarios.csv'
    if usuario_valido and clave_valida:
        archivo_usuarios.seek(0)
        usuarios_creados = [fila.split(',')[0] for fila in archivo_usuarios]
        if usuario_1 in usuarios_creados:
            messagebox.showinfo('Aviso', 'El usuario ya existe')
        else:
            writer.writerow([usuario_1, clave_1])
            lista_jugadores.append(usuario_1)
            messagebox.showinfo('Registro Exitoso', 'El usuario fue registrado exitosamente.')
            archivo_usuarios.close()
            registro_usuario.destroy()
            if len(lista_jugadores) >= MAX_JUGADORES:
                messagebox.showinfo('Aviso', 'Se han alcanzado el máximo de participantes posibles')
                iniciar_juego(root, lista_jugadores)
    archivo_usuarios.close()

MAX_REGISTRO = [0, 9999999]

def obtener_linea(archivo_usuarios):
    """ 
    Función: obtener_linea
    Parámetros: 
        - archivo_usuarios: representa el archivo de usuarios "usuarios.csv" ya abierto
    Salidas: 
        - registro: es una lista con el usuario y la clave leídos en una linea del archivo de usuarios
    Precondiciones: se debe haber abierto el archivo
    Postcondiciones: lea una linea del archivo pasado como parámetro
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """
    linea = archivo_usuarios.readline()
    registro = []
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = MAX_REGISTRO
    return registro

def validar_ingreso(root, input_usuario, input_clave, lista_jugadores):
    """ 
    Función: validar_ingreso
    Parámetros: 
        - root: es la raiz configurada previamente
        - input_usuario: es el nombre de usuario ingresado para validación
        - input_clave: es la clave ingresada para validación
        - lista_jugadores: es la lista de jugadores ingresados hasta el momento
    Salidas: -
    Precondiciones: Se debe estar ingresando un usuario 
    Postcondiciones: Validar el ingreso de un jugador que ya fue ingresado previamente
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """
    MAX_JUGADORES = 4
    archivo_usuarios = open('usuarios.csv', 'r')
    linea = obtener_linea(archivo_usuarios)
    usuario_ingresado = input_usuario.get()
    clave_ingresada = input_clave.get()
    usuario, clave = linea
    valido = False

    while usuario and valido == False:
        if usuario_ingresado == usuario and clave_ingresada == clave:
            lista_jugadores.append(usuario)
            messagebox.showinfo('Acceso', 'Usuario ingresado con éxito')
            input_usuario.delete(0, END)
            input_clave.delete(0, END)
            if len(lista_jugadores) >= MAX_JUGADORES:
                messagebox.showinfo('Aviso', 'Se han alcanzado el máximo de participantes posibles')
                iniciar_juego(root, lista_jugadores)
                valido = True
            valido = True
        linea = obtener_linea(archivo_usuarios)
        usuario, clave = linea

    if usuario_ingresado in lista_jugadores and not valido:
        messagebox.showwarning('Incorrecto', 'Usuario ya ingresado')
    elif not valido:
        messagebox.showwarning('Incorrecto', 'Usuario y/o clave inválida')

def iniciar_juego(root, lista_jugadores):
    """ 
    Función: iniciar_juego
    Parámetros: 
        - root: es la raiz configurada previamente
        - lista_jugadores: es la lista de jugadores ingresados hasta el momento
    Salidas: -
    Precondiciones: Se debe haber alcanzado el máximo de jugadores posibles o haber clickeado "iniciar juego" 
    Postcondiciones: Cierra la interfaz devolviendo la lista de jugadores para que comience el juego
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """
    if len(lista_jugadores):
        messagebox.showinfo("Pasapalabra", "El juego esta por comenzar.")
        root.destroy()
    else:
        messagebox.showwarning('Error', 'Debe haber ingresado al menos un usuario.')

def main():
    """ 
    Función: main
    Parámetros: -
    Salidas: -
    Precondiciones: Se debe correr el programa
    Postcondiciones: Es la funcion principal, por acá comienza a correr el código. Creación de interfaz
    Autores: Renato Villalba / Valentin Marturet / Valentina Llanos Pontaut
    """
    root = crear_root()
    frame = crear_frame(root)
    lista_participantes = []
    mensaje_de_inicio(root, frame, lista_participantes)
    root.mainloop()
    print("Lista de jugadores participantes:", lista_participantes)

# main()