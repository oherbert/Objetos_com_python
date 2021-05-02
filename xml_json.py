import json
from dict2xml import dicttoxml2
import xmltodict
import sys
import traceback
from xml.dom.minidom import parseString
from utils import couldbe_number, format_str, has_decimal_point, remove_empty_lines, format_fields
            
args = sys.argv

if len(args) > 1:

    parms = {
    'comma': False,
    'root': 'root',
    'item': 'item',
    'path': '',
    'decimal': None
    }

    for par in args:
        if '=' in par: 
            kv = par.split('=')
            kv[0] = kv[0].strip()
            kv[1] = kv[1].strip()

            if kv[0].upper() == "COMMA":
                kv[1] = True if 'TRUE' == kv[1].upper() else False

            if kv[0].upper() == "ROOT":
                kv[1] = kv[1] if '' != kv[1] else 'root'

            if kv[0].upper() == "ITEM":
                kv[1] = kv[1] if '' != kv[1] else 'item'  

            if kv[0].upper() == "DECIMAL":
                kv[1] = int(kv[1]) if kv[1].isdecimal() else None
            
            parms.update({kv[0].strip():kv[1]})
            print(kv[0],kv[1])

    if parms['path'] == '':
        parms['path'] = args[1] if 'JSON' in args[1].upper() or 'XML' in args[1].upper() else None
        if parms['path'] == None: raise NameError('File not informed, use first parms as file path or path=file.json')

    try:
        jsons = []
        xml = []

        if '.json' in parms['path']:
            with open( parms['path'], 'r') as reader:
                jsons = json.loads(reader.read())
            
            with open(parms['path'].replace('.json','.xml'), 'w') as writer:                
                
                xml = dicttoxml2(jsons,parms['comma'],parms['root'],parms['item'],parms['decimal'])
                try:
                    xml = parseString(xml).toprettyxml()
                except Exception:
                    print('Tags Missed, it not a xml')
                    raise NameError('Incorret out xml')

                xml = remove_empty_lines(xml)
                writer.write(xml)
        
        elif '.xml' in parms['path']:
            with open(parms['path'], 'r') as reader:
                jsons = xmltodict.parse(reader.read())
            
            with open(parms['path'].replace('.xml','.json'), 'w') as writer:
                if 'root' in jsons:
                    jsons = jsons['root']  
                
                if 'item' in jsons:
                    jsons = jsons['item'] 

                if not isinstance(jsons,list):
                    jsons = [jsons]

                jsons = format_fields(jsons) 
                jsons = json.dump(jsons, writer,indent= 2)                          

    except Exception:
        traceback.print_exc()
else:
    print('Not arguments found')