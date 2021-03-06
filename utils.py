def couldbe_number(string:str):
    if not isinstance(string,str):
        return False
    
    string = string.strip()
    aval = iter(string)
    stg = next(aval)

    if stg.isdecimal() or stg == '-':
        for st in aval:
            if not (st.isdecimal() or st =='.' or st ==','):
                return False
        return True
    
    else: return False 

def has_decimal_point(string:str):
    if not isinstance(string,str):
        return False
    
    if  '.' in string or ',' in string:
        return True
    
    else: return False

# Tratamento de duplos na str ou quebra de linnha
def format_str(string:str):
    old = ''
    new_string = ''
    for char in string:
        new = char
        char = '' if char == '\n' or char=='\t' else char
        char = '' if char == ' ' and (old == ' ' or old == '\n') else char
        old = char if new != ' ' and new !='\n' and new !='\t' else new
        new_string += char
    return new_string

def remove_empty_lines(string:str):
    lines = string.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != ""]
    string = ""
    
    for line in non_empty_lines:
        string += line + "\n"
    return string


"""
    Try parse values of a dict in type number
"""
def format_fields(elist:list, next_item:list = None):
    """
        Caso seja uma chamada recursiva o valor next_item deve ser atribuido,
        sempre deve ser passado uma lista
    """
    next_item = elist if next_item == None else next_item

    for item in next_item:
    
        if item == None:
            continue
        # Se tipo Tuple: unbox na tuple : se str cria um dict
        if isinstance(item,tuple):
            if not isinstance(item[1],str): 
                item = item[1]
            else:
                item = {item[0],item[1]}

        # Bloqueia de continuar caso não seja dict
        if not isinstance(item,dict):
            if isinstance(item,list):
                format_fields(elist,item)
            elif isinstance(item,tuple):
                format_fields(elist,[item])
            continue

        # Tratamento do dict
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value,str):
                    try:
                        # Bloqueio para tratamendo de str que començão com 0
                        if value[0] == '0' and not has_decimal_point(value):
                            continue  
                        
                        # Tratamento para int
                        elif couldbe_number(value) and not has_decimal_point(value):
                            item[key] = int(value)

                        # Tratamento para float
                        elif couldbe_number(value) and has_decimal_point(value):
                            item[key] = float(value.replace(',','.')) 
                        
                        # Tratamento de str puras
                        else:
                            item[key] = format_str(value)

                    except Exception:
                        traceback.print_exc()
                else:
                    format_fields(elist,[value])
        else:
            format_fields(elist,[item])              
    return elist