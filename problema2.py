"""
- El programa tendrá la función de crear el fichero con el nombre “notas.txt”
crearlo si no existe y el cual será dividido en dos archivos, uno principal

donde se llamará a las funciones que realizarán distintas operaciones en el
otro archivo la cual será llamada funciones.py.

- Crear una función donde se pedirá el tamaño de lista y la cantidad de
números que serán ingresado por consola (los números serán llenados de
manera aleatoria dentro de la lista), esta lista será escrita dentro del file
“notas.txt”
- Crear una función donde se usará la librería math para obtener la raíz
cuadrada de los números que han sido llenados en la lista anterior y los
cuales serán escritos en el file “notas.txt”.

"""


from ast import If


def crear_fichero():
    txt_file = open('/Users/arturodxx/curso_python/examen_final/my_files/notas.txt', 'a+')
    txt_file = open('/Users/arturodxx/curso_python/examen_final/my_files/notas.txt', "r+")


def crear_lista():
    lista = []
    while True:

        numeros = input('Igrese un numero: ')
        lista.append(numeros)

        opcion = input('Desea continuar (SI/NO)')
        if opcion.upper() == 'SI':
            pass
