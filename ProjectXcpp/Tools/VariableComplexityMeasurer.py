import re
from weightTable import WeightTable as wt


class VariableComplexityMeasurer:


    # W_GLOBAL_SCOPE = 2
    # W_LOCAL_SCOPE = 1
    # W_PRIMITIVE = 1
    # W_COMPOSITE = 2

    w = wt()
    W_GLOBAL_SCOPE = w.get_variable()[0]
    W_LOCAL_SCOPE = w.get_variable()[1]
    W_PRIMITIVE = w.get_variable()[2]
    W_COMPOSITE = w.get_variable()[3]

    code = ""
    lines = []
    final_complexity = []
    n_primitive = []
    n_composite = []

    inside_lines = []

    method_lines = []
    class_lines = []
    control_structure_lines = []

    not_possible_lines = []

    def __init__(self, code):
        self.clear_all()
        self.code = code
        self.remove_comments()
        self.run()

    def clear_all(self):
        self.code = ""
        self.lines.clear()
        self.final_complexity.clear()
        self.n_primitive.clear()
        self.n_composite.clear()
        self.inside_lines.clear()
        self.method_lines.clear()
        self.class_lines.clear()
        self.control_structure_lines.clear()
        self.not_possible_lines.clear()

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

    def get_variable_scope_weight(self):
        return self.lines

    def get_variable_complexity(self):
        return self.final_complexity

    def get_number_of_primitive_data(self):
        return self.n_primitive

    def get_number_of_composite_data(self):
        return self.n_composite

    def run(self):
        self.find_line_types()
        result = []
        lines = []
        p_types = ["bool", "byte", "char", "double", "float", "int", "long", "short", "string"]
        c_structures = ["class", "if", "else", "switch", "for", "while", "class", "do",
                        "foreach", "switch", "case", "do-while","break", "continue", "goto", "exit"]

        for r in self.code.split('\n'):
            frag = r.strip().split(' ')

            if r in self.method_lines:
                lines.append(self.W_LOCAL_SCOPE)
            elif r in self.class_lines:
                lines.append(self.W_GLOBAL_SCOPE)
            else:
                lines.append(0)

            p_total = 0
            # Primitive
            p = 0
            for t in p_types:
                # in primitive data types
                if t in frag:
                    if r not in self.not_possible_lines and r not in self.control_structure_lines:
                        if r in self.method_lines:
                            # Local
                            p_total += (self.W_LOCAL_SCOPE * self.W_PRIMITIVE)
                            p += 1
                        elif r in self.class_lines:
                            # Global
                            p_total += (self.W_GLOBAL_SCOPE * self.W_PRIMITIVE)
                            p += 1

            if "," in r:
                p *= 2
                p_total *= 2
            self.n_primitive.append(p)

            # Composite
            c = 0
            c_total = 0
            for f in frag:
                # f = f.strip()
                if re.findall("^[A-Z].*", f) \
                        and (not re.findall("[.]", r) or ".getInstance()" in r) \
                        and f not in c_structures \
                        and r not in self.not_possible_lines \
                        and r not in self.control_structure_lines:
                    # Local
                    if r in self.method_lines:
                        c_total += (self.W_LOCAL_SCOPE * self.W_COMPOSITE)
                        c += 1
                    # Global
                    elif r in self.class_lines:
                        c_total += (self.W_GLOBAL_SCOPE * self.W_COMPOSITE)
                        c += 1
            total = 0

            if '"' in r:
                c = 0

            if " new " in r or "getInstance()" in r:
                self.n_composite.append(int(c / 2))
                total = p_total + (c_total / 2)
            else:
                self.n_composite.append(c)
                total = p_total + c_total
            if '"' in r:
                total = 0
            result.append(total)

        self.final_complexity = result
        self.lines = lines

    def find_line_types(self):
        # cs - class stack, ms - method stack, css - control structure stack (including loops)
        cs = []
        ms = []
        css = []

        types = ["bool", "byte", "char", "double", "float", "int", "long", "short", "string", "void"]
        loops = ["for", "while", "class", "do", "for"]
        control_structures = ["if", "while", "do-while", "for", "break", "continue", "goto", "exit"]

        for r in self.code.split('\n'):
            frag = r.split(' ')
            if 'class' in frag:
                cs.append(1)
                self.not_possible_lines.append(r)
            else:
                # can be method, loop or control structure
                if '(' in r and ')' in r and not re.findall("[.]", r) and "new" not in r:
                    for f in frag:
                        # Method
                        if f in types or re.findall("^[A-Z].*", f):
                            if f not in loops and f not in control_structures:
                                cs.append(1)
                                ms.append(1)
                                self.not_possible_lines.append(r)
                        # Loops
                        elif f in loops or f in control_structures:
                            cs.append(1)
                            ms.append(1)
                            css.append(1)
                            self.not_possible_lines.append(r)

            # Remove { from stacks
            if '}' in r:
                if len(cs) > 0:
                    cs.pop()
                if len(ms) > 0:
                    ms.pop()
                if len(css) > 0:
                    css.pop()

            if len(cs) > 0:
                self.class_lines.append(r)
            if len(ms) > 0:
                self.method_lines.append(r)
            if len(css) > 0:
                self.control_structure_lines.append(r)
