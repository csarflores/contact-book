#Importar librería
import os

CARPETA = 'proyecto_final/contactos/' #carpeta de contactos
EXTENSION = '.txt' #extención de archivos

#Creamos la clase de Contactos
class Contacto:
    #Constructor
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():

    #Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra el menú de opciones
    mostrar_menu()

    # Preguntar al usuario la opción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida, intente nuevamente')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Eliminado correctamente')
    except Exception:
        print('No existe el contacto')

    #Reiniciar la app
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar \r\n')

    # Exepción: mensaje de error, evita que la aplicación truene.
    #try intenta abrir el archivo, si el archivo no existe o marca un error pasa automáticamente a except
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    
    #Reiniciar la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    #Recorre toda la carpeta y trae solo los .txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos
                print(linea.rstrip())
            #Imprime un separador entre los contactos
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    existe = existe_contacto(nombre_anterior)

    if existe:
        #Abrir archivo, reescribirlo y guardarlo
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            #Resto de los campos
            nombre_contacto = input('Agrega el nuevo nombre \r\n')
            telefono_contacto = input('Agrega el nuevo teléfono: \r\n')
            categoria_contacto = input('Agrega la nueva categoría: \r\n')

            #Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        #Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

        #Mostrar mensaje de éxito
        print('\r\n Contacto editado correctamente! \r\n')
    else:
        print('Ese contacto no existe')
    
    #Reiniciar app
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del Contacto \r\n')

    #Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:      
    
        #Crear el archivo cuando crea el contacto
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo: #as archivo es el nombre con el que nos vamos a referir a la extención (CARPETA + ...)

            #Resto de los campos
            telefono_contacto = input('Agrega el teléfono: \r\n')
            categoria_contacto = input('Categoría contacto: \r\n')

            #Instar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            #Mostrar mensaje de éxito
            print('\r\n Contacto creado correctamente! \r\n')
    else:
        print('Ese contacto ya existe')
    
    #Reiniciar la app si el contacto ya exite
    app()

def mostrar_menu():
    print('Seleccione del menú lo que desea hacer:')
    print('1) Agergar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA): #Comprueba si una carpeta existe, si no existe crear la carpeta

        #crear carpeta, si existe imprime alerta
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    #Revisar si el archivo ya existe antes de crearlo
    return os.path.isfile(CARPETA + nombre + EXTENSION)
    
app()