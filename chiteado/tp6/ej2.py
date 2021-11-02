import random
from dataclasses import dataclass

@dataclass
class dialluvia:
    dia: int
    mes: int
    lluvia_caida: int

def lluvia():
    lista_dias=[]
    lluvia_total = 0
    for x in range(12+1):

        if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
            for i in range(31):
                lluviagenerada=random.randint(50, 200)
                dias = dialluvia([i+1], [x], [lluviagenerada])
                lista_dias.append(dias)
                lluvia_total+=lluviagenerada

        elif x == 2:
            for i in range(28):
                lluviagenerada=random.randint(50, 200)
                dias = dialluvia([i+1], [x], [lluviagenerada])
                lista_dias.append(dias)
                lluvia_total+=lluviagenerada

        elif x == 4 or x == 6 or x == 9 or x == 11:
            for i in range(30):
                lluviagenerada=random.randint(50, 200)
                dias = dialluvia([i+1], [x], [lluviagenerada])
                lista_dias.append(dias)
                lluvia_total+=lluviagenerada

    print(f'Lluvia generada anualmente: {lluvia_total}')
    return lista_dias



def escribir_dias(lista):
    with open('archivo.csv', 'w', encoding='utf-8') as arch:
        for dias in lista:
            arch.write(f'{dias.dia} , {dias.mes} , {dias.lluvia_caida}\n')
    print(f'Todo listo')


def leer_dias():
    with open('archivo.csv', 'r', encoding='utf-8') as arch:
        lista=[]
        for dias in arch:
            campos = dias.split(',')
            diass = dialluvia(
                    campos[0], 
                    campos[1], 
                    campos[2], 
                    )
            lista.append(diass)

    total_generado = 0
    for dias in lista:
        print(f'Dia: {dias.dia} Mes: {dias.mes} Generado: {dias.lluvia_caida}')



def main():
    lista = lluvia()
    escribir_dia = escribir_dias(lista)
    mostrar = leer_dias()
    print('')
    ...

if __name__ == '__main__':
    main()
