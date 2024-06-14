"""
This is to test whether a collection of operations op, R1, R2, R3, R4 
is a stuquandle
"""
from util.quandle import Stuquandle

q = [
    [0, 2, 0, 2],
    [3, 1, 3, 1],
    [2, 0, 2, 0],
    [1, 3, 1, 3]
]

R1 = [
    [0, 3, 2, 1],
    [2, 1, 0, 3],
    [0, 3, 2, 1],
    [2, 1, 0, 3]
]

R2 = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]
]

R3 = [
    [0, 2, 0, 2],
    [3, 1, 3, 1],
    [2, 0, 2, 0],
    [1, 3, 1, 3]
]

R4 = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
]

def main():
    # after inputting your ops above, this will tell u 
    stq = Stuquandle()
    stq.assign_operations([q, R1, R2, R3, R4])
    print("Is it a stuquandle:", (stq.is_stuquandle()))

if __name__ == "__main__":
    main()