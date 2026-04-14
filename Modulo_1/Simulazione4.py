class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=name
        try:
            file=open(self.name, "r")
            file.close()
        except Exception:
            raise ExamException("Errore: il file non è apribile")
    def get_data(self):
        lista_grande=[]
        try:
            file=open(self.name, "r")
        except Exception:
            raise ExamException("Il file non esiste")
        with file:
            for riga in file:
                elementi=riga.strip().split(",")
                if elementi[0]=="date":
                    continue
                try:
                    data=elementi[0]
                    passeggeri=int(elementi[1])
                    if passeggeri<=0:
                        continue
                    lista_grande.append([data, passeggeri])
                except:
                    print("Numero di passeggeri invalido, riga ignorata")
                    continue
        return lista_grande
def compute_variations(time_series, first_year, last_year):
    passeggeri_per_anno={}
    for data, passeggeri in time_series:
        anno=int(data.split("-")[0])
        if anno in range(first_year, last_year+1):
            if anno not in passeggeri_per_anno:
                passeggeri_per_anno[anno]=[]
            passeggeri_per_anno[anno].append(passeggeri)
    medie_anni={}
    for anno, passeggeri in passeggeri_per_anno.items():
        medie_anni[anno]=sum(passeggeri)/len(passeggeri)
    variazioni={}
    anni_presenti=sorted(medie_anni.keys())
    for i in range(1, len(anni_presenti)):
        anno1=anni_presenti[i-1]
        anno2=anni_presenti[i]
        intervallo=f"{anno1}-{anno2}"
        variazioni[intervallo]=medie_anni[anno2]-medie_anni[anno1]
    return variazioni