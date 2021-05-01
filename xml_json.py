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
    if not isinstance(string,str):
        return False
    
    string = string.strip()

    if string[0].isdecimal or string[0] == '-':
        return True
    
    else: return False 

def has_decimal_point(string:str):
    if not isinstance(string,str):
        return False
    
    if  '.' in string or ',' in string:
        return True
    
    else: return False

def format_num_fields(elist:list, next_item = None):

    next_item = elist if next_item == None else next_item

    for item in next_item:

        if item == None:
            continue

        if isinstance(item,tuple):
            if not isinstance(item[1],str): 
                item = item[1]
            else:
                item = {item[0],item[1]}

        if not isinstance(item,dict):
            print('Not a dict')
            print('\n',item)
            if isinstance(item,list):
                print('\n it is a list \n')
                format_num_fields(elist,item)
            elif isinstance(item,tuple):
                print('it is ',type(item) )
                format_num_fields(elist,[item])
            else:
                print('continue',item)
            continue

        if len(item.keys()) == 1:
            val = list(item.keys())[0]
            val = str(val)
            if not isinstance(item[val],str):
                print('pop item')
                new_item = item.copy()
                item = new_item.popitem()    
        
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value,str):
                    try:
                        print(f'\n{value}\n')
                        if value[0] == '0' and not has_decimal_point(value):
                            continue  
                        
                        if couldbe_number(value) and not has_decimal_point(value):
                            item[key] = int(value)
                            print('int')
                            continue

                        if couldbe_number(value) and has_decimal_point(value):
                            item[key] = float(value.replace(',','.'))
                            print('float')    

                    except Exception:
                        traceback.print_exc()
                else:
                    format_num_fields(elist,[value])
        else:
            format_num_fields(elist,[item])              
    return elist            


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
