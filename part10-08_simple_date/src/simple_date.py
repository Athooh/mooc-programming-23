# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        return self.day < other.day

    def __gt__(self, other):
        if self.year != other.year:
            return self.year > other.year
        if self.month != other.month:
            return self.month > other.month
        return self.day > other.day

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __add__(self, days):
        day = self.day + days
        month = self.month
        year = self.year

        while day > 30:  
            if month == 12:  
                year += 1
                month = 1
            else:
                month += 1
            day -= 30

        return SimpleDate(day, month, year)
    
    def __sub__(self, other):
        days_per_month = 30
        days_in_year = 12 * days_per_month
        days1 = self.year * days_in_year + self.month * days_per_month + self.day
        days2 = other.year * days_in_year + other.month * days_per_month + other.day

        return abs(days1 - days2)

if __name__ == '__main__':
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)





        
