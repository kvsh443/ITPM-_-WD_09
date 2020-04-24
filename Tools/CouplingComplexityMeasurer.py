import re


class CouplingComplexityMeasurer:
    W_RM_TO_RM_INSIDE = 2
    W_RM_TO_RM_OUTSIDE = 3
    W_RM_TO_RCM_INSIDE = 3
    W_RM_TO_RCM_OUTSIDE = 4
    W_RCM_TO_RM_INSIDE = 3
    W_RCM_TO_RM_OUTSIDE = 4
    W_RCM_RCM_INSIDE = 4
    W_RCM_TO_RCM_OUTSIDE = 5
    W_RM_TO_GLOBAL_INSIDE = 1
    W_RCM_TO_GLOBAL_INSIDE = 1
    W_RM_TO_GLOBAL_OUTSIDE = 2
    W_RCM_TO_GLOBAL_OUTSIDE = 2

    code = ""
    declared_method_lines = []
    declared_method_names = []

    regular_method_calls_lines = []
    recursive_method_calls_lines = []

    regular_method_calls_names = []
    recursive_method_calls_names = []

    rm_to_rm_inside = []
    rm_to_rm_outside = []
    rm_to_rcm_inside = []
    rm_to_rcm_outside = []
    rcm_to_rm_inside = []
    rcm_to_rm_outside = []
    rcm_rcm_inside = []
    rcm_to_rcm_outside = []
    rm_to_global_inside = []
    rcm_to_global_inside = []
    rm_to_global_outside = []
    rcm_to_global_outside = []
    total = []

    method_lines = []
    class_lines = []
    control_structure_lines = []

    not_possible_lines = []
    method_tracker = []

    def __init__(self, code):
        self.clear_all()
        self.code = code
        self.remove_comments()
        self.run()

    def method_calls(self):

        types = ["boolean", "byte", "char", "double", "float", "int", "long", "short", "string", "void",
                 "String", "return", "int", "public"
                                            "ArrayList", "List", "HashMap", "return"]
        loops = ["for", "while", "class", "do", "foreach"]
        control_structures = ["if", "switch", "else", "case", "IOException"]

        type_list = []
        type_list.extend(types)
        type_list.extend(loops)
        type_list.extend(control_structures)

        global_variables = []
        method_variable_list = []

        main_index = 0

        for line in self.code.split("\n"):
            if line not in self.method_lines:
                variable_list = re.findall(r'[ ]{0,20}[A-z]{1,20}[ =;]', line)
                for var in variable_list:
                    variable = var.strip()
                    if variable not in type_list:
                        global_variables.append(variable.strip())

        for line in self.code.split("\n"):
            new_list = []
            if line in self.method_lines:
                if line not in self.declared_method_lines:
                    variable_list_1 = re.findall(r' [A-z]{1,20} ', line)
                    variable_list_2 = re.findall('[(][A-z]{1,20}[)]', line)
                    for variable in variable_list_1:
                        var = variable.strip()
                        if var not in type_list:
                            new_list.append(var)
                    for variable in variable_list_2:
                        var = re.findall('[A-z]{1,20}', variable)
                        for v in var:
                            if var not in type_list:
                                new_list.append(v.strip())

            method_variable_list.append(new_list)

        for line in self.code.split("\n"):
            rm_to_rm_inside = 0
            rm_to_rm_outside = 0
            rm_to_rcm_inside = 0
            rm_to_rcm_outside = 0
            rcm_to_rm_inside = 0
            rcm_to_rm_outside = 0
            rcm_rcm_inside = 0
            rcm_to_rcm_outside = 0
            rm_to_global_inside = 0
            rcm_to_global_inside = 0
            rm_to_global_outside = 0
            rcm_to_global_outside = 0

            if line not in self.not_possible_lines:
                # regular method parent
                if line in self.regular_method_calls_lines:
                    # regular methods calls
                    index = self.regular_method_calls_lines.index(line)
                    name = self.regular_method_calls_names[index]
                    # methods
                    if name not in self.recursive_method_calls_names:
                        if name in self.declared_method_names:
                            rm_to_rm_inside += 1
                        else:
                            rm_to_rm_outside += 1
                    # recursive method call
                    else:
                        if name in self.declared_method_names:
                            rm_to_rcm_inside += 1
                        else:
                            rm_to_rcm_outside += 1

                    for name in method_variable_list[main_index]:
                        if name in global_variables:
                            rm_to_global_inside += 1
                            break
                        else:
                            rm_to_global_outside += 1
                            break

                # rcm parent
                if line in self.recursive_method_calls_lines:
                    index = self.recursive_method_calls_lines.index(line)
                    name = self.recursive_method_calls_names[index]
                    # regular methods calls
                    if name not in self.recursive_method_calls_names:
                        if name in self.declared_method_names:
                            rcm_to_rm_inside += 1
                        else:
                            rcm_to_rm_outside += 1
                    # recursive method call
                    else:
                        if name in self.declared_method_names:
                            rcm_rcm_inside += 1
                        else:
                            rcm_to_rcm_outside += 1

                    for name in method_variable_list[main_index]:
                        if name in global_variables:
                            rcm_to_global_inside += 1
                            break
                        else:
                            rcm_to_global_outside += 1
                            break

            self.rm_to_rm_inside.append(rm_to_rm_inside)
            self.rm_to_rm_outside.append(rm_to_rm_outside)
            self.rm_to_rcm_inside.append(rm_to_rcm_inside)
            self.rm_to_rcm_outside.append(rm_to_rcm_outside)
            self.rcm_to_rm_inside.append(rcm_to_rm_inside)
            self.rcm_to_rm_outside.append(rcm_to_rm_outside)
            self.rcm_rcm_inside.append(rcm_rcm_inside)
            self.rcm_to_rcm_outside.append(rcm_to_rcm_outside)

            self.rm_to_global_inside.append(rm_to_global_inside)
            self.rm_to_global_outside.append(rm_to_global_outside)
            self.rcm_to_global_inside.append(rcm_to_global_inside)
            self.rcm_to_global_outside.append(rcm_to_global_outside)
            main_index += 1

    def clear_all(self):
        self.code = ""

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
        self.find_method_lines()
        self.find_line_types()
        self.find_method_line_types()
        self.method_calls()
        self.calculate_total()

    def find_method_lines(self):
        method_call_lines = []
        types = ["void", "boolean", "byte", "char", "double", "float", "int", "long", "short", "string",
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
                                self.declared_method_lines.append(r)
                        else:
                            if f not in loops and f not in control_structures:
                                if r not in method_call_lines:
                                    method_call_lines.append(r)

        for line in method_call_lines:
            if line in self.declared_method_lines:
                method_call_lines.remove(line)

        for declared in self.declared_method_lines:
            start = None
            for t in types:
                s = re.search(t, declared)
                if s:
                    start = s.span()[1]
                    break
            end = re.search("\\(", declared).span()[0]
            if start:
                name = str(declared[start:end]).strip()
                if name not in self.declared_method_names:
                    self.declared_method_names.append(name)

        for call in method_call_lines:
            new_word = call.strip()
            end = re.search('\\(', new_word)
            if end:
                for f in new_word.split(' '):
                    start = 0
                    self.regular_method_calls_lines.append(call)

                    if 'return' in f:
                        # self.recursive_method_calls_lines.append(call)
                        s = re.search('return', new_word)
                        if s:
                            start = s.span()[1]
                            # self.recursive_method_calls_names.append(new_word[start:end.span()[0]].strip())

                            # regular methods
                            self.regular_method_calls_names.append(new_word[start:end.span()[0]].strip())
                            break
                    else:
                        # regular methods
                        self.regular_method_calls_names.append(new_word[start:end.span()[0]].strip())

    # def method_type_tracker(self):
    #     method_types = []
    #     lines = self.code.split('\n')
    #     start = 0
    #     while start < len(self.method_tracker):
    #         method_type = False
    #         if self.method_tracker[start] == 1:
    #             count = 1
    #             next_start = start + 1
    #             while self.method_tracker[next_start] == 1:
    #                 for li in self.recursive_method_calls_lines:
    #                     if li in lines[next_start]:
    #                         method_type = True
    #                     count += 1
    #                     next_start += 1
    #             for a in range(count):
    #                 method_types.append(method_type)
    #         else:
    #             method_types.append(method_type)
    #         start += 1
    #     print(method_types)

    def find_method_line_types(self):
        inside_method = False
        last_saved_method = ""
        print(self.declared_method_lines)
        print(self.declared_method_names)
        for line in self.code.split("\n"):
            if line in self.method_lines:
                if line in self.declared_method_lines:
                    last_saved_method = self.declared_method_names[self.declared_method_lines.index(line)]
                    inside_method = True
                if inside_method and line not in self.declared_method_lines:
                    s = re.search('return', line)
                    end = re.search('\\(', line)
                    if s and end:
                        start = s.span()[1]
                        name = line[start:end.span()[0]].strip()
                        if last_saved_method == name:
                            self.recursive_method_calls_lines.append(line)
                            self.recursive_method_calls_names.append(name)

            else:
                inside_method = False

        for line in self.regular_method_calls_lines:
            if line in self.recursive_method_calls_lines:
                index = self.regular_method_calls_lines.index(line)
                self.regular_method_calls_lines.remove(line)
                self.regular_method_calls_names.remove(self.regular_method_calls_names[index])

    def find_line_types(self):
        # cs - class stack, ms - method stack, css - control structure stack (including loops)
        cs = []
        ms = []
        css = []

        types = ["boolean", "byte", "char", "double", "float", "int", "long", "short", "string", "void",
                 "String",
                 "ArrayList", "List", "HashMap"]
        loops = ["for", "while", "class", "do", "foreach"]
        control_structures = ["if", "switch", "else", "case", "IOException"]

        for r in self.code.split('\n'):
            bo = 0
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
                                bo = 1
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
                    if len(ms) == 0:
                        bo = 1
                if len(css) > 0:
                    css.pop()

            if len(cs) > 0:
                self.class_lines.append(r)
            if len(ms) > 0:
                self.method_lines.append(r)
            if len(css) > 0:
                self.control_structure_lines.append(r)

            self.method_tracker.append(bo)

    def calculate_total(self):
        lines = self.code.split("\n")
        for i in range(0, len(lines)):
            total = self.rm_to_rm_inside[i] * self.W_RM_TO_RM_INSIDE + \
                    self.rm_to_rm_outside[i] * self.W_RM_TO_RM_OUTSIDE + \
                    self.rm_to_rcm_inside[i] * self.W_RM_TO_RCM_INSIDE + \
                    self.rm_to_rcm_outside[i] * self.W_RM_TO_RCM_OUTSIDE + \
                    self.rcm_to_rm_inside[i] * self.W_RCM_TO_RM_INSIDE + \
                    self.rcm_to_rm_outside[i] * self.W_RCM_TO_RM_OUTSIDE + \
                    self.rcm_rcm_inside[i] * self.W_RCM_RCM_INSIDE + \
                    self.rcm_to_rcm_outside[i] * self.W_RCM_TO_RCM_OUTSIDE + \
                    self.rm_to_global_inside[i] * self.W_RM_TO_GLOBAL_INSIDE + \
                    self.rcm_to_global_inside[i] * self.W_RCM_TO_GLOBAL_INSIDE + \
                    self.rm_to_global_outside[i] * self.W_RM_TO_GLOBAL_OUTSIDE + \
                    self.rcm_to_global_outside[i] * self.W_RCM_TO_GLOBAL_OUTSIDE

            self.total.append(total)
