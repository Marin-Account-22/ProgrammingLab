"""
def calcola_ora(minuti):
    return minuti//60
def calcola_minuti(minuti):
    return minuti%60
minuti=69
print(f"{calcola_ora(minuti)}h {calcola_minuti(minuti)}min")


x=input("Inserisci un numero intero\n")
x=int(x)
print(x**2)
print(x**3)


x=input("Inserisci un numero intero\n")
x=int(x)
if(x%2==0):
    print("Il numero è pari")
else:
    print("Il numero è dispari")


x=input("Scegli una parola: ")
y=input("Scegli una lettera: ")
def conta_lettere(x, y):
    conta=0
    for i in x:
        if i==y:
            conta+=1
    print(f"{conta}")
conta_lettere(x, y)


x=input("Scegli un numero intero\n")
x=int(x)
def primo (x):
    for i in range(x//2):
        if (x%(i+2) == 0):
            print (f"{x} non è primo")
            return
    print (f"{x} è primo")
primo(x)


x=input("Inserisci un numero intero ")
x=int(x)
somma=0
while x!=0:
    somma=somma+x
    x=input("Inserisci un altro numero intero ")
    x=int(x)
print("La somma dei valori scritti è ")
print(f"{somma}")


x=input("Inserisci un numero intero ")
x=int(x)
valore=1
for i in range(x+1):
    if(i==0):
        i=i+1
    valore=valore*i
print("Il fattoriale del valore inserito è ")
print(f"{valore}")


x=input("Inserisci 3 numeri interi\n")
y=input()
z=input()
x=int(x)
y=int(y)
z=int(z)
def triangolo(x,y,z):
    if(x+y>z):
        if(x+z>y):
            if(y+z>x):
                if (x==y or y==z or x==z):
                    if(x==y and y==z):
                        print("I 3 valori possono essere i lati di un triangolo isoscele")
                        return
                    print("I 3 valori possono essere i lati di un triangolo iscoscele")
                    return
                print("I 3 valori possono essere i lati di un triangolo scaleno")
                return
    print("I 3 valori non possono essere i lati di un triangolo")
triangolo(x,y,z)


x=input("Scrivi una parola\n")
def conta_vocali(x):
    conta=0
    for t in x:
        if(t=="a" or t=="e" or t=="i" or t=="o" or t=="u"):
            conta+=1
    return conta
print("Nella parola ci sono", conta_vocali(x), "vocali")
"""