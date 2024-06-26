from util.quandle import Stuquandle

# CHANGE THE MOD N BELOW
n = 3
op = [[0 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        # CHANGE THE NEXT LINE ACCORDING TO YOUR OPERATION
        value = x # example
        op[x][y] = value % n

R1 = [[0 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        # CHANGE THE NEXT LINE ACCORDING TO YOUR OPERATION
        value = 2 * y * y # example
        R1[x][y] = value % n

R2 = [[0 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        # CHANGE THE NEXT LINE ACCORDING TO YOUR OPERATION
        value =  2 * x * x # example
        R2[x][y] = value % n

R3 = [[0 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        # CHANGE THE NEXT LINE ACCORDING TO YOUR OPERATION
        value = 2 * x + 2 * x * x # example
        R3[x][y] = value % n

R4 = [[0 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        # CHANGE THE NEXT LINE ACCORDING TO YOUR OPERATION
        value = 2 * y + 2 * y * y
        R4[x][y] = value % n

print(op)
print(R1)
print(R2)
print(R3)
print(R4)

stq = Stuquandle()
stq.assign_operations([op, R1, R2, R3, R4])
print(stq.is_stuquandle())