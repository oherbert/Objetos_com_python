# Objetos_com_python

O programa pode ser executado via prompt, passando parametros ou arrastando o arquivo para o arquivo conversor.bat***. 

# O app tem 6 argumentos sendo eles:
 "comma = true/false" - Utiliza virgulas no lugar de ponto decimal, por default é false
 "root = root" - Um json sem uma chave principal por default é criado a chave 'root'
 "item = item" - Um json sem um nome para cada, objeto por default recebe a chave 'item'
 "path = local" - Caminho para leitura do arquivo para conversão, sendo o primeiro argumento da chamada ou utilizando "path = c:\seu\caminho"
 "decimal = 1" número de casas decimais para os numeros floats, por default, 1 casa decimal
 "output= None" indica onde será salvo o documento de saída, por default no mesmo local do documento de leitura.

 *** Lembrando que no arquivo conversor.bat é necessario alterar o local da chamada do programa o abrindo em um editor de textos, no abaixo exemplo ele está instalado em "C:\xml_json\xml_json.exe", a vantagem de utilizar o arquivo bat é que a chamada via prompt ou arrastando o arquivo, é possível deixar parametrizadas as configurações.

# Exemplo 1
C:\xml_json\xml_json.exe %1 "decimal=2" "comma=true" "root=Departamentos" "item=Departamento" %2
 O campo %1 é o primeiro parametro e o %2 seria o campo output, no caso estão default. 

# Exemplo 2 
C:\xml_json\xml_json.exe %1 "output=c:\Saidas" %2 %3 %4 %5 
 Todos os parâmetros, menos o output está default. 
Obs. o único parâmetro que tem alguma relevância na ordem é o primeiro, caso não seja passado "path=c:\caminho\do\seu\arquivo" casocontrario é irrelevante a ordem. 
