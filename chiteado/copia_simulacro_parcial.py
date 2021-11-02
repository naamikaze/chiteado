

from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    codigo: str

def main_escribir():
    with open('archivo1.txt', 'w', encoding='utf-8') as arch1: 

        for i in range(100):
            arch1.write(f'{i} - Cliente {i}\n')

        

                

               
        
        

        ...
        print('Archivo generado')
    ...

def main_leer():
    lista_clientes=[]
    with open('archivo1.txt', 'r', encoding='utf-8') as arch1:
        
        
        for linea in arch1:
            
            cli = Cliente(linea[4:-1],linea[0:4])
            lista_clientes.append(cli)
    print(lista_clientes)

if __name__ == '__main__':
    main_escribir()
    
    ...
