import re
from weightTable import WeightTable as wt


class MethodComplexityMeasurer:
    code = ""
    # W_PRIMITIVE = 1
    # W_COMPOSITE = 2
    # W_VOID = 0
    # M_W_PRIMITIVE_R = 1
    # M_W_COMPOSITE_R = 2
    w = wt()

    W_PRIMITIVE = w.get_method()[0]
    W_COMPOSITE = w.get_method()[1]
    W_VOID = w.get_method()[2]
    M_W_PRIMITIVE_R = w.get_method()[3]
    M_W_COMPOSITE_R = w.get_method()[4]

    w_return_types = []
    n_primitive_params = []
    n_composite_params = []
    complexity = []

    method_lines = []

    def __init__(self, code):
        self.clear_all()
        self.code = code
        self.remove_comments()
        self.run()

    def clear_all(self):
        self.code = ""
        self.w_return_types.clear()
        self.n_primitive_params.clear()
        self.n_composite_params.clear()
        self.complexity.clear()
        self.method_lines.clear()

    def remove_comments(self):
        count = re.findall("/*", self.code)

        for i in count:
            # Remove multi line comments
            start = re.search("/\\*", self.code)
            end = re.search('\\*/', self.code)

            if start:
                a = self.code[0:start.span()[0]]
                b = self.code[end.span()[1]: len(self.code)]
                self.code = a + b

        # Remove Single line comments
        s = ""
        for i in self.code.split('\n'):
            start = re.search("//", i)
            if start:
                if i.strip():
                    if i[0: start.span()[0]].strip():
                        s += i[0: start.span()[0]]
                        s += "\n"
            else:
                if i.strip():
                    s += i
                    s += "\n"
        if s.strip():
            self.code = s

    def get_weight_return_type(self):
        return self.w_return_types

    def get_number_of_primitive_params(self):
        return self.n_primitive_params

    def get_number_of_composite_params(self):
        return self.n_composite_params

    def get_method_complexity(self):
        return self.complexity

    def run(self):
        self.find_method_lines()
        types = ["boolean", "byte", "char", "double", "float", "int", "long", "short", "string"]
        loops = ["for", "if", "while", "switch", "class", "do", "foreach"]

        for r in self.code.split('\n'):
            prim = 0
            comp = 0
            p_prim = 0
            p_comp = 0

            frag = r.split(' ')

            # Identify method declaration line
            if r in self.method_lines:
                sub_end = re.search("\\(", r).span()[0]
                next_end = re.search("\\)", r).span()[0]

                # get composite return type
                n_frag = r[0:sub_end].split(' ')
                comp_type = None
                for f in n_frag:
                    comp_type = re.findall("^[A-Z].*", f)
                    if comp_type:
                        break

                # Identify Return type
                if comp_type:
                    comp += 1
                elif re.findall("void", r):
                    pass
                else:
                    for f in frag:
                        if f in types:
                            prim += 1
                            break

                # Parameters
                n_frag = r[sub_end + 1:next_end].split(' ')

                for f in n_frag:
                    comp_type = re.findall("^[A-Z].*", f)
                    if comp_type:
                        p_comp += 1
                    elif re.findall("void", f):
                        pass
                    else:
                        if f in types:
                            p_prim += 1

            r_complexity = (prim * self.W_PRIMITIVE) + (comp * self.W_COMPOSITE)
            self.w_return_types.append(r_complexity)
            self.n_primitive_params.append(p_prim)
            self.n_composite_params.append(p_comp)
            self.complexity.append(r_complexity + (p_prim * self.W_PRIMITIVE) + (p_comp * self.W_COMPOSITE))

    def find_method_lines(self):
        types = ["boolean", "byte", "char", "double", "float", "int", "long", "short", "string", "void",
                 "String",
                 "ArrayList", "List", "HashMap"]
        loops = ["for", "while", "class", "do", "foreach"]
        control_structures = ["if", "switch", "else", "case", "IOException"]

        for r in self.code.split('\n'):
            frag = r.split(' ')
            if 'class' in frag:
                pass
            else:
                # can be method, loop or control structure
                if '(' in r and ')' in r and not re.findall("[.]", r) and "new" not in r:
                    for f in frag:
                        # Method
                        if f in types or re.findall("^[A-Z].*", f):
                            if f not in loops and f not in control_structures:
                                self.method_lines.append(r)
