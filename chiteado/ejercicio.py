from dataclasses import dataclass

@dataclass
class Produccion:
    maquina: str
    hora: int
    producido: int
    defectuoso: int

@dataclass
class Calidad:
    maquina: str
    hora: int
    defectos: int



def leer_calidad():
    with open('calidad.csv', 'r', encoding='utf-8') as arch:
        lista=[]
        primera=True
        for linea in arch:
            if primera:
                primera=False
                continue
            else:
                campos = linea.split(';')
                camp = Calidad(
                    campos[0], 
                    int(campos[1]),
                    int(campos[2]),
                )
                lista.append(camp)
        return lista

def leer_produccion():
    with open('produccion.csv', 'r', encoding='utf-8') as arch:
        lista=[]
        primera=True
        for linea in arch:
            if primera:
                primera=False
                continue
            else:
                campos = linea.split(';')
                camp = Produccion(
                    campos[0], 
                    int(campos[1]),
                    int(campos[2]),
                    0
                )
                lista.append(camp)
        return lista


def insertar_produccion(lista):
    with open('produccion.csv','r',encoding='utf-8') as arch:
        for linea in lista:
            for l in arch:
                campos = l.split(';') 
                if campos[0] == linea.maquina and campos[1] == linea.hora:
                    linea.producido == campos[2]
                else:
                    print('error')
    return lista

def insertar_produccion(listap, listac):
    for linea in listap:
        for l in listac:
            if l.maquina == linea.maquina and l.hora == linea.hora:
                linea.defectuoso = l.defectos
    return listap
 


def main():
    produccion = leer_produccion()
    calidad = leer_calidad()
    producir = insertar_produccion(produccion, calidad)
    print(producir)
    ...

if __name__ == '__main__':
    main()