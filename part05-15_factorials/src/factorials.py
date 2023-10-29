# Write your solution here
def factorials(n: int):
    fact_dict = {}
    x = 1    
    for i in range(1, n + 1):
        x *= i 
        fact_dict[i] = x
    
    return fact_dict
if __name__ == '__main__':
    k = factorials(1)
    print(k[1])
    print(k[3])
    print(k[5])
    