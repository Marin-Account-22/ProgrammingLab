class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=name
        try:
            file=open(self.name, "r")
            file.readline()
            file.close()
        except Exception:
            raise ExamException("Errore: file non esistente o non leggibile")
    def get_data(self):
        lista_grande=[]
        with open(self.name, "r") as file:
            for riga in file:
                elementi=riga.strip().split(",")
                if elementi[0]=="dt":
                    continue
                data=elementi[0]
                try:
                    temperatura=float(elementi[1])
                    if temperatura<=0:
                        continue
                    lista_grande.append([data, temperatura])
                except Exception:
                    continue
def compute_variations(time_series, first_year, last_year, N):
    if N>=last_year-first_year+1:
        raise ExamException("N deve essere strettamente minore dell'intervallo")
    temperature_anni={}
    for data, temperatura in time_series:
        anno=int(data.split("-")[0])
        if first_year<=anno<=last_year:
            if anno not in temperature_anni:
                temperature_anni[anno]=[]
            temperature_anni[anno].append(temperatura)
    medie_annuali={}
    for year, temperatures in temperature_anni.items():
        medie_annuali[year]=sum(temperatures)/len(temperatures)
    medie_precedenti={}
    for anno in range(first_year+N, last_year+1):
        medie_precedenti[anno]=0
        for i in range(1, N+1):
            medie_precedenti[anno]+=(medie_annuali[anno-i])
        medie_precedenti[anno]=medie_precedenti[anno]/N
    variazioni={}
    for anno in medie_precedenti.keys():
        variazioni[str(anno)]=medie_annuali[anno]-medie_precedenti[anno]
    return variazioni