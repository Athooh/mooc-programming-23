# Write your solution 
import string

def change_case(orig_string: str):
    new_case = []
    nw_string = [char for char in orig_string]
    for case in nw_string:
        if case.isupper():
            new_case.append(case.lower())
        elif case.islower():
            new_case.append(case.upper())
        else:
            new_case.append(case)
    return "".join(new_case)

def split_in_half(orig_string: str):
    str_len = len(orig_string)
    mid = str_len // 2
    
    return orig_string[0:mid], orig_string[mid:]

def remove_special_characters(orig_string: str):
    updated_str = []
    nw_string = [char for char in orig_string]
    for case in nw_string:
        if case in string.ascii_letters or case in string.digits or case in string.whitespace:
            updated_str.append(case)
        else:
            continue
            
    return "".join(updated_str)

