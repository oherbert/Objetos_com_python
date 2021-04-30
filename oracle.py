import cx_Oracle  
import sys
import json
from itertools import zip_longest
import datetime

argumentos = sys.argv
nome_arquivo = 'saida.json'

if len(argumentos) > 2:
    nome_arquivo = argumentos[2]

if len(argumentos) > 1:
    try:
        con = cx_Oracle.connect('hr/hr@localhost/XEPDB1')
        cursor = con.cursor()  
        cursor.execute(argumentos[1]) 

        colunas = [row[0] for row in cursor.description]

        dicionario = []

        for valores in list(cursor):
            linha = []
            for valor, coluna in zip_longest(valores,colunas):
                
                if isinstance(valor, datetime.datetime):
                    valor = valor.strftime(r'%d/%m/%Y %H:%M:%S')
                
                linha.append([coluna,valor])
            
            dicionario.append(dict(linha))

        with open(nome_arquivo,'w') as arquivo:
            json.dump(dicionario,arquivo,indent= 2)    
        
        cursor.close() 
        con.close()
    except Exception:
        print('Erro ao processar o comando')