import itertools
from util.polynomial import StuquandlePolynomial

# q = [
#     [0, 2, 0, 2],
#     [3, 1, 3, 1],
#     [2, 0, 2, 0],
#     [1, 3, 1, 3]
# ]

# q = [[0,0,0], [0,0,0], [0,0,0]]

# R1 = [
#     [0, 3, 2, 1],
#     [2, 1, 0, 3],
#     [0, 3, 2, 1],
#     [2, 1, 0, 3]
# ]

# R2 = [
#     [0, 0, 0, 0],
#     [1, 1, 1, 1],
#     [2, 2, 2, 2],
#     [3, 3, 3, 3]
# ]

# R3 = [
#     [0, 2, 0, 2],
#     [3, 1, 3, 1],
#     [2, 0, 2, 0],
#     [1, 3, 1, 3]
# ]

# R4 = [
#     [0, 1, 2, 3],
#     [0, 1, 2, 3],
#     [0, 1, 2, 3],
#     [0, 1, 2, 3]
# ]

q = [[0, 2, 4, 1, 3], [4, 1, 3, 0, 2], [3, 0, 2, 4, 1], [2, 4, 1, 3, 0], [1, 3, 0, 2, 4]]
R1 = [[0, 2, 4, 1, 3], [4, 1, 3, 0, 2], [3, 0, 2, 4, 1], [2, 4, 1, 3, 0], [1, 3, 0, 2, 4]]
R2 = [[0, 3, 1, 4, 2], [3, 1, 4, 2, 0], [1, 4, 2, 0, 3], [4, 2, 0, 3, 1], [2, 0, 3, 1, 4]]
R3 = [[0, 3, 1, 4, 2], [3, 1, 4, 2, 0], [1, 4, 2, 0, 3], [4, 2, 0, 3, 1], [2, 0, 3, 1, 4]]
R4 = [[0, 2, 4, 1, 3], [4, 1, 3, 0, 2], [3, 0, 2, 4, 1], [2, 4, 1, 3, 0], [1, 3, 0, 2, 4]]

def check_rules_link1(coloring):
    a, b, c, d = coloring
    if (R1[b][d] == a and q[a][d] == b and 
        q[c][a] == d and R2[b][d] == c):
        return True
    return False

def check_rules_link2(coloring):
    a, b, c, d, e = coloring 
    if (R1[c][e] == a and R4[d][a] == b and
        R2[c][e] == d and q[b][e] == c and R3[d][a] == e):
        return True 
    return False

def main():
    n = 5 # Z_n (you can change it to size of the tables)

    count_inv1 = 0
    count_inv2 = 0
    colorings1 = []
    colorings2 = []

    # Coloring 1st link
    for coloring in itertools.product(range(n), repeat=4): # repeat= number of arcs
        print("COLORING:", list(coloring))
        if check_rules_link1(list(coloring)):
            count_inv1 += 1 
            colorings1.append(list(coloring))
    
    # Coloring 2nd link
    for coloring in itertools.product(range(n), repeat=5): # repeat= number of arcs
        print("COLORING:", list(coloring))
        if check_rules_link2(list(coloring)):
            count_inv2 += 1
            colorings2.append(list(coloring))

    print("------------------")
    print("Counting invariant for Link 1:", count_inv1)
    print("Counting invariant for Link 2:", count_inv2)
    print()
    print("Colorings for Link 1:", colorings1)
    print("Colorings for Link 2:", colorings2)
    print("------------------")
    print("Are the colorings the same:", (colorings1 == colorings2))

    # Stuquandle Polynomials
    stq = StuquandlePolynomial()
    stq.form_stuquandle_poly_list([q, R1, R2, R3, R4])

    print("------LINK 1-------")
    for coloring in colorings1:
        stq.print_substuquandle(coloring, [q, R1, R2, R3, R4])
    print("------LINK 2-------")
    for coloring in colorings2:
        stq.print_substuquandle(coloring, [q, R1, R2, R3, R4])


if __name__ == "__main__":
    main()
