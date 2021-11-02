import random
from dataclasses import dataclass

@dataclass
class deportistas:
    nombre: str
    deporte: int 
    altura: int

def generar_lista():
    lista = []
    contador =0
    for x in range(3):
        for i in range(3):
            contador +=1
            altura = random.randint(160, 190)
            deportista = deportistas([f"deportista{contador}"], [x+1], [altura])
            lista.append(deportista)
    return lista

def archivo_generar(lista):
    print(lista)
    with open('deportistas.csv', 'w', encoding='utf-8') as arch:
        contador = 0
        for deport in lista:
            arch.write(f'{deport.altura}\n')
def main():
    lista_deportistas = generar_lista()
    escribir_archivo = archivo_generar(lista_deportistas)
    promedio = sacar_promedio()
    ...

if __name__ == '__main__':
    main()