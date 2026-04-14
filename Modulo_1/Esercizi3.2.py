"""
parole = ["cane", "gatto", "cane", "uccello", "gatto", "cane"]
def conta_occorrenze(parole):
    diz = {}
    for i in parole:
        if i in diz:
            diz[i] += 1
        else:
            diz[i] = 1
    return diz
print(conta_occorrenze(parole))


def somma(file):
    totale=0
    with open(file, 'r') as my_file:
        next(my_file)
        for bagigi in my_file:
            totale+=int(bagigi)
    return totale
print(somma("shampoo_sales.csv"))


def conta_parola(file, parola):
    totale=0
    with open(file, 'r') as my_file:
        for scritta in my_file:
            elementi=scritta.split(',')
            for elemento in elementi:
                if (elemento==parola):
                    totale+=1
    return totale
print(conta_parola("parole_da_contare.csv", "Filippo"))


def dizionario(file):
    diz={}
    with open(file, 'r') as my_file:
        for riga in my_file:
            parole=riga.split(',')
            for parola in parole:
                if parola in diz:
                    diz[parola] += 1
                else:
                    diz[parola] = 1
    return diz
print(dizionario("parole_da_contare.csv"))


def trascrizione(file):
    righe_uniche=[]
    with open(file, "r") as my_file:
        for riga in my_file:
            riga=riga.strip()
            if riga not in righe_uniche:
                righe_uniche.append(riga)
    with open("Unique.txt", "w") as my_file:
        my_file.writelines(righe_uniche)
trascrizione("parole_da_contare.csv")
"""