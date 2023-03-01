#Ejercicio 4
# 4. Una empresa tiene 500 almacenes. Cada almacén debe
# reportar el nombre y 5 registros c/u, contiene el tipo de articulo
# y el número de unidades vendidas de ese artículo.

# Haga un programa en Python para determinar cuál fue el
# almacén que mas vendió, cual fue el articulo más vendido de
# ese almacén y cual el más vendido en general.

import operator
sum = 0
almacenes = {}
maximoVendidoGeneral = {}
maximoEsponencial = {}
NAlmancenes = int(input("Ingrese el numero de almacenes que quiere analizar: "))
opciones = ["Nombre del Almacen: ", "Producto: ", "Numero de ventas: "]
y = 0

while y < NAlmancenes:
    nombre = input(opciones[0])
    almacenes[nombre] = {}
    for q in range(2):
        producto, NVentas = input(opciones[1]),int(input(opciones[2]))
        maximoVendidoGeneral[producto] = NVentas
        if len(almacenes[nombre]) < 1: almacenes[nombre] = {producto:NVentas}
        else: almacenes[nombre][producto] = NVentas
    y+=1        

for almacen in almacenes:
    productMax = max(almacenes[almacen].items(), key=operator.itemgetter(1))[0]
    valueMax = max(almacenes[almacen].items(), key=operator.itemgetter(1))[1]
    print(
    f"""
    --------------------------------------------------------------------------------------------------------------------------------
    El producto que mas se vendio fueron los/as {productMax} con una cantidad de {valueMax} unidades en el almacen '''({almacen})'''
    --------------------------------------------------------------------------------------------------------------------------------
    """)
    for (index,t) in enumerate(almacenes[almacen]):
       sum += almacenes[almacen][t]
       maximoEsponencial[almacen] = sum
       if index == len(almacenes[almacen]) - 1: sum = 0
    

maxGeneralProducto = max(maximoVendidoGeneral.items(), key=operator.itemgetter(1))[0]
maxGeneralProductoVentas = max(maximoVendidoGeneral.items(), key=operator.itemgetter(1))[1]
maxGeneralArticulos = max(maximoEsponencial.items(), key=operator.itemgetter(1))[0]

print(
f"""
----------------------------------------------------------------------------------------------------------------------
El producto que mas se vendio en general fue: {maxGeneralProducto} con un total de {maxGeneralProductoVentas} unidades 
----------------------------------------------------------------------------------------------------------------------
""")

print(
    f"""
    ---------------------------------------------------
    El almacen que mas vendio fue: {maxGeneralArticulos}
    ---------------------------------------------------
    """)