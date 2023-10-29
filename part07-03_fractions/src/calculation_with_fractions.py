# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    if not isinstance(amount, int) or amount <= 0:
        raise ValueError("The amount must be a positive integer greater than 0.")

    equal_fraction = Fraction(1, amount)

    fractions_list = [equal_fraction] * amount

    return fractions_list

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))
