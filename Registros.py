class Publicidad():
    def __init__(self, identificador, nombre, tematica, horario, monto):
        self.identificador = identificador
        self.nombre = nombre
        self.tematica = tematica
        self.horario = horario
        self.monto = monto

    def __str__(self):
        cad = ("Identificador: {}. Publicidad: {} Tematica: {}. Horario: {}. Monto: {}.")
        return cad.format(self.identificador, self.nombre, self.tematica, self.horario, self.monto)

#FUNCIONES AUXILIARES
def validar_mayor(inf, men):
    n = int(input(men))
    while n <= inf:
        n = int(input("Ingrese un numero mayor a " + str(inf) + ": "))
    return n

def add_in_orden_identificador(v, reg):
    n = len(v)
    izq, der = 0, n - 1
    pos = n
    while izq <= der:
        c = (izq + der) // 2
        if v[c].identificador == reg.identificador:
            pos = c
            break
        if v[c].identificador < reg.identificador:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    v[pos:pos] = [reg]
