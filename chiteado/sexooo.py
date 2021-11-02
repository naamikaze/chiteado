from dataclasses import dataclass

@dataclass
class Turnos:
    turnos: int 
    maquina:int 
    prod:int 
    deff:int 

def leer_archivo():
    with open('turnos.csv', 'r', encoding='utf-8') as arch:
        lista = []
        primeravez = True
        for linea in arch:
            if primeravez:
                primeravez=False
                continue
            else:
                campos = linea.split(';')
                turnacos=Turnos(

                int(campos[0]),
                int(campos[1]),
                int(campos[2]),
                int(campos[3]),

                )

                lista.append(turnacos)

    return lista

def crear_matriz():
    datos = [['A', 450, 1500],['B', 350, 1425],['C', 400, 1450],['D', 250, 1000] ,['E', 200, 900]]
    return datos
    sexo(leer)

def calcular(leer):
    for linea in leer:
        total_diario=0
        total_diario = linea.prod - linea.deff
        valuacion = total_diario * 77
        print(f'Maquina {linea.maquina} Total: {total_diario} Valuacion: {valuacion}\n')

def crear_archivo(lista):
    primera=True
    with open('archivosexo.csv', 'w', encoding='utf-8') as arch:
        for linea in lista:
            if primera:
                arch.write(f'turno;maquina;prod;def\n')
                primera=False
            else:
                arch.write(f'{linea.turnos};{linea.maquina};{linea.prod};{linea.deff}\n')


def main():
    leer = leer_archivo()
    matriz= crear_matriz()
    reporte = calcular(leer)
    crear = crear_archivo(leer)
    ...

if __name__ == '__main__':
    main()