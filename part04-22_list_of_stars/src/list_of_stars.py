# Write your solution here
def list_of_stars(my_list):
    for x in my_list:
        print(f"{'*' * x}")
        
if __name__ == '__main__':
    list_of_stars([3, 7, 1, 1, 2])