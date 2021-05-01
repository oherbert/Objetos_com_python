from dataclasses import dataclass 

class Xml:
    body = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    
    def __add__(self, string:str):
        self.body += f'{string}\n'
    
    def print(self):
        print(self.body)

    def add_item(self,key:str,value:str,parms = None):
        if parms == None:
            self.body += f'<{key}>{value}</{key}>\n' 


def create(array:list, xml:Xml):
    firstk = 'Root'

    print('\n',len(array),'\n')

    if len(array) == 1:
        array = array[0]
        firstk = str(list(array.keys())[0])
        print('\n',firstk,'\n')

    xml + f'<{firstk}>'
    root = True if 'Root' in firstk else False

    for elem in array:
        if isinstance(elem, dict):
            if len(elem) > 1:
                xml + f'<item>'
                for key, value in elem.items():
                    xml.add_item(key,value)
                xml + f'</item>'
            else:
                pass
       
    xml + f'</{firstk}>'  
    xml.print()

def dicttoxml2(mylist:list):
    xml = Xml()   
    create(mylist,xml)