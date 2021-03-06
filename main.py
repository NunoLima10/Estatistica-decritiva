
__author__="Nuno Lima"
__copyright__="Copyright 2022 Nuno Lima"
__version__="0.0.1"
__maintainer__="Nuno Lima"
__email__="contato.playcraft@gmail.com or njlima@uta.cv"
__status__="Production"

from table import Table

rol_data1 = [50,50,52,53,54,54,55,55,56,56,57,57,57,58,58,58,59,59,60,60,60,60,61,61,62,62,62,63,63,64,65,66,67,68,68,69,70,71,72,73]
rol_data2 = [32.3,62.2,10.3,22,13.1,9.9,11.9,20,36.4,23.5,18,22.6,20.3,38.3,19.6,27.2,28.9,18.4,27.3,21.7,23.7,13.9,36.3,32.9,29.7,25.4,23.8,15.7,17,39.2,22.7,29.9,18.3,33]
rol_data3 = [1,2,3,3,10,10,10,4,6,6,5,2,2,2,23,24,20,21,33,20,14,7,5,6]
talble_data1 = [[50,54,4],[54,58,9],[58,62,11],[62,66,7],[66,70,5],[70,74,4],[74,78,0]]       
talble_data2 = [[2,4,2],[4,6,4],[6,8,7],[8,10,4],[10,12,3]]
rol_data4 = [230,235,200,175,170,290,181,245,150,190,120,145,220,225,215,195,200,230,240,200,230,165,265,210,250,210,215,190,270,250]

def main():

    print("Exemplo 1\n\n\n")

    table1 = Table(rol_data1)
    table1.print_table()
    table1.table_info("all")
    table1.generate_frequacy_grafic()

    
    print("\n\n\nExemplo 2\n\n\n")

    table2 = Table()
    table2.set_table(talble_data2)
    table2.print_table()
    table2.table_info("all")
    table2.generate_frequacy_grafic()
     
 
if __name__=="__main__":
    main()