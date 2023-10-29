# Write your solution here
def even_numbers(beginning: int, maximum: int):
    number = beginning + (beginning % 2)
    while number <= maximum and number % 2 == 0:
        yield number
        number += 2

if __name__ == '__main__':
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)