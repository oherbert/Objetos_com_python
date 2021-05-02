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
