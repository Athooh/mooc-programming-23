# Write your solution here

def dict_of_numbers():
    number_dict = {}
    
    single_digits = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    for dgt in range(100):
        if dgt in single_digits and dgt >= 0 and dgt <= 10:
            number_dict[dgt] = single_digits[dgt]
        elif dgt >= 10 and dgt < 20 and dgt in teens:
            number_dict[dgt] = teens[dgt]
        else:
            tens_digit = (dgt // 10) * 10
            ones_digit = dgt % 10
            if ones_digit == 0:
                number_dict[dgt] = tens[tens_digit]
            else:
                number_dict[dgt] = tens[tens_digit] + "-" + single_digits[ones_digit]

    return number_dict

if __name__ == '__main__':
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
