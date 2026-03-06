"""
def conta_occorrenze(parole):
    diz = {}
    for i in parole:
        if i in diz:
            diz[i] += 1
        else:
            diz[i] = 1
    return diz
parole = ["cane", "gatto", "cane", "uccello", "gatto", "cane"]
print(conta_occorrenze(parole))


def somma_vendite(file):
    somma = 0
    with open(file, "r") as f:
        for riga in f:
            riga = riga.strip()
            if riga:
                somma += float(riga)
    return somma
"""
def somma(file):
    totale=0
    my_file=open(file, 'r')
    next(my_file)
    for line in my_file:
        data, vendite=line.split(",")
        totale+=float(vendite)
    my_file.close()
    return totale
print(somma("shampoo_sales.csv"))