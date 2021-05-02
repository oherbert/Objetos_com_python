from dataclasses import dataclass 

class Xml:
    body = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    added = False
    item = True
    
    def __init__(self,comma:bool):
        self.comma = comma
    
    def __add__(self, string:str):
        self.body += f'{str(string)}\n'
        self.added = True

    def add_item(self,key:str,value:str,parms = None):
        if isinstance(value,float):
            value = str(value).replace('.',',') if self.comma else value

        self.body += f'<{key}>{str(value)}</{key}>\n' 

    def has_element(self):
        return self.added
    
    def print(self):
        print(self.body)


def create_xml(array:list, xml:Xml):
    root = True if xml.has_element() == False else False 
    
    firstk = 'Root' if root else ''
    key_par = ''

    # Tramento para lista
    if len(array) == 1 and isinstance(array,list):
        array = array[0].copy()
        xml.item = False
        firstk = str(list(array.keys())[0])
        
        # Tratamento de dict com 1 dict dentro
        if len(array) == 1 and isinstance(array[firstk],dict):
            
            array = array[firstk]
            key_to_remove = []
            print('\n',type(array),len(array),'\n')

            if isinstance(array,dict):
                for k in array.keys():
                    if '@' in k:
                        key = k.replace('@','')
                        if isinstance(array[k],float) or isinstance(array[k], int):
                            num = str(array[k]).replace('.',',') if comma else array[k]
                            key_par += f' {key}={num}'
                            key_to_remove.append(k)
                        else:
                            key_par += f' {key}="{array[k]}"'
                            key_to_remove.append(k)

                # Remove os parametros da chave
                for rem in key_to_remove: array.pop(rem)
                array = [array]
        # Dict com str dentro
        else:
            xml.add_item(firstk,array[firstk])
            return 
        xml + f'<{firstk}{key_par}>'

    for elem in array:
        #Tratamento dos dict internos
        if isinstance(elem, dict):
            if len(elem) >= 1:
                next_val = str(list(elem)[0])

                #Tratamento de int, flot ou str 
                if not isinstance(elem[next_val],dict):
                    xml + f'<item>' if xml.item else ''
                    for key, value in elem.items():
                        
                        if not (isinstance(value,dict) or isinstance(value,list)):
                            xml.add_item(key,value)

                        # Trataemto Tags com varios valores ex. Nomes:[a,b]    
                        elif isinstance(value,list):
                            for v in value:
                                create_xml([{key:v}],xml)
                        
                        # Tramento de Tags com outro dict dentro ex. Nome:{sobrenome:a,ultimo:b}  
                        else:
                            create_xml([{key:value}],xml)

                    xml +'</item>'if xml.item else ''
                #Caso seja uma lista ou outro dict dentro do dict 
                else:
                    for k,v in elem.items():
                        create_xml([{k:v}],xml)
            #    
            else:
                create_xml([elem],xml)

        # Se houve uma lista destro da lista
        elif isinstance(elem,list):
            create_xml(elem,xml)
        # Exception
        else:
            print('It was not possible to parse your Json')
            raise NameError('Parse Error')

    xml + f'</{firstk}>'  

def dicttoxml2(mylist:list, comma = False):
    xml = Xml(comma)   
    create_xml(mylist,xml)
    return xml.body
