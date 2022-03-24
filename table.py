from math import floor
from table_row import TableRow
DECIMAL_PLACES=2

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
                

    #
    def get_class_num(self)->int:
            return 5 if 25>=self.size else self.next_int(self.size**0.5) 
        
    def get_range_num(self)->int:
            return round(self.max_value-self.mim_value,2)
        
    def get_amplitude(self)->int:
            return self.next_int(self.range_num/self.class_num)

    def next_int(self,value)->int:
            return int(floor(value)+1) if value>floor(value) else int(value)
                             
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

    def deviation_table(self)->None:
             for row in self.table:row.set_deviation(self.average)   

    def find_row(self,num)->TableRow:
            for row in self.table:
                if num>=row.min_value and num<row.max_value:return row
  
    def get_modal_class(self):
           modal_row=self.table[0]
           for row in self.table:
                     if row.absolute_frequency>modal_row.absolute_frequency:
                        modal_row=row
           return modal_row
 
    def get_separatrices(self,value_order,i=1)->float:
            order=i*self.size/value_order
            for row in self.table:
                 if order<row.accumulated_frequency:
                         row=self.table[row.id+1]
                         break

            prev_accumulated_frequency= 0 if row.id-1==-1 else self.table[row.id-1].accumulated_frequency
            return round(row.min_value+((order-prev_accumulated_frequency)/row.absolute_frequency)*self.amplitude,2)

    def get_moda(self)->float:
           row=self.get_modal_class()
           prev_absolute_frequency= 0 if row.id-1==-1 else self.table[row.id-1].absolute_frequency
           next_absolute_frequency= 0 if row.id+1>self.class_num-1 else self.table[row.id+1].absolute_frequency
           delta1=row.absolute_frequency-prev_absolute_frequency
           delta2=row.absolute_frequency-next_absolute_frequency
           return round(row.min_value+(delta1/(delta1+delta2))*self.amplitude,2)

    def get_average(self):
        return self.get_separatrices(2,1) 
#teste
    def get_mean_deviation(self)->float:
        sum=0
        for row in self.table:sum+=row.deviation*row.absolute_frequency
        return round(sum/self.size,2)

    def get_variance(self)->float:
        sum=0    
        for row in self.table:sum+=(row.deviation**2)*row.absolute_frequency
        return round(sum/self.size,2)

    def get_standard_deviation(self)->float:
        return round(self.get_variance()**0.5,2)

    def get_coefficient_of_variation(self):
        return round(self.get_standard_deviation()/self.amplitude,2)

    def get_first_person_coefficient(self):
        return round((self.average-self.get_moda())/self.get_standard_deviation(),2)

    def get_second_person_coefficient(self):
        Q1=self.get_separatrices(4)
        Q3=self.get_separatrices(4,3)
        return round((Q1+Q3-2*self.average)/Q3-Q1,2)

    def get_kurtosis(self):
        pass
    #--------build table------

    def init_table(self)->dict:
            upper_limit=self.mim_value+self.amplitude
            return[TableRow(upper_limit+self.amplitude*(i-1),upper_limit+self.amplitude*i,i)for i in range(self.class_num)]        
    
    def generate_table(self)->None:
        self.accumulated_frequency_table()
        self.cumulative_frequency_table()
        self.relative_frequency_table()

        self.average=self.get_average()
        self.deviation_table()

    def set_table(self,talble_data)->None:
            self.table=[]
            self.size=0
            for id,data in enumerate(talble_data):
               row=TableRow(data[0],data[1],id)
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

            self.average=self.get_average()
            self.deviation_table()
    
    #-----------grafic------

    def print_table(self)->None:
        print("id label |Fi      |Fa      |fi      |xi      |di      |")
        print("-------------------------------------------------------")
        for row in self.table:
                colums=[f"{row.id}-{row.label}",f"{row.absolute_frequency}",f"{row.accumulated_frequency}",f"{row.relative_frequency}%",f"{row.midpoint}",f"{row.deviation}"]
                
                for colum in colums:
                        print(colum,end="")
                        print(" "*(8-len(colum)),end="")
                        print("|",end="")
                print("")
                print("-------------------------------------------------------")

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
            grafic=[[grafic[j][i] for j in range(colum_size)]for i in range(row_size)]
            grafic=[[grafic[-(i+1)][j] for j in range(colum_size)]for i in range(row_size)]
            self.print_frequacy_grafic(grafic)