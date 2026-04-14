"""
class Cat():
    razza="felino"
    def __init__(self, name, age):
        self.name=name
        self.age=age
siamese=Cat("Luna", "4")
print(siamese.name)
siamese.name="Milù"
print(siamese.name)
print(siamese.age)
print(siamese.razza)


import random
class coin():
    def __init__(self):
        self.faccia=None
    def lancio(self):
        risultato=random.randint(0,1)
        if(risultato==1):
            self.faccia="testa"
        else:
            self.faccia="croce"
    def risultato(self):
        return self.faccia
moneta=coin()
moneta.lancio()
print(moneta.risultato())


class Veicolo():
    def __init__(self, modello, marca, anno):
        self.modello=modello
        self.marca=marca
        self.anno=anno
        self.speed=0
    def __str__(self):
        return f"{self.marca}  {self.modello}  {self.anno}  {self.speed} km/h"
    def accellerare(self):
        self.speed+=5
    def frenare(self):
        self.speed-=5
    def get_speed(self):
        return self.speed
auto=Veicolo("Panda", "Fiat", "2009")
auto.accellerare()
auto.accellerare()
auto.frenare()
print(auto)
print(auto.get_speed())
"""