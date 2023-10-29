# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("length must not be below zero")
        
    # A getter method
    @property
    def length(self):
        return self.__length
        
    
    # A setter method
    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("length must not be below zero")

if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)