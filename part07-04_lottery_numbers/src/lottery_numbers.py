# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    lucky_numbers = []
    count = 0

    while count < amount:
        num = randint(lower, upper)
        if num not in lucky_numbers:
            lucky_numbers.append(num)
            count += 1

    return sorted(lucky_numbers)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
