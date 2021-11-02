from dataclasses import dataclass

@dataclass
class Alumno:
    apellido: str
    dni: str
    nombre: str
    provincia: str
    idProvincia: str
    localidad: str
    sede: str
    direccion: str
    llamada: str


def main():
    lista_alumnos=[]
    with open('./clase10/personas-certificadas.csv', 'r', encoding='utf-8') as arch:
        primera_vez= True
        for linea in arch:

            if primera_vez:
                primera_vez = False
                continue


            campos = linea[:-1].split(',') #Hago que cada coma sea un mini vector


            alumno = Alumno(

            campos[1],
            campos[0],
            campos[2],
            campos[3],
            campos[4],
            campos[5],
            campos[6],
            campos[7],
            campos[8],
            
            ) #Hago que cada campo que genera el split 0=Dni, etc se coloque en el dataclass de alumnos y vaya generando los mismos

            lista_alumnos.append(alumno) #Meto a los alumnos generados con el dataclass en una lista

    lista_cordoba=[]
    lista_tucuman=[]
    for alumn in lista_alumnos:
        if alumn.idProvincia == '14':
            lista_cordoba.append(alumn)
        if alumn.idProvincia == '90':
            lista_tucuman.append(alumn)

    with open('al_cordoba.csv', 'w', encoding='utf-8') as arch:
        for alumnxs in lista_cordoba:
            arch.write(f'{alumnxs.dni},{alumnxs.apellido},{alumnxs.nombre}\n')
            #arch.write(f'{alumnxs}\n')


if __name__ == '__main__':
    main()
    ...