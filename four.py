# ROBOTS BEST PATH
# ? Puntos:
# 1 - Montañita, con vaso con agua
# 2 - NADA, con peso
# 3 - NADA, se puede llevar peso ahí
# 4 - Montañita grande P1, con peso
# 5 - Montañita grande P2, con vaso con agua y se puede llevar peso ahí

# * Subir y bajar montañitas significa doble de tiempo
# * Buscar el mejor circuito posible

# ! Subir montaña
# p.type == "montaña"
# ! Bajar montaña con un vaso sin que se caiga
# p.type == "montaña" AND p.objeto == "vaso"
# p.type == "montaña" AND currentObjeto == "vaso"
# ! Llevar un peso de un punto a otro
# p.objeto == "peso"
# p+n.espacio == "peso"

class Punto:
    def __init__(self, nombre, tipo, tiempo, objeto, espacio):
        self.nombre = nombre
        self.tipo = tipo
        self.tiempo = tiempo
        self.objeto = objeto
        self.espacio = espacio

p1 = Punto("P1-Montaña", "Montaña", 2, "vaso", "")
p2 = Punto("P2-Lugar Uno", "Lugar", 1, "peso", "")
p3 = Punto("P3-Lugar Dos", "Lugar", 1, "", "peso")
p4 = Punto("P4-Montaña Grande Uno", "Montaña", 2, "peso", "")
p5 = Punto("P5-Montaña Grande Dos", "Montaña", 2, "vaso", "peso")

puntos = {
    p1: [p2, p3, p4],
    p2: [p1, p3, p4],
    p3: [p1, p2, p4],
    p4: [p1, p2, p3, p5],
    p5: [p1, p2, p3, p4],
}

visitados = set()
subioMontaña = False

agarroVaso = False
bajoVaso = False

agarroPeso = False
dejoPeso = False

mejorCicuito = ""
mejorTiempo = 100000
tiempo = 0

def resetData():
    global tiempo, subioMontaña, agarroVaso, bajoVaso, agarroPeso, dejoPeso
    subioMontaña = False
    agarroVaso = False
    bajoVaso = False
    agarroPeso = False
    dejoPeso = False
    tiempo = 0

def búsqueda(visitados, puntos, punto):
    global tiempo, subioMontaña, agarroVaso, bajoVaso, agarroPeso, dejoPeso

    if punto not in visitados:
        print(punto.nombre + " - " + str(punto.tiempo))
        if(punto.tipo == "Montaña"):
            subioMontaña = True
            if(punto.objeto == "vaso" and not agarroVaso):
                agarroVaso = True
            if(agarroVaso):
                bajoVaso = True
        if(punto.objeto == "peso" and not agarroPeso):
            agarroPeso = True
        elif(punto.espacio == "peso" and agarroPeso):
            dejoPeso = True
        visitados.add(punto)
        tiempo = tiempo + punto.tiempo
        # print(str(subioMontaña)  + "  "  + str(bajoVaso) + " " + str(dejoPeso))
        for siguiente in puntos[punto]:
            búsqueda(visitados, puntos, siguiente)
            if(subioMontaña and bajoVaso and dejoPeso):
                return tiempo


for i,p in enumerate(list(puntos)[0:4]):
    print("\n\n---- Desde Punto " + str(i+1) + "----")
    duracion = búsqueda(visitados, puntos, p)
    
    print("\nDuró: " + str(duracion))
    if(duracion < mejorTiempo):
        mejorCicuito = str(i+1)
        mejorTiempo = duracion

    visitados.clear()
    resetData()

print("\n\nSecuencia de Punto " + mejorCicuito + ", con tiempo: " + str(mejorTiempo))