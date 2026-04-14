"""
class ExamException(Exception):
    pass
class MovingAverage():
    def __init__(self, lunghezza):
            self.lunghezza=lunghezza
            if not isinstance(self.lunghezza, int):
                raise ExamException("Inserisci un numero intero")
            if(self.lunghezza<1):
                raise ExamException("Inserisci un valore maggiore di 0")
    def compute(self, lista):
            if not isinstance(lista, list):
                raise ExamException("L'input deve essere una lista")
            if(len(lista)<self.lunghezza):
                raise ExamException("La lista deve essere più lunga della finestra")
            try:
                medie_mobili=[]
                for i in range(len(lista)-self.lunghezza+1):
                    caso=lista[i:i+self.lunghezza]
                    media=sum(caso)/self.lunghezza
                    medie_mobili.append(media)
                return medie_mobili
            except TypeError:
                raise ExamException("La lista deve contenere solo numeri interi")
moving_average=MovingAverage(2)
print(moving_average.compute([1,2,3,4,5]))
"""