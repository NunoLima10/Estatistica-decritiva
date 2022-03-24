from table import Table


rol_data1=[50,50,52,53,54,54,55,55,56,56,57,57,57,58,58,58,59,59,60,60,60,60,61,61,62,62,62,63,63,64,65,66,67,68,68,69,70,71,72,73]
rol_data2=[32.3,62.2,10.3,22,13.1,9.9,11.9,20,36.4,23.5,18,22.6,20.3,38.3,19.6,27.2,28.9,18.4,27.3,21.7,23.7,13.9,36.3,32.9,29.7,25.4,23.8,15.7,17,39.2,22.7,29.9,18.3,33]
rol_data3=[1,2,3,3,10,10,10,4,6,6,5,2,2,2,23,24,20,21,33,20,14,7,5,6]
talble_data1=[[50,54,4],[54,58,9],[58,62,11],[62,66,7],[66,70,5],[70,74,4],[74,78,0]]       
talble_data2=[[2,4,2],[4,6,4],[6,8,7],[8,10,4],[10,12,3]]

def main():
    table1=Table(rol_data1)
    #table1.set_table(talble_data2)
    table1.print_table()
    print(f"Media-{table1.get_separatrices(2)}")
    print(f"Moda-{table1.get_moda()}")
    print(f"Desvio medio-{table1.get_mean_deviation()}")
    print(f"Variancia-{table1.get_variance()}")
    print(f"Desvio padrao-{table1.get_standard_deviation()}")
    print(f"Coeficente de variacao-{table1.get_coefficient_of_variation()}")
    print(f"1-Coeficente de  Person-{table1.get_first_person_coefficient()}")
    print(f"2-Coeficente de  Person-{table1.get_second_person_coefficient()}")
   
  
if __name__=="__main__":
    main()