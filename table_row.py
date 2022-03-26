__author__="Nuno Lima"
__copyright__="Copyright 2022 Nuno Lima"
__version__="0.0.1"
__maintainer__="Nuno Lima"
__email__="contato.playcraft@gmail.com or njlima@uta.cv"
__status__="Production"

DECIMAL_PLACES = 3


class TableRow():
    def __init__(self, min_value, max_value, id):
        super().__init__()
        self.id = id
        self.min_value = round(min_value,DECIMAL_PLACES)
        self.max_value = round(max_value,DECIMAL_PLACES)
        self.label = f"[{ self.min_value}-{self.max_value}["
        self.elements = []
        self.midpoint = round((self.max_value+self.min_value)/2,DECIMAL_PLACES)
        self.absolute_frequency = 0
        self.accumulated_frequency = 0
        self.relative_frequency = 0
        self.deviation = 0
        

    def add_elemente(self, elemente) -> None:
        self.elements.append(elemente)
        self.absolute_frequency += 1
    
    def set_accumulated_frequency(self, num)-> None:
             self.accumulated_frequency = round(num,DECIMAL_PLACES)
             
    def set_relative_frequency(self, num)-> None:
            self.relative_frequency = round(num*100,DECIMAL_PLACES)
    
    def set_deviation(self,average)-> None:
        self.deviation = round(abs(self.midpoint-average),DECIMAL_PLACES)
