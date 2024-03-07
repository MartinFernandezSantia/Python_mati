def suma(a, b):
    return(a+b)

print (suma(15,20))

listaN = ['Matias','Martin','Jose','Alberto']
def imprimir_nombres (listaN):
    for i in range(len(listaN)):
        print(listaN[i])

imprimir_nombres(listaN)

# dic = {
#     'nombre_clave': valor
# }

# valor=5
# dic["nombre_clave"] = valor
nombre = 'matias'
dic = {}

def conte_caracteres(nombre):
    for i in range(len(nombre)):
        cont = 0
        for j in range(len(nombre)):
            if nombre[j] == nombre[i]:
                cont += 1
        dic[nombre[i]] = cont
    print(dic)


conte_caracteres(nombre)


