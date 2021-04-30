import json
from dicttoxml import dicttoxml
import xmltodict
import sys
import traceback
from xml.dom.minidom import parseString
"""
    Try parse values of a dict in type number
"""
def try_parse_number(lista:list):
    for item in lista:
        for key, value in item.items():
            try:
                item[key] = int(value)
            except Exception:
                try:
                    item[key] = float(value)
                except Exception:
                    pass
    return lista            


parametros = sys.argv

if len(parametros) > 1:

    try:
        jsons = []
        xml = []

        if '.json' in parametros[1]:
            with open(parametros[1], 'r') as reader:
                jsons = json.loads(reader.read())
            
            with open(parametros[1].replace('.json','.xml'), 'w') as writer:
                xml = dicttoxml(jsons, attr_type=False)
                writer.write(parseString(xml).toprettyxml())
        
        elif '.xml' in parametros[1]:
            with open(parametros[1], 'r') as reader:
                jsons = xmltodict.parse(reader.read()) 
            
            with open(parametros[1].replace('.xml','.json'), 'w') as writer:
                if 'root' in jsons:
                    jsons = jsons['root']  
                
                if 'item' in jsons:
                    jsons = jsons['item'] 

                if not isinstance(jsons,list):
                    print('\n\n', 'Aqui','\n\n')
                    jsons = [jsons]

                print('\n',type(jsons),'\n')

                jsons = try_parse_number(jsons) 
                jsons = json.dump(jsons, writer,indent= 2)                          

    except Exception:
        traceback.print_exc()
