DECIMAL_PLACES=3


class TableRow():
    def __init__(self,min_value,max_value,id):
        super().__init__()
        self.id=id
        self.min_value=round(min_value,DECIMAL_PLACES)
        self.max_value=round(max_value,DECIMAL_PLACES)
        self.label=f"[{ self.min_value}-{self.max_value}["
        self.elements=[]
        self.midpoint=round((self.max_value+self.min_value)/2,DECIMAL_PLACES)
        self.absolute_frequency=0
        self.accumulated_frequency=0
        self.relative_frequency=0
        self.deviation=0
        

    def add_elemente(self,elemente):
        self.elements.append(elemente)
        self.absolute_frequency+=1
    
    def set_accumulated_frequency(self,num):
             self.accumulated_frequency=round(num,DECIMAL_PLACES)
             
    def set_relative_frequency(self,num):
            self.relative_frequency=round(num*100,DECIMAL_PLACES)
    
    def set_deviation(self,average):
        self.deviation=round(abs(self.midpoint-average),DECIMAL_PLACES)
