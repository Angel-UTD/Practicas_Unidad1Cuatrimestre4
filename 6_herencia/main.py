from coches import Coches,Camiones,Camionetas

coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)

camion1 = Camiones("Dina", "Negro", "2020", 180, 300, 12, 8, 2500)
camion2 = Camiones("Star", "Azul", "2019", 150, 200, 14, 6, 2000)

camioneta1 = Camionetas("Renault", "Amarillo", "2025", 240, 250, 8, "delantera", True)
camioneta2 = Camionetas("Nissan", "Blanca", "2020", 180, 150, 6, "trasera", False)

camion1.acelerar()
camion1.frenar()
camion1.cargar("material de construcción")
print("Eje:", camion1.getEje())
print("Capacidad de carga:", camion1.getCapacidadCarga())

camion2.acelerar()
camion2.frenar()
camion2.cargar("alimentos")
print("Eje:", camion2.getEje())
print("Capacidad de carga:", camion2.getCapacidadCarga())

camioneta1.acelerar()
camioneta1.frenar()
camioneta1.transportar(5)
print("Tracción:", camioneta1.getTraccion())
print("¿Está cerrada?:", camioneta1.getCerrada())

camioneta2.acelerar()
camioneta2.frenar()
camioneta2.transportar(2)
print("Tracción:", camioneta2.getTraccion())
print("¿Está cerrada?:", camioneta2.getCerrada())

coche1.acelerar()
coche1.frenar()
print(f"El color es: {coche1.getcolor()}")
print(f"La marca es: {coche1.getmarca()}")

coche2.acelerar()
coche2.frenar()
print(f"El color es: {coche2.getcolor()}")
print(f"La marca es: {coche2.getmarca()}")