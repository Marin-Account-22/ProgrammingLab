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
            raise ExamException("Errore: impossibile aprire il file")
    def get_data(self):
        lista_grande=[]
        with open(self.name, "r") as file:
            for riga in file:
                elementi=riga.strip().split(",")
                data=str(elementi[0])
                if(float(elementi[2])<5):
                    temperatura=float(elementi[1])
                    lista_grande.append([data, temperatura])
                else:
                    print("Data saltata perché valore troppo incerto")
def compute_month_variation(time_series, first_year, second_year):
    if(type(first_year) is not int or type(second_year) is not int):
        raise ExamException("Errore: gli anni inseriti devono essere di tipo interi")
    if(second_year<=first_year):
        raise ExamException("Errore: il secondo anno deve essere maggiore del primo")
    anno1={}
    anno2={}
    for data, temperatura in time_series:
        mese=int(data.split("/")[1])
        anno=int(data.split("/")[2])
        if anno==first_year:
            anno1[mese]=temperatura
        if anno==second_year:
            anno2[mese]=temperatura
    variazioni={}
    for mese in range(1, 13):
        if mese in anno1 and mese in anno2:
            variazioni[mese]=anno2[mese]-anno1[mese]
        else:
            print("La variazione per il mese {} non può essere calcolata".format(mese))
    if variazioni=={}:
        raise ExamException("Gli anni considerati non hanno mesi validi")
    return variazioni