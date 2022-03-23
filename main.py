from math import floor


rol_data1=[50,50,52,53,54,54,55,55,56,56,57,57,57,58,58,58,59,59,60,60,60,60,61,61,62,62,62,63,63,64,65,66,67,68,68,69,70,71,72,73]
rol_data2=[32.3,62.2,10.3,22,13.1,9.9,11.9,20,36.4,23.5,18,22.6,20.3,38.3,19.6,27.2,28.9,18.4,27.3,21.7,23.7,13.9,36.3,32.9,29.7,25.4,23.8,15.7,17,39.2,22.7,29.9,18.3,33]
rol_data3=[1,2,3,3,10,10,10,4,6,6,5,2,2,2,23,24,20,21,33,20,14,7,5,6]

class TableRow():
    def __init__(self,min_value,max_value,id):
        super().__init__()
        self.id=id
        self.min_value=round(min_value,2)
        self.max_value=round(max_value,2)
        self.label=f"[{ self.min_value}-{self.max_value}["
        self.elements=[]
        self.midpoint=round((self.max_value+self.min_value)/2,2)
        self.absolute_frequency=0
        self.accumulated_frequency=0
        self.relative_frequency=0
        

    def add_elemente(self,elemente):
        self.elements.append(elemente)
        self.absolute_frequency+=1
    
    def set_accumulated_frequency(self,num):
             self.accumulated_frequency=round(num,2)
             
    def set_relative_frequency(self,num):
            self.relative_frequency=round(num*100,2)

class Table():
    def __init__(self,data=[]):
        super().__init__()

        self.data=data
        
        if self.data!=[]:
                self.size=len(data)
                self.max_value=max(data)
                self.mim_value=min(data)

                self.class_num=self.get_class_num()
                self.range_num=self.get_range_num()
                self.amplitude=self.get_amplitude()
                
                self.table=self.init_table()
                self.generate_table()

    def get_class_num(self)->int:
            return 5 if 25>=self.size else self.next_int(self.size**0.5) 
        
    def get_range_num(self)->int:
            return round(self.max_value-self.mim_value,2)
        
    def get_amplitude(self)->int:
            return self.next_int(self.range_num/self.class_num)

    def next_int(self,value)->int:
            return int(floor(value)+1) if value>floor(value) else int(value)
        
    def init_table(self)->dict:
            upper_limit=self.mim_value+self.amplitude
            return[TableRow(upper_limit+self.amplitude*(i-1),upper_limit+self.amplitude*i,i+1)for i in range(self.class_num)]
    
    def find_row(self,num)->TableRow:
            for row in self.table:
                if num>=row.min_value and num<row.max_value:return row
    
    def get_modal_class(self):
           modal_row=self.table[0]
           for row in self.table:
                     if row.absolute_frequency>modal_row.absolute_frequency:
                        modal_row=row
           return modal_row
           
                       
    def accumulated_frequency_table(self)->None:
            for num in self.data:
                    row=self.find_row(num)
                    row.add_elemente(num)

    def cumulative_frequency_table(self)->None:
            for row_index in range(self.class_num):
                    if row_index==0:
                            self.table[row_index].set_accumulated_frequency(self.table[row_index].absolute_frequency)
                    else: 
                            self.table[row_index].set_accumulated_frequency(self.table[row_index-1].accumulated_frequency+self.table[row_index].absolute_frequency)

    def relative_frequency_table(self)->None:
            for row in range(self.class_num):
                    self.table[row].set_relative_frequency(self.table[row].absolute_frequency/self.size)


    def generate_table(self)->None:
        self.accumulated_frequency_table()
        self.cumulative_frequency_table()
        self.relative_frequency_table()

    def get_quartiles(self,quartiles)->float:
            order=self.size/quartiles+self.mim_value
            row=0
            prev_accumulated_frequency= 0 if row.id-1==0 else self.table[row.id-1].accumulated_frequency
            return row.min_value+(order-prev_accumulated_frequency)*self.amplitude/row.accumulated_frequency


    def set_table(self,talble_data):
            self.table=[]
            self.size=0
            for id,data in enumerate(talble_data):
               row=TableRow(data[0],data[1],id+1)
               row.absolute_frequency=data[2]
               self.size+=data[2]
               self.table.append(row)

            self.class_num=len(self.table)  
            self.max_value=talble_data[-1][1]
            self.mim_value=talble_data[0][0]
            self.range_num=self.max_value-self.mim_value
            self.amplitude=talble_data[0][1]-talble_data[0][0]
               
            self.cumulative_frequency_table()
            self.relative_frequency_table()

    def print_table(self)->None:
        for row in self.table:
                print(f"{row.id}-{row.label} |   {row.absolute_frequency} |  {row.accumulated_frequency}   |  {row.relative_frequency}%")

    def print_frequacy_grafic(self,grafic):
            for i in range(len(grafic)):
                    for j in range(len(grafic[i])):
                           print("*",end="")  if grafic[i][j]==1 else print(" ",end="")
                           print("    ",end="")
                    print("") 
            print("-"*3*(len(grafic)-1))

    def generate_frequacy_grafic(self):
            row_size=self.get_modal_class().absolute_frequency
            colum_size=self.class_num
            
            grafic=[[1 if i<row.absolute_frequency else 0 for i in range(row_size)]for row in self.table]
            self.print_frequacy_grafic(grafic)
            grafic=[[grafic[j][i] for j in range(colum_size)]for i in range(row_size)]
            grafic=[[grafic[-(i+1)][j] for j in range(colum_size)]for i in range(row_size)]
            self.print_frequacy_grafic(grafic)

                    
 

        
def main():
    table1=Table()
    talble_data=[[50,54,4],[54,58,9],[58,62,11],[62,66,7],[66,70,5],[70,74,4],[74,78,0]]
    table1.set_table(talble_data)
    #table2=Table(rol_data2)

    table1.generate_frequacy_grafic()
    #table1.get_quartiles(2)

    #table2.generate_table()
    #table2.print_table()
    
 
if __name__=="__main__":
    main()