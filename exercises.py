#Ejercicio 3
# 3. En pocos días comienza la vuelta a España y la federación
# colombiana de ciclismo, como incentivo ha determinado pagar
# un valor adicional. El programa pedirá por teclado el sueldo
# básico por kilometro recorrido, el número de kilómetros
# recorridos durante toda la vuelta, numero de kilómetros
# recorridos con la camiseta de líder.
# Calcular el valor a pagar total, si se sabe que si recorre en la
# bici más de 1800 kilómetros con la camiseta de líder, esos
# kilómetros se consideran especiales y tendrán un recargo de
# 25%.
# El total de kilómetros por recorrer durante toda la vuelta serán
# 3.277 kilómetros,el ganador de la vuelta a España recibirá 700
# millones de pesos.

NFinalistas = int(input("ingrese el numero de finalistas: "))
mensajes = ["finalista: ",  "Sueldo k: ", "#kilometros R en toda La V: ", "#kilometros R como Lider: "]
w = len(mensajes)
opcion=[]
limite = 3177
porcientoDemas = 1800
finalistas={}
m = 0

while m < NFinalistas:
    for q in range(0, w):
        name, sueldo, kilom, kilomLider=input(mensajes[q]),input(mensajes[q+1]),input(mensajes[q+2]),input(mensajes[q+3])
        finalistas[name] = [int(sueldo), int(kilom), int(kilomLider)]
        break
    m+=1

for finalista in finalistas:
    for (indexPago, Valorpago) in enumerate((finalistas[finalista])):
        kilomCon = finalistas[finalista][indexPago + 1] 
        kilomLiderCon = finalistas[finalista][indexPago + 2] 
        if kilomCon > limite:
             print(f"El finalista {finalista} se paso del limite con {kilomCon - limite} km demas...")    
        else: 
             if kilomLiderCon >= porcientoDemas:
                operation = ((kilomCon * .25) + kilomCon) 
                print(f"{finalista} paso los 1800 siendo lider entonces gano un porcentaje del 25% a {kilomCon}, por {operation}")
                break
             else:
                operation = (kilomCon * (kilomCon - kilomLiderCon))
                print(f"El total a pagar a {finalista} fue de: {operation}")
        break
               