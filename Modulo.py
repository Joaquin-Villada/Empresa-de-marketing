from Registros import *
import pickle
import random
import os

def menu():
    print("\n" + "*" * 4 +  "Menu de opciones" + "*" * 4)
    print("1) Cargar publicidades.")
    print("2) Mostrar datos cargados.")
    print("3) Buscar en la base de datos publicidad por id.")
    print("4) Mostrar monto total segun tematica y franja horaria")
    print("5) Mayor monto en el registro")
    print("6) Segun el mayor monto del registro deducir cuantas palabras no empiezan con vocales")
    print("7) Salir....")

def cargar_vector(v, n):
    for i in range(n):
        marcas = ("Nike", "Adidas", "Taverniti", "Puma", "Rebook", "Calvin Klein")
        producto = ("Zapatillas", "Casco", "Pantalones", "Remeras", "Buzos", "Chaquetas", "Guantes", "Acesorios")
        identificador = random.randint(11111, 99999)
        nombre = random.choice(marcas) + " " + random.choice(producto) + "."
        tematica = random.randint(1, 5)
        horario = random.randint(1, 96)
        monto = round(random.uniform(0, 10000), 2)
        registro = Publicidad(identificador, nombre, tematica, horario, monto)
        add_in_orden_identificador(v, registro)
    print("Las publicidades se cargaron ordenados por numero de id de menor a mayor, eliga la opcion 2 para visualizarlos.")

def mostrar_vector(v):
    for i in v:
        print("\t", i ,"\n")

def buscar_id(v, id):
    band = True
    for i in v:
        if i.identificador == id:
            print("Se encontro la siguiente publicidad: ", i)
            band = False
            return i.nombre
            break
    if band:
        print("Publicidad inexistente.")
        return "Publicidad inexistente."

def crear_matriz(vec):
    matriz = [[0] * 5 for i in range(96)]
    for i in vec:
        columna = i.tematica - 1
        fila = i.horario - 1
        if i.monto != 0:
            matriz[fila][columna] += i.monto
    return matriz

def mostrar_matriz(matriz):
    for c in range(5):
        for f in range(96):
            if matriz[f][c] != 0:
                print("En la tematica " + str(c+1) + " y franja horaria " + str(f+1) + " hay un monto total de: " + str(round(matriz[f][c], 2)))

def mayor_facturacion(matriz):
    band = True
    for c in range(5):
        for f in range(96):
            if band:
                mayor = matriz[f][c]
                fila = f + 1
                columna = c + 1
                band = False
            elif matriz[f][c] > mayor:
                mayor = round(matriz[f][c], 2)
                fila = f + 1
                columna = c + 1
    print("El mayor monto encontrado fue de " + str(mayor) + " perteneciente a la tematica " + str(columna) + " y a la franja horaria " + str(fila))

def no_vocal(cad):
    band = True
    cont = 0
    for i in cad:
        if band == True and i not in "aeiouAEIOU":
            cont += 1
            band = False
        if i == " ":
            band = True
        else:
            band = False
    print("La cantidad de palabras que no empezaban con vocales es de " + str(cont))


def principal():
    v = []
    op = -1
    op4, op3 = True, True
    while op != 7:
        menu()
        op = int(input("Ingrese la opcion deseada: "))
        if op == 1:
            n = validar_mayor(0, "Ingrese la cantidad de publicidades que desea cargar: ")
            cargar_vector(v, n)
        elif v == []:
            print("Primero cargue el vector en la opcion 1")
            op = -1
        elif op == 2:
            print("Las publicidades cargados son: \n")
            mostrar_vector(v)
        elif op == 3:
            op3 = False
            id = validar_mayor(11110, "Ingrese el id que desea buscar: ")
            nombre = buscar_id(v, id)
        elif op == 4:
            montos = crear_matriz(v)
            mostrar_matriz(montos)
            op4 = False
        elif op == 5:
            if op4:
                print("\nPrimero cargue los montos en el punto 4.\n")
            else:
                mayor_facturacion(montos)
        elif op == 6:
            if op3:
                print("Primero busque la id en el punto 3")
            else:
                print(nombre)
                no_vocal(nombre)
        elif op == 7:
            print("Gracias por usar el programa")
        else:
            print("Ingrese una opcion correcta")

if __name__ == '__main__':
    principal()
