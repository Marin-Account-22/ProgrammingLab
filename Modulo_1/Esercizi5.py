"""
class Canguro():
    def __init__(self):
        self.contenuto_tasca=[]
    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)
    def __str__(self):
        return f"{self.contenuto_tasca}"
can=Canguro()
guro=Canguro()
can.intasca("cocco")
print(can)
print(guro)


class Persona():
    def __init__(self, ruolo, nome, cognome):
        self.ruolo=ruolo
        self.name=nome
        self.surname=cognome
    def saluta(self):
        print("Ciao, sono", self.name, self.surname + ",", self.ruolo)
class Studente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi=corsi
    def saluta(self):
        Persona.saluta(self)
        print("Frequento i corsi:", self.corsi)
class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi=corsi
    def saluta(self):
        Persona.saluta(self)
        print("Sono il docente dei corsi:", self.corsi)
    def insegna_tutti(self, studente):
        for corso in studente.corsi:
            if corso not in self.corsi:
                print("Il prof {} {} non è adatto per {}".format(self.name, self.surname, studente.name))
                return False
        print("Il prof {} {} è perfetto per {}".format(self.name, self.surname, studente.name))
        return True
corsi_Del_Santo=["Programmazione", "Laboratorio", "Analisi", "Geometria"]
Del_Santo=Docente("Giuseppe", "Del Santo", corsi_Del_Santo)
corsi_Andrea=["Programmazione", "Laboratorio", "Analisi", "Geometria"]
Andrea=Studente("Andrea", "Marin", corsi_Andrea)
studenti=[Andrea]
docenti=[Del_Santo]
def verifica_docenti(studenti, docenti):
    for studente in studenti:
        trovato=False
        for docente in docenti:
            if docente.insegna_tutti(studente):
                trovato=True
        if trovato:
            print(studente.name, studente.surname, "ha un docente per tutti i corsi")
        else:
            print(studente.name, studente.surname, "non ha un docente per tutti i corsi")
verifica_docenti(studenti, docenti)


class Veicolo():
    def __init__(self, marca, modello):
        self.modello=modello
        self.marca=marca
    def __str__(self):
        return f"{self.marca}  {self.modello}"
class Auto(Veicolo):
    def __init__(self, marca, modello, numero_porte):
        super().__init__(marca, modello)
        self.porte=numero_porte
    def __str__(self):
        return f"{self.marca} {self.modello} {self.porte}"
class Moto(Veicolo):
    def __init__(self, marca, modello, tipo):
        super().__init__(marca, modello)
        self.tipo=tipo
    def __str__(self):
        return f"{self.marca} {self.modello} {self.tipo}"
Polo=Auto("Wolksvagen", "Polo", "4 porte")
print(Polo)
"""