
#NO ANDA PORQUE LA CLASE SE TRABA

def buscar_posicion_caracter(caracter, linea):
    for i in range(len(linea)):
        if linea[i] == caracter:
            return i
    return -1

def leer_lineas_archivo(nombre_archivo):
    lineas=[]
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            lineas.append(linea[:-1])
        print(lineas)
        return lineas
        ...

def borrar_coment(lineas_archivo):
    lista = []
    for linea in lineas_archivo:
        i = buscar_posicion_caracter('#', linea)
        if i == -1:
            lista.append(linea)
        else:
            lista.append(linea[0:i])
        #reemplazar = linea.replace('#', '')
    return lista 
    ...

def escribir_archivo(nombre, texto):
    with open(nombre, 'w', encoding='utf-8') as archivo:
        for linea in  texto:
            archivo.write(linea + '\n')
    

def main():
    nombre_archivo='archivao.py'
    lineas_archivo= leer_lineas_archivo(nombre_archivo)
    lineas_sin_comentario = borrar_coment(lineas_archivo)
    escribir_archivo("copia_" + nombre_archivo, lineas_sin_comentario)

if __name__ == '__main__':
    main()
