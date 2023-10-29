# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
        self.tot_height = 0
        
    def add(self, person: Person):
        self.persons.append(person)
        self.tot_height += person.height
        
    def is_empty(self):
        if len(self.persons) == 0:
            return True
        else:
            return False
        
    def print_contents(self):
        if not self.is_empty():
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.tot_height}cm")
        for person in self.persons:
            print(f"{person.name} ({person.height}cm)")
    
    def shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            short_person = self.persons[0].name
            short_height = self.persons[0].height
            for person in self.persons:
                if person.height < short_height:
                    short_person = person.name
                    short_height = person.height
            return short_person
    
    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            shortest_person = self.persons[0]
            shortest_index = 0
            for index, person in enumerate(self.persons):
                if person.height < shortest_person.height:
                    shortest_person = person
                    shortest_index = index
            
            removed = self.persons.pop(shortest_index)
            self.tot_height -= removed.height
            return removed

if __name__ == '__main__':
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()