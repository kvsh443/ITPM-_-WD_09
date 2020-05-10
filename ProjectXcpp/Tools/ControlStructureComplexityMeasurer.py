import re
from weightTable import WeightTable as wt


class ControlStructureComplexityMeasurer:
    code = ""
    # W_IF = 2
    # W_FOR_WHILE = 3
    # W_SWITCH = 2
    # W_CASE = 1

    w = wt()
    W_IF = w.get_control_structures()[0]
    W_FOR_WHILE = w.get_control_structures()[1]
    W_SWITCH = w.get_control_structures()[2]
    W_CASE = w.get_control_structures()[3]

    w_type = []
    w_nest = []
    n_conditions = []

    method_lines = []
    class_lines = []
    control_structure_lines = []
    loop_count = []

    not_possible_lines = []

    def __init__(self, code):
        self.clear_all()
        self.code = code
        self.remove_comments()
        self.run()

    def clear_all(self):
        self.w_type.clear()
        self.w_nest.clear()
        self.n_conditions.clear()
        self.method_lines.clear()
        self.class_lines.clear()
        self.control_structure_lines.clear()
        self.loop_count.clear()
        self.not_possible_lines.clear()

    def get_weight_due_to_type(self):
        return self.w_type

    def get_weight_due_to_nest(self):
        return self.w_nest

    def get_number_of_conditions(self):
        return self.n_conditions

    def get_control_structure_complexity(self):
        result = []
        for t, c, n in zip(self.w_type, self.n_conditions, self.w_nest):
            if c == 0:
                c = 1
            total = (t * c) + n
            result.append(total)
        return result

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

    def run(self):
        self.find_line_types()
        saved_ccs = 0
        for r, n_loops in zip(self.code.split('\n'), self.loop_count):
            w = 0
            w_in = 0
            conditions = 0

            if r in self.control_structure_lines and r not in self.not_possible_lines:

                if "if" in r or "else" in r:
                    conditions += 1
                    weight = self.W_IF
                    if "&&" in r or "||" in r:
                        n = ((len(re.findall("[|&]", r))) / 2)
                        conditions += n

                    if n_loops > 1:
                        w_in += (weight * (n_loops - 1))

                    w += weight

                if "for" in r or "while" in r or "do" in r:
                    conditions += 1
                    if n_loops > 1:
                        w_in += (self.W_FOR_WHILE * (n_loops - 1))

                    w += self.W_FOR_WHILE

                if "switch" in r:
                    conditions += 1
                    if n_loops > 1:
                        w_in += (self.W_SWITCH * (n_loops - 1))

                    w += self.W_SWITCH

                if "case" in r:
                    conditions += 1
                    if n_loops > 1:
                        w_in += (self.W_CASE * (n_loops - 1))

                    w += self.W_CASE

            total = (w * conditions) + saved_ccs
            self.w_type.append(w)
            self.w_nest.append(w_in)
            self.n_conditions.append(conditions)
            print(total)
            saved_ccs = total

    def find_line_types(self):
        # cs - class stack, ms - method stack, css - control structure stack (including loops)
        cs = []
        ms = []
        css = []

        types = ["bool", "byte", "char", "double", "float", "int", "long", "short", "string", "void"]
        loops = ["for", "while", "class", "do", "foreach"]
        control_structures = ["if", "while", "do-while", "for", "break", "continue", "goto", "exit"]

        for r in self.code.split('\n'):
            frag = r.split(' ')
            if 'class' in frag:
                cs.append(1)
                self.not_possible_lines.append(r)
            else:
                # can be method, loop or control structure
                if '(' in r and ')' in r and "new" not in r:
                    for f in frag:
                        fl = f.strip()
                        # Method
                        if f in types or re.findall("^[A-Z].*", f) and not re.findall("[.]", r):
                            if f not in loops and f not in control_structures:
                                cs.append(1)
                                ms.append(1)
                                self.not_possible_lines.append(r)
                        # Loops
                        elif fl in loops or fl in control_structures:
                            cs.append(1)
                            ms.append(1)
                            css.append(1)
                        else:
                            print(fl)

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

            count = 0
            if len(css) > 0:
                self.control_structure_lines.append(r)
                for i in css:
                    count += i

            self.loop_count.append(count)
        print(self.control_structure_lines)
