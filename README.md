# Estatistica-decritiva
Esse projeto foi desenvolvido com proposito de aprendizagem dos conteúdos da disciplina de Probabilidade e Estatística e engloba 
apenas a parte de Estatística Descritiva é também para colocar em pratica conceitos de programação orientada a objetos.

O projeto ainda está em desenvolvimento então possui algumas limitações 
 - Apenas para dados agrupados 
 - Apenas class com amplitudes iguais
 
Como o propósito é a aprendizagem qualquer duvida ou sugestão para melhorar o código tanto na parte de eficiência ou na legibilidade 
são aceites, os contatos estão abaixo.
- contato.paycraft10@gmail.com
- njlima@uta.cv

# Como utilizar

### Inserir dados
>Caso seus dados estiverem  **distribuídos em rol** você deve colocar eles numa lista serandam cada elemento por uma virgula como demostrado no exemplo abaixo.
>
>Embora os dados estejam ordenados não a necessidade de colocar eles ordenados.
>````
>rol_data1 = [50,50,52,53,54,54,55,55,56,56,57,57,57,58,58,58,59,59,60,60,60,60,61,61,62,62,62,63,63,64,65,66,67,68,68,69,70]
>````
> Caso já tenha os dados numa **distribuição de frequência** você deve colocar os dados numa lista composto por variais lista onde o primeiro elemento é o limite inferior o segundo o limite superior e o terceiro a frequência absoluta.
> ````
> talble_data1 = [[50,54,4],[54,58,9],[58,62,11],[62,66,7],[66,70,5],[70,74,4],[74,78,0]]
> ````

### Criar uma tabela
>Caso seus dados estiverem **distribuídos em rol** você deve criar uma instância da ``Class Table`` passando como argumento a variável onde está guardado os dados segue o seguinte exemplo. 
>````
>table1 = Table(rol_data1)
>````
> Caso já tenha os dados numa **distribuição de frequência** você deve criar uma instância vazia da ``Class Table`` e depois passando os dados com o método  ``set_table()`` segue o seguinte exemplo,ao criar uma instancia vazia você não pode executar métodos da tabela antes de colocar dados nela.
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
>Para ver todas as informações sobre a tabela deve usar o método ``table_info()`` passando como argumento 'all' para ver todas as informações 
>````
>table1.table_info("all")
>````
>Caso queria apenas algumas informações você pode passar  uma string com cada um deles separados por virgulas, a ordem não importa.
>````
>table1.table_info("K,H,R,N")
>````
>As abreviações estão descritas abaixo
> - "K"   Numero de class
> - "R"   Range 
> - "H"   Amplitude
> - "N"   Tamanho 
> - "M"   Media
> - "Q1"  1° Quartil 
> - "Q3"  3° Quartil
> - "Mo"  Moda 
> - "MoC" Class modal
> - "Dm"  Desvio medio
> - "V"   Variancia 
> - "Dp"  Desvio padrao 
> - "Cv"  Coeficente de variacao
> - "1Cp" 1-Coeficente de Person 
> - "2Cp" 2-Coeficente de Person
> - "Ck"  Curtose

---
>### Separatrizes
>Para calcular as medidas separatrizes você deve usar o método ``get_separatrices()``
>
>O primeiro argumento é o valor que o n será dividido, e o segundo o valor de i que como padrão é igual a 1 caso não seja passado 
> ### Quartis
>
>Para calcular o 1° Quartil, o valor de n será dividido por 4
>````
>Q1 = table1.get_separatrices(4)
>````
>Para calcular o 2° Quartil, que é igual a media 
>````
>Q2 = table1.get_separatrices(2)
>````
>Para calcular o 3° Quartil , o segundo argumento que é 3 será atribuído ao i que será multiplicado pelo n sendo 3*n/4
>```
>Q3 = table1.get_separatrices(4,3)
>````
> ### Decis
> 
> O valor do i varia entre 1 a 9, mas o valor que n será divido sempre será 10
>
>Para calcular o 9° Decil 
>```
>D9 = table1.get_separatrices(10,9)
>````
>Para calcular o 5° Decil 
>```
>D5 = table1.get_separatrices(10,5)
>````
> ### Percentis
> 
> O valor do i varia entre 1 a 99, mas o valor que n será divido sempre será 100
>
>Para calcular o 99° percentil 
>```
>P99 = table1.get_separatrices(100,99)
>````
>Para calcular o 50° percentil 
>```
>P50 = table1.get_separatrices(100,50)
>````
### Ultima atualização 0.0.1
> - 

### Em  Breve
> - Suporte a dados  não agrupados 
> - Suporte a class com amplitudes diferentes



