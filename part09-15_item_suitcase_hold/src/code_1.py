# Write your solution here:
class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight
        
    def get_name(self):
        return self.__name
    
    def get_weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

# class Hold:
#     pass

class Suitcase:
    def __init__(self, max_weight: float):
        self.max_weight = max_weight
        self.suitcase = []
        
    def add_item(self, item: Item):
        if self.total_weight() + item.get_weight() <= self.max_weight: 
            self.suitcase.append(item)

    def total_weight(self):
        return sum(item.get_weight() for item in self.suitcase)
    
    def print_items(self):
        for item in self.suitcase:
            print(item)
        
    def weight(self):
        weight = self.total_weight()
        return int(weight)
    
    def heaviest_item(self):
        if not self.suitcase:
            return None
        
        heaviest = self.suitcase[0]
        for item in self.suitcase:
            if item.get_weight() > heaviest.get_weight():
                heaviest = item
                
        return heaviest
        
    
        
    def __str__(self):
        if len(self.suitcase) != 1:
            return f"{len(self.suitcase)} items ({self.total_weight()} kg)"
        else:
            return f"{len(self.suitcase)} item ({self.total_weight()} kg)"


class CargoHold:
    def __init__(self, max_weight: float):
        self.max_weight = max_weight
        self.suitcases = []

    def add_suitcase(self, suitcase):
        if self.total_weight() + suitcase.total_weight() <= self.max_weight:
            self.suitcases.append(suitcase)

    def total_weight(self):
        return sum(suitcase.total_weight() for suitcase in self.suitcases)

    def __str__(self):
        return f"{len(self.suitcases)} suitcase{'s' if len(self.suitcases) != 1 else ''}, space for {self.max_weight - self.total_weight()} kg"
    
    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()

if __name__ == '__main__':
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
