from dataclasses import dataclass 
from utils import couldbe_number

class Xml:
    body = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    added = False
    item = True
    
    def __add__(self, string:str):
        self.body += f'{string}\n'
        self.added = True
    
    def print(self):
        print(self.body)

    def add_item(self,key:str,value:str,parms = None):
        if parms == None:
            self.body += f'<{key}>{value}</{key}>\n' 

    def has_element(self):
        return self.added


def create(array:list, xml:Xml, comma:bool):
    root = True if xml.has_element() == False else False 
    
    firstk = 'Root' if root else ''
    key_par = ''

    #print(type(array),len(array))

    if len(array) == 1 and isinstance(array,list):
        array = array[0].copy()
        xml.item = False
        firstk = str(list(array.keys())[0])
        
        if len(array) == 1 and isinstance(array[firstk],dict):
            array = array[firstk]
            key_to_remove = []
            print('\n',type(array),len(array),'\n')

            if isinstance(array,dict):
                for k in array.keys():
                    if '@' in k:
                        key = k.replace('@','')
                        if couldbe_number(array[k]):
                            num = array[k].replace('.',',') if comma else array[k]
                            key_par += f' {key}={num}'
                            key_to_remove.append(k)
                        else:
                            key_par += f' {key}="{array[k]}"'
                            key_to_remove.append(k)

                for rem in key_to_remove: array.pop(rem)
                array = [array]
            else:
                print(' VALORES',array)
                xml.add_item(firstk,array[firstk])
                return 
            xml + f'<{firstk}{key_par}>'

    for elem in array:
        print('dentro for\n',len(elem),'\n',type(elem),'\n',elem,'\n')
        if isinstance(elem, dict):
            if len(elem) >= 1:
                #print(len(elem), elem)
                if isinstance(elem,dict):
                    next_val = str(list(elem)[0])

                if not isinstance(elem[next_val],dict):
                    xml + f'<item>' if xml.item else ''
                    for key, value in elem.items():
                        
                        if not isinstance(value,dict):
                            xml.add_item(key,value)
                            print('\n gravado ',key,value,'\n')
                        else:
                            print('\nDict inside dict', key,value,'\n')
                            create([{key:value}],xml,comma)

                    xml +'</item>'if xml.item else ''
                else:
                    print('\nRe create\n', elem)
                    for k,v in elem.items():
                        print(f'Dentro do Recreate \n{k}:{v} \n')
                        create([{k:v}],xml,comma)    
            else:
                print('\nchamada recu\n', elem)
                create([elem],xml,comma)
        elif isinstance(elem,list):
            create([elem],xml,comma)
        else:
            print('Não foi...')

    xml + f'</{firstk}>'  

def dicttoxml2(mylist:list, comma = False):
    xml = Xml()   
    create(mylist,xml, comma)
    print('\n')
    xml.print()