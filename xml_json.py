import json
from dicttoxml import dicttoxml
import xmltodict
import sys
import traceback
from xml.dom.minidom import parseString
"""
    Try parse values of a dict in type number
"""

def couldbe_number(string:str):
    if isinstance(string,str):
        return False
    
    string = string.strip()

    if string[0].isdecimal or string[0] == '-':
        return True
    
    else: return False 

def has_decimal_point(string:str):
    if isinstance(string,str):
        return False
    
    if ( '.' in value or ',' in value) in string:
        return True
    
    else: return False

def format_num_fields(array, next_item = None):

    next_item = array if next_item == None else next_item

    for item in next_item:

        print(type(item))

        if isinstance(item,tuple):
            print('Tuple unbox')
            new_item = item.copy()
            item = new_item[1]

        if not isinstance(item,dict):
            print('Not a dict')
            continue

        if len(item.keys()) == 1:
            print('pop item')
            new_item = item.copy()
            item = new_item.popitem()    
        
        if isinstance(item, dict):
            for key, value in item.items():
                try:
                    #print('\n',value,'\n inside instace')
                    if not isinstance(value,str):
                        continue
                    
                    if value[0] == '0' and not has_decimal_point(value):
                        continue  

                    if couldbe_number(value) and not has_decimal_point(value):
                        item[key] = int(value)

                    if couldbe_number(value) and has_decimal_point(value):
                        item[key] = float(value.replace(',','.'))    

                except Exception:
                    traceback.print_exc()
        else:
            
            teste = format_num_fields(array,[item[1]])
            
    
    return array            


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
                writer.write(xml.parseString(xml).toprettyxml())
        
        elif '.xml' in parametros[1]:
            with open(parametros[1], 'r') as reader:
                jsons = xmltodict.parse(reader.read())
            
            with open(parametros[1].replace('.xml','.json'), 'w') as writer:
                
                if 'root' in jsons:
                    jsons = jsons['root']  
                
                if 'item' in jsons:
                    jsons = jsons['item'] 

                if not isinstance(jsons,list):
                    jsons = [jsons]

                jsons = format_num_fields(jsons) 
                jsons = json.dump(jsons, writer,indent= 2)                          

    except Exception:
        traceback.print_exc()
