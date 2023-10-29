# Write your solution here
import re

def is_dotw(my_string: str):
    dotw_expression = r'\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b'

    match = re.search(dotw_expression, my_string)

    return bool(match)

def all_vowels(my_string: str):
    vowel_expression = r'^[aeiouAEIOU]+$'

    return bool(re.match(vowel_expression, my_string))

import re

def time_of_day(my_string: str):
    time_expression = r'^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'

    return bool(re.match(time_expression, my_string))

if __name__ == '__main__':
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))


