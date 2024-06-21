class QuandlePolynomial:
    def __init__(self):
        self.rs = [] # row counts
        self.cs = [] # column counts

    """ 
    Table must be filled with values 0 to (n-1)
    If not, set start_with_one = True
    """
    def form_quandle_poly(self, table, start_with_one = False): 
        if start_with_one:
            table = [[x - 1 for x in row] for row in table]

        self.rs = [0 for _ in range(len(table))]
        self.cs = [0 for _ in range(len(table))]

        # compute rs
        for i in range(len(table)): # 0 to n-1
            ri = 0
            for j in range(len(table)):
                if table[i][j] == i:
                    ri += 1
            self.rs[i] = ri 
        
        # compute cs
        for i in range(len(table)):
            ci = 0
            for j in range(len(table)):
                if table[j][i] == j:
                    ci += 1
            self.cs[i] = ci 
    
    def print(self):
        terms = {}
        for i in range(len(self.rs)):
            if (self.rs[i], self.cs[i]) in terms:
                terms[(self.rs[i], self.cs[i])] += 1
            else:
                terms[(self.rs[i], self.cs[i])] = 1

        output = []
        for (r, c), count in terms.items():
            if r == 0:
                s_part = ""
            elif r == 1:
                s_part = "s"
            else:
                s_part = f"s^{r}"

            if c == 0:
                t_part = ""
            elif c == 1:
                t_part = "t"
            else:
                t_part = f"t^{c}"

            if count == 1:
                term_parts = [part for part in [s_part, t_part] if part]
            else:
                term_parts = [str(count)] + [part for part in [s_part, t_part] if part]

            term_string = " * ".join(term_parts) + " + "
            output.append(term_string)
        
        final_output = ""
        if output:
            final_output = "".join(output)[:-3]
        else:
            final_output = ""
        print(final_output)

class StuquandlePolynomial:
    # Now we have 5 different tables, which makes 5 different pairs of lists
    def __init__(self):
        n = 0
        self.operations = [([], []), ([], []), ([], []), ([], []), ([], [])] # tables 2 - 5
    
    # her assumed that indexing from 0
    def compute_table(self, table):
        # compute rs
        rs = [0 for _ in range(len(table))]
        cs = [0 for _ in range(len(table))]

        for i in range(len(table)): # 0 to n-1
            ri = 0
            for j in range(len(table)):
                if table[i][j] == i:
                    ri += 1
            rs[i] = ri 
        
        # compute cs
        for i in range(len(table)):
            ci = 0
            for j in range(len(table)):
                if table[j][i] == j:
                    ci += 1
            cs[i] = ci 
        
        return (rs, cs)

    def form_stuquandle_poly_list(self, operations, start_with_one = False):
        self.n = len(operations[0])
        if start_with_one:
            for i in range(5):
                operations[i] = [[x - 1 for x in row] for row in operations[i]]
        
        for i in range(5):
            self.operations[i] = (self.compute_table(operations[i])[0], self.compute_table(operations[i])[1])
    
    def print_stuquandle(self):
        terms = {}
        o = self.operations

        for i in range(self.n):
            term = (o[0][0][i], o[0][1][i],
                    o[1][0][i], o[1][1][i],
                    o[2][0][i], o[2][1][i],
                    o[3][0][i], o[3][1][i],
                    o[4][0][i], o[4][1][i])
            if term in terms:
                terms[term] += 1
            else:
                terms[term] = 1
        
        print("terms count of 10-tuples:", terms)

        output = []
        variable_names = [f's{i//2+1}' if i % 2 == 0 else f't{i//2+1}' for i in range(10)]

        for exponents, count in terms.items():
            term_parts = []
            if count != 1:
                term_parts.append(str(count))
            
            for var_name, exp in zip(variable_names, exponents):
                if exp == 0:
                    continue
                elif exp == 1:
                    term_parts.append(var_name)
                else:
                    term_parts.append(f'{var_name}^{exp}')
            
            term_string = ' * '.join(term_parts)
            output.append(term_string)
        
        final_output = ' + '.join(output)
        print(final_output)

    
    def print_substuquandle(self, image, operations):
        """Image is a list of elements [0, 1]"""
        terms = {}
        o = self.operations
        q, R1, R2, R3, R4 = operations
        
        # print("Image:", image)
        # need to close the image
        for x in range(self.n):
            for y in range(self.n):
                if (x in image and y in image):
                    if q[x][y] not in image:
                        image.append(q[x][y])
                    if R1[x][y] not in image:
                        image.append(R1[x][y])
                    if R2[x][y] not in image:   
                        image.append(R2[x][y])
                    if R3[x][y] not in image:
                        image.append(R3[x][y])
                    if R4[x][y] not in image:
                        image.append(R4[x][y])
        # print("Updated image:", image)

        for i in range(self.n):
            if i in image:
                term = (o[0][0][i], o[0][1][i],
                        o[1][0][i], o[1][1][i],
                        o[2][0][i], o[2][1][i],
                        o[3][0][i], o[3][1][i],
                        o[4][0][i], o[4][1][i])
                if term in terms:
                    terms[term] += 1
                else:
                    terms[term] = 1
        
        # print("terms count of 10-tuples:", terms)

        output = []
        variable_names = [f's{i//2+1}' if i % 2 == 0 else f't{i//2+1}' for i in range(10)]

        for exponents, count in terms.items():
            term_parts = []
            if count != 1:
                term_parts.append(str(count))
            
            for var_name, exp in zip(variable_names, exponents):
                if exp == 0:
                    continue
                elif exp == 1:
                    term_parts.append(var_name)
                else:
                    term_parts.append(f'{var_name}^{exp}')
            
            term_string = ' * '.join(term_parts)
            output.append(term_string)
        
        final_output = ' + '.join(output)
        print(final_output)
