#LECTURA Y ESCRITURA DE TEXTOS 

from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    codigo: str

def main_escribir():
    with open('archivo1.txt', 'w', encoding='utf-8') as arch1: #El 'w' es el tipo de escritura, lo primero es el nombre y lo ultimo es el encoding, lo que dice as arch es el nombre de la variable o sease de como identificar al archivo en el programa.

        for i in range(100):
            arch1.write(f'{i} - Cliente {i}\n')

        #arch1.write(

                #'UADE - Programación 1\n'  #Con el \r\n hago un salto de línea, el profe puso solo con \n pero a mi de igual forma me funcionaba 

               # ) #Escribo en el archivo
        
        #arch1.write('Archivos de texto\n') 

        ...
        print('Archivo generado')
    ...

def main_leer():
    lista_clientes=[]
    with open('archivo1.txt', 'r', encoding='utf-8') as arch1:
        #texto = arch1.read()
        #print(texto)
        for linea in arch1:
            #linea.replace('\n', '')
            cli = Cliente(linea[4:-1],linea[0:4])
            lista_clientes.append(cli)
    print(lista_clientes)

if __name__ == '__main__':
    main_escribir()
    #main_leer()
    ...
