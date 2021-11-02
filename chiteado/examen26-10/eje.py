from dataclasses import dataclass
from typing import List

@dataclass
class Clientes:
    nro_afiliado: int 
    cod_prestacion: int
    reintegro: int

def leer_archivo():
    lista = []
    with open('obrasocial.csv', 'r', encoding='utf-8') as arch:
        for linea in arch:
            campos = linea.split(';')
            client =  Clientes(
                int(campos[0]),
                int(campos[1]), 
                0
                
            )
            lista.append(client)

    return lista

def calcular_importes(clientes: List[Clientes]):
    #Meto todo en una función para que recorra todo mas facil
    for clien in clientes:
       calc_importes(clientes) 
    ...

def calc_importes(clientes: Clientes):
    #Calculo el importe de prestacion
    importe_prestacion =  calcular_importe_prestacion(clientes.cod_prestacion)
    #Calculo el importe de afiliados
    afiliadd = calcular_por_afiliado(clientes.cod_prestacion, clientes.nro_afiliado)
    #Calculo el importe total de las dos (cuanto  porcentaje tengo q usar, etc)
    importe = importe_prestacion * (1 - afiliadd/100)
    return importe


def calcular_por_afiliado(prestacion, afiliado):
    if afiliado <= 30000:
        return 0
    elif  afiliado > 60000:
        return 80
    #Si no es ninguno de esos dos rangos entonces está en el rango de 30001 - 60000
    else:
        if prestacion == 100 or prestacion == 200:
            return 0
        else:
            return 40

def calcular_importe_prestacion(prest):
    #Dependiendo q prestacion tiene devuelve el precio
    if prest == 100:
        return 1000
    elif prest == 200:
        return 2000
    elif prest == 300:
        return 3000
    elif  prest == 400:
        return 4000


def crear_liquidacion(lista):
    with open('liqui.txt', 'w', encoding='utf-8') as arch:
        arch.write(f'{"Nro. Afiliado":^20}|{"Cod.Prestacion":^20}|{"Importe":>15}\n')
        for linea in arch:
            arch.write(f'{lista.nro_afiliado:^20d}|{lista.cod_prestacion:^20d}|{lista.reintegro:^15f}\n')

def main():
    #Leo el archivoj
    leer = leer_archivo()
    #Calculo importes
    calcular_importes(leer)
    #Creo el archivo de liquidación
    archivo = crear_liquidacion(leer)
    ...

if __name__ == '__main__':
    main()
    ...

