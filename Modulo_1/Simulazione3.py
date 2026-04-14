class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=name
        try:
            file=open(self.name, "r")
        except Exception:
            raise ExamException("Errore: impossibile aprire il file")
        try:
            file.readline()
        except:
            raise ExamException("Errore: il file è vuoto o non contiene dati validi")
        file.close()
    def get_data(self, country):
        lista_grande=[]
        paese_presente=False
        with open(self.name, "r") as file:
            for riga in file:
                elementi=riga.strip().split(",")
                if elementi[0]=="dt":
                    continue
                data=elementi[0]
                temperatura=elementi[1]
                paese=elementi[2]
                if paese==country:
                    paese_presente=True
                    try:
                        lista_grande.append([data, float(temperatura)])
                    except Exception:
                        continue
        if not paese_presente:
            raise ExamException("Errore: il nome del paese non è presente nel file")
        return lista_grande
def compute_variations(time_series_1, time_series_2, first_year, last_year):
    if(type(first_year) is not int or type(last_year) is not int):
        raise ExamException("Errore: l'anno inserito non è un intero")
    temperature_paese_1={}
    temperature_paese_2={}
    for data, temperatura in time_series_1:
        anno=int(data.split("-")[0])
        if anno in range(first_year, last_year+1):
            if anno not in temperature_paese_1:
                temperature_paese_1[anno]=[]
            temperature_paese_1[anno].append(temperatura)
    for data, temperatura in time_series_2:
        anno=int(data.split("-")[0])
        if anno in range(first_year, last_year+1):
            if anno not in temperature_paese_2:
                temperature_paese_2[anno]=[]
            temperature_paese_2[anno].append(temperatura)
    medie_annuali_1={}
    medie_annuali_2={}
    for year, temperature in temperature_paese_1.items():
        if year in range(first_year, last_year+1):
            medie_annuali_1[year]=sum(temperature)/len(temperature)
    for year, temperature in temperature_paese_2.items():
        if year in range(first_year, last_year+1):
            medie_annuali_2[year]=sum(temperature)/len(temperature) 
    variazioni={}
    for anno in range(first_year, last_year+1):
        if anno in medie_annuali_1 and anno in medie_annuali_2:
            variazioni[str(anno)]=medie_annuali_2[anno]-medie_annuali_1[anno]
        else:
            continue
    if variazioni=={}:
        raise ExamException("Errore: l'intervallo selezionato non contiene valori validi")