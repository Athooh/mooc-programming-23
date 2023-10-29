# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.numb_list = []

    def add_number(self, number:int):
        self.numb_list.append(number)

    def count_numbers(self):
        return len(self.numb_list)
    
    def get_sum(self):
        if len(self.numb_list) == 0:
            return self.numbers
        else:
            return sum(self.numb_list)
    
    def average(self):
        if len(self.numb_list) == 0:
            return self.numbers
        else:
            return sum(self.numb_list) / len(self.numb_list)
        
    def sum_even(self):
        return sum([x for x in self.numb_list if x % 2 == 0])
    
    def sum_odd(self):
        return sum([x for x in self.numb_list if x % 2 != 0])
        
stats = NumberStats()
print("Please type in integer numbers:")
while True:
    num = int(input())
    if num < 0:
        break
    stats.add_number(num)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats.sum_even())
print("Sum of odd numbers:", stats.sum_odd())
    