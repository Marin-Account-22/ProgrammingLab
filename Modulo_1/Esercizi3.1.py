"""
my_list= [1,2,3,4]
def somma(lista):
    return sum(lista)
print(somma(my_list))
/
my_list= [1,2,3,4]
def somma_lista(lista):
    y=0
    for i in lista:
        y+=i
    return y
print(somma_lista(my_list))


mia_stringa= "anna"
def palindromo(stringa):
    y=0
    for i in stringa:
        if(i!=stringa[-1-y]):
            return False
        y+=1
    return True
print(palindromo(mia_stringa))


A=[1,2,3,4]
def scambio(lista, i, j):
    t=lista[j]
    lista[j]=lista[i]
    lista[i]=t
    return lista
print(scambio(A, 1, 2))


A=[1,2,3,4]
my_list=[5,6,2,8,9]
def uguali(lista1, lista2):
    for x in lista1:
        for i in lista2:
            if(x==i):
                return True
    return False
print(uguali(A, my_list))


A=[4,9,1,3]
def alfabetizzazione(lista):
    numeri=["Zero", "Uno", "Due", "Tre", "Quattro", "Cinque", "Sei", "Sette", "Otto", "Nove"]
    nuova_lista=[]
    for i in lista:
        nuova_lista.append(numeri[i])
    return nuova_lista
print(alfabetizzazione(A))
"""