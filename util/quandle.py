def inverse(op, x, y):
        """ what's (x *^-1 y)"""
        for z in range(len(op)):
            if op[z][y] == x:
                return z

""" checks quandle axioms """
def is_quandle(table):
    for i in range(len(table)): # axiom 1
        if table[i][i] != i:
            print("failed axiom 1 (not quandle)")
            return False 
        
    for i in range(len(table)): # axiom 2
        for j in range(len(table)):
            xpy = table[i][j]
            if table[xpy][j] != i:
                print("failed axiom 2 (not quandle)")
                return False
############## check for uniqueness in axiom 2 TO-DO######################
            
    for x in range(len(table)): # axiom 3
        for y in range(len(table)):
            for z in range(len(table)):
                left = table[table[x][y]][z]
                right = table[table[x][z]][table[y][z]]
                if left != right:
                    return False 
    return True

""" checks oriented singquandle axioms 
definition 5.2 """
def is_sinquandle(op, R1, R2):
    n = len(op)
    for x in range(n): # axiom 4, 5 from def 5.2
        for y in range(n):
            if (R2[x][y] != R1[y][op[x][y]] or  # axiom 4
                op[R1[x][y]][R2[x][y]] != R2[y][op[x][y]]): # axiom 5
                return False

    for x in range(n): 
        for y in range(n):
            for z in range(n): 
                if (op[R1[inverse(op, x, y)][z]][y] != R1[x][op[z][y]] or # axiom 1
                    R2[inverse(op, x, y)][z] != inverse(op, R2[x][op[z][y]], y) or # axiom 2
                    op[inverse(op, y, R1[x][z])][x] != inverse(op, op[y][R2[x][z]], z)): # axiom 3
                    return False
    return True 

# now check axioms 6, 7, 8, 9, 10 from def 6.1
def is_stuquandle(op, R3, R4):
    n = len(op)
    print("Check for stuquandle")
    for x in range(n):
        for y in range(n):
            print("Axiom 6", op[R3[y][x]][R4[y][x]] == R4[op[x][y]][y], "values", x, y)
            if (op[R3[y][x]][R4[y][x]] != R4[op[x][y]][y] or # axiom 6 def 6.1
                R4[y][x] != R3[op[x][y]][y]): # axiom 7 
                print("Failed either axiom 6 or 7")
                return False 
    
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if (R3[op[y][x]][z] != op[R3[y][inverse(op, z, x)]][x] or # axiom 8
                    R4[y][inverse(op, z, x)] != inverse(op, R4[op[y][x]][z], x) or # axiom 9
                    inverse(op, op[x][R4[y][z]], y) != op[inverse(op, x, R3[y][z])][z]): # axiom 10
                    print("Failed either axiom 8, 9, or 10")
                    return False
    return True 
  
class Stuquandle:
    def __init__(self):
        self.operations = [[] for _ in range(5)] # 5 operations *, R1, R2, R3, R4

    def assign_operations(self, tables, start_with_one = False):
        self.operations = tables 
        if start_with_one:
            for i in range(len(tables)):
                self.operations[i] = [[x - 1 for x in row] for row in self.operations[i]]

    def is_stuquandle(self):
        return (is_quandle(self.operations[0]) and
                is_sinquandle(self.operations[0], self.operations[1], self.operations[2]) and
                is_stuquandle(self.operations[0], self.operations[3], self.operations[4]))

        

