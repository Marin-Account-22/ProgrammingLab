"""
list_a=[1,3,5,7]
list_b=[2,4,6]
lista_nuova=[x*y for x in list_a for y in list_b if x*y>10]
print(lista_nuova)


def terna(a, b, c):
    if(a**2+b**2==c**2):
        return True
lista_triplette=[(a,b,c) for a in range(1, 21) for b in range(1, 21) for c in range(1, 21) if terna(a, b, c)]
print(lista_triplette)


lista_a=[0,1,3,4]
lista_b=["a", "b", "c"]
lista_mista=[(x, y) for x in lista_a for idx, y in enumerate(lista_b) if x%2==0 and idx%2!=0]
print(lista_mista)


sentence="the cat sat on the mat the cat"
parole=sentence.split()
diz={elemento: parole.count(elemento) for elemento in parole}
print(diz)
"""