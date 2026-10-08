#Programa principal desde la que se manda llamar los objetos de la clase de coches
from coche import Coches

coche1=Coches("VW","blanco","2022",220,150,5)
coche2=Coches("nissan","azul","2020",180,150,6)    

print(coche1.getvelocidad())
for i in range(1,101):
    coche1.acelerar()

print(coche1.getvelocidad())

coche1.setvelocidad(400)
print(coche1.getvelocidad())