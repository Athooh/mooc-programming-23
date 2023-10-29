# Write your solution here
import math
def hypotenuse(leg1: float, leg2: float):
    leg3 = leg1**2 + leg2**2
    leg3 = math.sqrt(leg3)
    return leg3 

if __name__ == '__main__':
    print(hypotenuse(3,4))
    print(hypotenuse(5,12))
    print(hypotenuse(1,1))