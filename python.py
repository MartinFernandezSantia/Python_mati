# if 1==2:
#     print(1)
# elif True==1:
#     print(2)
# else:
#     print("hola")

diccionarios = {
    'Matias': 'puto',
    'Juan': 2,
    2: 3
}

listas = [1,2,3,4, "hola", diccionarios, {'Hola': 'chau'}]
# print(listas[5]['Matias'])

# print(diccionarios[2])}

for i in range(len(listas)):
    print(listas[i])

contador = 0
while contador < len(listas):
    print(listas[contador])
    contador += 1

# int sumar(int a, int b){

# }
    
def sumar(a, b, c = 100):
    return (a + b) * c

sumar(1, 2, 3)


class Usuario:
    def __init__(self, nombre, edad, mail):
        self.nombre = nombre
        self.edad = edad

        self.saludar()
        return
    
    def saludar(self):
        print(f'Hola soy {self.nombre} y tengo {self.edad}')

user = Usuario('Martin', 20, 'asd@asd.com')

user2 = Usuario('Matias', 20, 'aioijw@oiajd.com')



