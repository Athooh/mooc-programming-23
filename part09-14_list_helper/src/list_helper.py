# WRITE YOUR SOLUTION HERE:
class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        common_char = ""
        count = 0
        for char in my_list:
            if my_list.count(char) > count:
                count = my_list.count(char)
                common_char = char
        
        return common_char
    
    @classmethod
    def doubles(cls, my_list: list):
        doubles_list = []
        for char in my_list:
            if my_list.count(char) >= 2 and char not in doubles_list:
                doubles_list.append(char)

        return len(doubles_list)

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))