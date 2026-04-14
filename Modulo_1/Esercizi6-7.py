"""
class CSVFile():
    def __init__(self, name):
        self.name=name
        if type(name)!=str:
            raise Exception("Il nome del file deve essere una stringa")
    def get_data(self, start=None, end=None):
        lista = []
        try:
            with open(self.name, 'r') as my_file:
                for i, riga in enumerate(my_file, start=1):
                    passa_start = (start is None or i >= start)
                    passa_end = (end is None or i <= end)
                    if passa_start and passa_end:
                        contenuto = riga.strip().split(",")
                        lista.append(contenuto)
        except FileNotFoundError:
            raise FileNotFoundError(f"Il file {self.name} non esiste")
        return lista
class NumericalCSVFile(CSVFile):
    def get_data(self):
        dati=super().get_data()
        numerical_data=[]
        for riga in dati:
            riga_convertita=[]
            riga_convertita.append(riga[0])
            try:
                for valore in riga[1:]:
                    riga_convertita.append(float(valore))
                numerical_data.append(riga_convertita)
            except Exception as e:
                print(f"Errore nella conversione della riga {riga}: {e}")
                continue
        return numerical_data
Vendite_shampoo=NumericalCSVFile("shampoo_sales.csv")
print(Vendite_shampoo.get_data())


from datetime import datetime
def data():
    try:
        nascita = input("Inserisci la tua data di nascita (GG/MM/AAAA): ")
        nascita = datetime.strptime(nascita, "%d/%m/%Y")
        oggi=datetime.now()
        età=oggi.year-nascita.year
        if(oggi.month, oggi.day) < (nascita.month, nascita.day):
            età-=1
        prossimo_compleanno=nascita.replace(year=oggi.year)
        if prossimo_compleanno<oggi:
            prossimo_compleanno=prossimo_compleanno.replace(year=oggi.year+1)
        differenza=prossimo_compleanno-oggi
        giorni=differenza.days
        ore, resto=divmod(differenza.seconds, 3600)
        minuti, secondi=divmod(resto, 60)
        print(f"Al tuo prossimo compleanno mancano {giorni} giorni, {ore} ore, {minuti} minuti e {secondi} secondi")
    except ValueError:
        print("La data scritta così non va bene!")
        data()
data()


def inserimento():
    try:
        intero=input("Inserisci un numero intero: ")
        intero=int(intero)
        intero=intero**2
        print(f"Il quadrato del numero inserito è {intero}")
    except ValueError:
        print("Il valore inserito non va bene, riprovare")
        inserimento()
inserimento()


def menù():
    x=True
    while x:
        try:
            scelta=input("Scegliere un'opzione: 1) per sommare 2 numeri, 2) per sottrarre due numeri, 3) per uscire  ")
            scelta=int(scelta)
            if(scelta==1):
                somma1=int(input("Scegli il primo numero da sommare: "))
                somma2=int(input("Scegli il secondo numero da sommare: "))
                print(f"La somma dei due numeri è {somma1+somma2}")
            if(scelta==2):
                differenza1=int(input("Scegli un numero: "))
                differenza2=int(input("scegli un da sottrarre al primo: "))
                print(f"La differenza dei due numeri è {differenza1-differenza2}")
            if(scelta==3):
                print("Grazie per aver usato il mio menù")
                x=False
            if(scelta<1 or scelta>3):
                print("Il numero inserito non è collegato ad una funzione, riprovare")
        except ValueError:
            print("Inserire un numero intero tra quelli proposti")
menù()
"""