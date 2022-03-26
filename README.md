# Estatistica-decritiva
## Como usar

### Inserir dados
>Caso seus dados estiverem em **distribuídos de rol** você deve colocar eles numa lista serandam cada elemento por uma virgula como demostrado no exemplo abaixo.
>
>Embora os dados estejam ordenados não a necessidade de colocar eles ordenados em ordem.
>````
>rol_data1 = [50,50,52,53,54,54,55,55,56,56,57,57,57,58,58,58,59,59,60,60,60,60,61,61,62,62,62,63,63,64,65,66,67,68,68,69,70]
>````
> Caso já tenha os dados numa **distribuição de frequência** você deve colocar os dados numa lista composto por variais lista onde o primeiro elemento é o limite inferior o segundo o limite superior e o terceiro a frequência absoluta.
> ````
> talble_data1 = [[50,54,4],[54,58,9],[58,62,11],[62,66,7],[66,70,5],[70,74,4],[74,78,0]]
> ````

### Criar uma tabela
>Caso seus dados estiverem em **distribuídos de rol** você deve criar uma instância da ``Class Table`` passando como argumento a variável onde está guardado os dados seguindo o seguinte exemplo. 
>````
>table1 = Table(rol_data1)
>````
> Caso já tenha os dados numa **distribuição de frequência** você deve criar uma instância vazia da ``Class Table`` e depois passando os dados com o método  ``set_table()`` segue o seguinte exemplo.
> ````
> table1 = Table()
>table1.set_table(talble_data1)
>```` 
### Usar Metodos da tabela
>Para imprimir a tabela você deve usar o método ``print_table()`` segue o seguinte exemplo.
>````
>table1.print_table()
>````
>
>Para ver os dados da frequência absoluta em forma de gráfico deve usar o método ``generate_frequacy_grafic()``  segue o seguinte exemplo.
>````
>table1.generate_frequacy_grafic()
>````
>
>Para ver todas as  informações sobre a tabela deve usar o método ``table_info()`` passando como argumento 'all' para ver todas as informações 
>````
>table1.table_info("all")
>````

