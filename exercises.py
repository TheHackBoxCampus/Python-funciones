#Ejercicio 2
# 2. N atletas han pasado a finales en salto triple en los juegos
# olímpicos de 2022.

# Diseñe un programa que pida por teclado los nombres de cada
# atleta finalista y a su vez, sus marcas del salto en metros.

# Informar el nombre de la atleta campeona que se quede
# con la medalla de oro y si rompió récord, reportar el pago que
# será de 500 millones. El récord esta en 15,50 metros.

import operator
finalista = {}
pos = []

class agregarPersonas:
    def __init__(self, nombre_metros) -> str:
        self.infoParticipante = nombre_metros

    def obtenerInformacion(self):
        nFinalistas = int(input("Numero de finalistas: "))
        opciones = ["finalista: ", "metros: "]
        n = len(opciones)
        y = 0
       
        while y < nFinalistas:
            for i in range(n):
                nombre, metros = input(opciones[i]),input(opciones[(i+1)])
                self.infoParticipante[nombre] = int(metros)
                break
            y+=1

    def mostrarInformacion(self, aux):
        for e in self.infoParticipante:
            aux.append(self.infoParticipante[e])
            maxValue = max(aux)
            finallyPost = max(self.infoParticipante.items(), key=operator.itemgetter(1))[0]

        if int(maxValue) >= 15.50: 
            print(f"el jugador/a {finallyPost} rompio el record de 15.50, con un salto de {maxValue} metros")
        else: 
            print(f"el jugador/a que tuvo el mayor salto fue {finallyPost} con un salto de {maxValue} metros")

exePrograma = agregarPersonas(finalista)
exePrograma.obtenerInformacion()
exePrograma.mostrarInformacion(pos)