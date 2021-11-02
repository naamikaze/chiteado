def main_leer():
    lista=[]
    with open('archivo.py', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            lista.append(linea)
    return lista


def main_borrar(lista):
    lista1 = []
    for linea in lista:
        reemplazar = linea.replace('#', '')
        lista1.append(reemplazar)
    print(lista1)
    return lista1 

def main_ingresar(lista):
    with open('archivo.py', 'w', encoding='utf-8') as archivo:
        for x in range(len(lista)):
            archivo.write(lista[x])
    print('Todo listo')


def main():
    lista = main_leer()
    borrada = main_borrar(lista)
    main_ingresar(borrada)
    ...


if __name__ == '__main__':
    main()
    ...
        
