class Coches:
    def __init__(self, marca,color,modelo,velocidad,potencia,asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo     
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def acelerar(self):
        self._velocidad+=1

    def frenar(self):
        self._velocidad-=1

    def getmarca(self):
        return self._marca

    def setmarca(self, marca):
        self._marca = marca

    def getcolor(self):
        return self._color

    def setcolor(self, color):
        self._color = color        

    def getmodelo(self):
        return self._modelo

    def setmodelo(self, modelo):
        self._modelo = modelo

    def getvelocidad(self):
        return self._velocidad

    def setvelocidad(self, velocidad):
        self._velocidad = velocidad

    def getpotencia(self):
        return self._potencia

    def setpotencia(self, potencia):
        self._potencia = potencia

    def getasientos(self):
        return self._asientos

    def setasientos(self, asientos):
        self._asientos = asientos


class Camiones(Coches):
    def  __init__(self, marca,color,modelo,velocidad,potencia,asientos,eje,capacidadCarga):
        super().__init__(marca,color,modelo,velocidad,potencia,asientos)
        self._eje=eje
        self._capacidadCarga=capacidadCarga

    def cargar(self, tipo_Carga):
        print("El tipo de carga del camión es: ", tipo_Carga)

    def acelerar(self):
        self._velocidad+=1
        print("Acelerando como camion")

    def frenar(self):
        self._velocidad-=1
        print("Frenando como camion")

    def setEje(self, eje):
        self._eje = eje    

    def getEje(self):
        return self._eje

    def setCapacidadCarga(self, _capacidadCarga):
        self._capacidadCarga = _capacidadCarga    
    
    def getCapacidadCarga(self):
        return self._capacidadCarga


class Camionetas(Coches):
    def  __init__(self, marca,color,modelo,velocidad,potencia,asientos,traccion,cerrada):
        super().__init__(marca,color,modelo,velocidad,potencia,asientos)
        self.__traccion=traccion
        self.__cerrada=cerrada

    def transportar(self, num_pasajeros):
        print("El numero de pasajeros que puede transportar la camioneta es: ", num_pasajeros)

    def acelerar(self):
        self._velocidad+=1
        print("Acelerando camioneta")

    def frenar(self):
        self._velocidad-=1
        print("Frenando camioneta")

    def setTraccion(self, traccion):
        self.__traccion = traccion  

    def getTraccion(self):
        return self.__traccion

    def setCerrada(self, cerrada):
        self.__cerrada = cerrada

    def getCerrada(self):

        return self.__cerrada



        
