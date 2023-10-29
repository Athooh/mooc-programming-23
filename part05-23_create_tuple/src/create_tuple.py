# Write your solution 
def create_tuple(x: int, y: int, z: int):
    new_tuple = ()
    smallest_tuple = min(x, y, z)
    largest_tuple = max(x, y, z)
    sum_tuple = x + y + z    
    
    new_tuple = (smallest_tuple, largest_tuple, sum_tuple)
    return new_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))