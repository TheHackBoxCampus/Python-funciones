artemis = []
sputnik = []

def artemis_sputnik(typeVar, ftcRes, group, nameGroup,arr):
      if typeVar == float(f"{group}.1"):
          upperTransform = nameGroup.upper()
          print(
          f"""
          LA LISTA DE {upperTransform} CUENTA CON LAS SIGUIENTES PERSONAS
          {arr}
          """)
          ftcRes()
      elif typeVar == float(f"{group}.2"):
          newCamper = input("Digite el nombre del nuevo Integrante de {}: ".format(nameGroup))          
          arr.append(newCamper)
          print("Se agrego correctamente.")
          ftcRes()
      elif typeVar == float(f"{group}.3"):
          name = input("Escribe el nombre del integrante que quieres eliminar: ")
          if name in arr:
             arr.remove(name)
             print("Se elimino correctamente")
             ftcRes()
          else: 
             print("Ese integrante no exite")
             ftcRes()
      elif typeVar == float(f"{group}.4"):
          arr.sort()
          print("Se ha ordenado de forma alfabetica!")
          ftcRes()
      elif typeVar == float(2.5) or typeVar == float(1.5):
          integrant = input("Escribe el camper que quieres buscar dentro de {}: ".format(nameGroup))
          if integrant in arr:
             for (index,value) in enumerate(arr):
                 if arr[index] == integrant:
                    print(f"El integrante: {integrant} se encuentra en la posicion: {index + 1}") 
                    ftcRes()
          else:
             print(f"No existe dentro de la lista {nameGroup}")
             ftcRes()


def operations_ftc(numberReal, restoreFtc):
    if type(numberReal) is str and len(numberReal) == 1: 
        typeint = int(numberReal)
        if typeint == 1:
          print("Artemis se ha creado Correctamente..") 
          return restoreFtc()
        elif typeint == 2:
          print("Sputnik se ha creado Correctamente..")        
          return restoreFtc()
        elif typeint == 3: return 
    else:
      typeFloat = float(numberReal)
      if typeFloat > 2:
          artemis_sputnik(typeFloat, restoreFtc, round(typeFloat), "sputnik", sputnik)
      else: 
          artemis_sputnik(typeFloat, restoreFtc, round(typeFloat), "artemis", artemis)
    

 