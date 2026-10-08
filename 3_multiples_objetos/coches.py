class Coches:
    marca = ""
    color = "no tiene color"
    modelo = ""     
    velocidad = 0
    potencia = 0
    asientos = 0

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1


coche1= Coches ()
coche2= Coches ()

print(f"el coche 1 es de color {coche1.color} ")

coche1.color="Rojo y blanco"
print(f"el coche 1 es de color {coche1.color} ")

coche2.color="Blanco y negro"
print(f"el coche 2 es de color {coche2.color} ")



for i in range(10,110,10):
    coche1.acelerar()
    coche2.acelerar()

print(f"la velocidad del coche 1 es de {coche1.velocidad} km/h")
print(f"la velocidad del coche 2 es de {coche2.velocidad} km/h")

