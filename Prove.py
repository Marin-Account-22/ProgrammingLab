"""
import random
class Persona():
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
    def __str__(self):
        return "Soggetto: {} {}".format(self.name, self.surname)
    def salutare(self):
        random_number=random.randint(0,2)
        if random_number==0:
            print("Ciao, io sono {} {}".format(self.name, self.surname))
        elif random_number==1:
            print("Ciao, mi chiamo {}".format(self.name))
        elif random_number==2:
            print("Ehi ciao, sono {}".format(self.name))
class Studente(Persona):
    def __str__(self):
        return "Studente: {} {}".format(self.name, self.surname)
class Professore(Persona):
    def __str__(self):
        return "Professore: {} {}".format(self.name, self.surname)
    def salutare(self):
        random_number=random.randint(0,1)
        if random_number==0:
            print("Buongiorno, io sono il professor {}".format(self.surname))
        else:
            print("Salve, sono il professor {} {}".format(self.name, self.surname))
Marin=Persona("Andrea", "Marin")
#Marin.salutare()
Del_Santo=Professore("Giuseppe", "Del Santo")
#Del_Santo.salutare()
Samu=Studente("Samuele", "Bon")
#Samu.salutare()
print(Marin.__str__())
print(Del_Santo.__str__())
print(Samu.__str__())


class Banca:
    def __init__(self, saldo):
        self.__saldo = saldo
    def deposita(self, x):
        self.__saldo += x
    def saldo(self):
        return self.__saldo
Unicredit=Banca(100)
print(Unicredit._Banca__saldo)
print(Unicredit.saldo())


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    def __call__(self, other):
        return self.x*other + self.y
v1=Vector(2,3)
v2=Vector(3,4)
v3=v1.__add__(v2)
v4=v3.__mul__(2)
# print(v4.x, v4.y)
v5=v1.__call__(2)
print(v5)


my_var="ciao"
try:
    my_var=float(my_var)
except ValueError:
    print("errore di valore, valeva '{}'".format(my_var))
else:
    print("non c'è nessun errore")
finally:
    print("daje Roma")


numero=2
if numero<5:
    differenza=5-numero
    raise ValueError("Il numero è troppo piccolo, devi incrementarlo almeno di {}".format(differenza))
"""

for i in [0,1,2,3]:
    if i==0:
        continue
    else: print(i)