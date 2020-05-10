import re


class InheritanceComplexityMeasurer:
    code = ""

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
                ci = self.class_info[class_name]
                dir_inh = len(ci[0])
                indir_inh = len(ci[1])

                self.ndi.append(dir_inh)
                self.nidi.append(indir_inh)

                tivalue = dir_inh + indir_inh

                self.ti.append(tivalue)
                if tivalue >= 3:
                    self.final_result.append(4)
                else:
                    self.final_result.append(tivalue)

            else:
                self.final_result.append(0)
                self.ndi.append(0)
                self.nidi.append(0)
                self.ti.append(0)
