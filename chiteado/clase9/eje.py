#FIJARME COMO HACER EL EJERCICIO1
import random
from dataclasses import dataclass

@dataclass
class Alumno:
    apellido: str
    nombre: str
    edad: int 
    carrera: int
    mat_aprobadas: int

@dataclass
class Producto:
    nombre: str
    categoria: int
    stock: int
    precio: float 

class ValorNoEncontrado(Exception):
    pass

class ErrorCadenaVacia(Exception):
    pass

# Ejercicio 2 Tema 2
def main_ejercicio2_tema2():
    try:
        # cantidad_vocales= contar_vocales("")
        cantidad_vocales= contar_vocales("dfgtesdao")
        print(f"Cantidad de vocales: {cantidad_vocales}")
    except ErrorCadenaVacia:
        print("La cadena esta vacia")

def es_vocal(letra):

#Este es la forma más facil que funciona
    """
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return True
    else:
        return False
    """
#Esta es otra opción
    """
    for vocal in vocales:
        if letra == vocal:
            return True
    return False
    """
    """
    if letra in vocales:
        return True
    return False
   """

    vocales = "aeiouAEIOUáéíóú"
    # print(letra in vocales)
    return letra in vocales

def contar_vocales(texto):

    if len(texto) == 0: #Si el texto no tiene nada escrito levanta la excepcion de que no hay nada
        raise ErrorCadenaVacia

    cantidad= 0
    for i in range(len(texto)):
        if es_vocal(texto[i]):
            cantidad += 1
    return cantidad

def buscar_matriz(vector, buscar):

    for fila in range(len(vector)):
        for columna in range(len(vector[fila])):

            if buscar == vector[fila][columna]: #Con esto pregunto si lo que busco es igual a lo que esta en esa posicion de fila y columna.  

                #matris[fila][columna] = 0 <-- meteria un valor 

                return [fila, columna]

    raise ValorNoEncontrado #Si ya hubiese encontrado un valor corta en el return pero como no encontró nada avanza hasta llegar al raise

def main3():
    lista_alumnos = generar_alumnos()
    mayor_cant_materias(lista_alumnos)
    #mayor_cant_materias(lista_alumnos)
    ...

def generar_alumnos():
    lista=[]
    #Voy llenando la lista de alumnos
    for i in range(10):

        lista.append(Alumno(
            #El str+1 lo que hace es convertir el i del for en texto y lo concatena con la lista, asi es mas facil meter todo en la lista
            #Lo pongo en un formato mas comodo.
            'Apellido' + str(i),
            'Nombre' + str(i),
            20 + i, #Este seria la edad
            random.randint(1,3), #Carrera
            random.randint(0,30), #Materias aprobadas
            ))

    return lista

def mayor_cant_materias(lista_alumnos):
    carrera= ingrese_numero("Ingrese carrera (1, 2 o 3)", 1, 3)
    alumno_mayor = None
    mayor = -1

    for alumno in lista_alumnos: #Recorro todos los dataclass alumno de lista de alumnos
        if alumno.carrera == carrera: #Si la carrera del alumno coincide con la que elegimos empieza a comparar.
            if alumno.mat_aprobadas > mayor: #Si el alumno que en su dataclass mat_aprobadas es mayor que la variable mayor.
                mayor = alumno.mat_aprobadas #El valor de mayor pasa a ser el del mat_aprobadas de el alumno correspondiente.
                alumno_mayor = alumno #Definimos que el alumno mayor va a ser el que actualmente esta en el for.

    if mayor == -1:
        print('No hay alumnos en la carrera solicitada.')
    else:
        print(f'Nombre: {alumno_mayor.nombre}')
        print(f'Apellido: {alumno_mayor.apellido}')
        print(f'Edad: {alumno_mayor.edad}')

def ingrese_numero(msg, min, max):
    while True:
        try:
            nro = int(input(msg))
            if nro < min or nro > max:
                print('Nro fuera de rango')
            else:
                return nro
        except ValueError:
            print('Ingrese un numero')
        ...
def main_productos():
    lista=generar_alumnos()
    imprimir_lista(lista)

def imprimir_lista(lista):
    for alumno in lista:
        if alumno.carrera == 1 and alumno.edad > 30: #ALumnos carrera contador mayores de 30 ACA NO ME GENERA NADA PORQUE LLEGA HASTA 29 PORQUE LA EDAD TIENE UN + i 
            print(f'{alumno.nombre} | {alumno.apellido} | {alumno.edad}')

def sacar_promedio(lista):
    promedio = 0
    cont = 0
    for alumno in lista:
        if alumno.carrera == 3:
            promedio += alumno.edad
            cont +=1
    return promedio / cont


def main32():
    lista = generar_alumnos()
    try:
        promedio = sacar_promedio(lista)
        print(f'Promedio de los chavales: {promedio}')
    except ZeroDivisionError:
        print('No hay alumnos en la carrera solicitada.')
        ...

def main():
    #main_productos()
    #main_ejercicio2_tema2()
    #matriz1()
    #main3()
    main32()

def matriz1():
    valor_buscar = 3
    matrizo = [[1,2,3],[4,5,6],[7,8,9]]
    try:
        posicion = buscar_matriz(matrizo, valor_buscar)
        print(f'La posición del valor solicitado es: {posicion[0]} , {posicion[1]}') #Como hago return en forma de vector lo pongo de esta forma [0][1] como en la linea 10
    except ValorNoEncontrado:
        print('No se encontró el valor solicitado.')
    ...

if __name__ == '__main__':
    main()
