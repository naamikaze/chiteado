from dataclasses import dataclass

@dataclass
class Maquinas:
    maquina: str 
    hora: int
    defectos: int

@dataclass
class Produccion:
    maquina:str
    hora:int
    unidades:int


def leer_calidad():
    with open('calidad.csv', 'r', encoding='utf-8') as arch:
        lista=[]
        primeravez = True
        for maquinas in arch:

            if primeravez:
                primeravez = False
                continue

            campos = maquinas[:-1].split(';') 
            maq = Maquinas(campos[0], campos[1], campos[2]) 
            lista.append(maq)
    return lista


def leer_produccion():
    with open('produccion.csv', 'r', encoding='utf-8') as arch:
        lista=[]
        primeravez = True
        for maquinas in arch:

            if primeravez:
                primeravez = False
                continue

            campos = maquinas[:-1].split(';') 
            maq = Produccion(campos[0], campos[1], campos[2]) 
            lista.append(maq)
    return lista



def defectuosas(listacalidad, listaproduccion, maquina_e, horario):
    cantdefectos=0
    for maquina in listacalidad:
        print(f'{maquina.maquina},{maquina.hora},{maquina.defectos}')
        if maquina.maquina == maquina_e and maquina.hora == horario:
            cantdefectos+= maquina.defectos

    print(f'Cantidad de defectuosas en la maquina {maquina_e} y hora {horario} es de: {cantdefectos}') 

    ...

def main():
    calidad = leer_calidad()
    produccion = leer_produccion()
    defect = defectuosas(calidad, produccion, 'E', 11)
    ...

if __name__ == '__main__':
    main()
    ...
