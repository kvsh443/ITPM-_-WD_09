import re
from weightTable import WeightTable as wt


class InheritanceComplexityMeasurer:
    code = ""
    w = wt()
    # C_W_0_INHERITANCE = 0
    # C_W_1_INHERITANCE = 1
    # C_W_2_INHERITANCE = 2
    # C_W_3_INHERITANCE = 3
    # C_W_MORE_INHERITANCE = 4

    C_W_0_INHERITANCE = w.get_inheritance()[0]
    C_W_1_INHERITANCE = w.get_inheritance()[1]
    C_W_2_INHERITANCE = w.get_inheritance()[2]
    C_W_3_INHERITANCE = w.get_inheritance()[3]
    C_W_MORE_INHERITANCE = w.get_inheritance()[4]

    final_result = []
    ndi = []
    nidi = []
    ti = []
    cname = ""
    CLASS_NAMES = []
    LINES_WITH_INHERITANCE = []
    class_name = " "
    class_info = {}
    directly_inherited = []
    indirectly_inherited = []

    def __init__(self, code):
        self.clear_all()
        self.code = code
        self.remove_comments()
        self.run()

    def clear_all(self):
        self.code = ""
        self.final_result.clear()
        self.ndi.clear()
        self.nidi.clear()
        self.ti.clear()

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

    def get_complexity(self):
        return self.final_result

    def get_ndi(self):
        return self.ndi

    def get_nidi(self):
        return self.nidi

    def get_ti(self):
        return self.ti

    def run(self):
        # class inheritance details

        self.LINES_WITH_INHERITANCE = re.findall("class \\w+ extends \\w+", self.code)

        for line in (re.findall("class \\w+", self.code)):
            self.CLASS_NAMES.append(line.split(" ")[1].strip())

        for class_name in self.CLASS_NAMES:
            # lists to store direct / indirect classes
            directly_inherited = []
            indirectly_inherited = []

            # Go through children using the recursion
            def find_children(cname):
                for line in self.LINES_WITH_INHERITANCE:
                    if "extends " + cname in line:
                        child_name = line.split(" ")[1]

                        if cname == class_name:
                            directly_inherited.append(child_name)
                            find_children(child_name)
                        else:
                            indirectly_inherited.append(child_name)
                            find_children(child_name)

            find_children(class_name)
            self.class_info[class_name] = [directly_inherited, indirectly_inherited]

        # starting to read a heavily code file line by line
        for r in self.code.split('\n'):
            frag = r.split(' ')

            if 'class' in frag:
                class_name = ""
                results = re.findall("class \\w+", r)
                class_name = results[0].split(" ")[1].strip()
                if class_name == "":
                    continue
                dir_inh = 0
                indir_inh = 0

                for key, value in self.class_info.items():
                    if class_name in value[0]:
                        dir_inh += 1
                    if class_name in value[1]:
                        indir_inh += 1

                self.ndi.append(dir_inh)
                self.nidi.append(indir_inh)

                tivalue = dir_inh + indir_inh

                self.ti.append(tivalue)
                if tivalue == self.C_W_0_INHERITANCE:
                    self.final_result.append(self.C_W_0_INHERITANCE)
                elif tivalue == self.C_W_1_INHERITANCE:
                    self.final_result.append(self.C_W_1_INHERITANCE)
                elif tivalue == self.C_W_2_INHERITANCE:
                    self.final_result.append(self.C_W_2_INHERITANCE)
                elif tivalue == self.C_W_3_INHERITANCE:
                    self.final_result.append(self.C_W_3_INHERITANCE)
                elif tivalue >= self.C_W_MORE_INHERITANCE:
                    self.final_result.append(self.C_W_MORE_INHERITANCE)
                else:
                    self.final_result.append(0)

            else:
                self.final_result.append(0)
                self.ndi.append(0)
                self.nidi.append(0)
                self.ti.append(0)
