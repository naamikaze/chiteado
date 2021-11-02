from dataclasses import dataclass

@dataclass
class Calidad:
    maquina: str
    hora:str 
    defectos:str 

def leer_archivo():
    lista = []
    with open('calidad.csv', 'r', encoding='utf-8') as arch:
        primeravez = True
        for linea in arch:
            if primeravez:
                primeravez=False
                continue
            else:
                campos = linea.split(';')
                maquinas = Calidad(0,0,0)
                maquinas.maquina = campos[0]
                maquinas.hora = int(campos[1])
                maquinas.defectos = int(campos[2])
                lista.append(maquinas)
    return lista





def main():
    leer = leer_archivo()
    print(leer)
    ...

if __name__ == '__main__':
    main()
