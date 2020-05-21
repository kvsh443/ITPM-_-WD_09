import re
from weightTable import WeightTable as wt


class SizeComplexityMeasurer(object):
    code = ''
    # W_KEYWORD = 1
    # W_IDENTIFIER = 1
    # W_OPERATOR = 1
    # W_NUMERICAL_VAL = 1
    # W_STRING_LIT = 1

    w = wt()
    W_KEYWORD = w.get_size()[0]
    W_IDENTIFIER = w.get_size()[1]
    W_OPERATOR = w.get_size()[2]
    W_NUMERICAL_VAL = w.get_size()[3]
    W_STRING_LIT = w.get_size()[4]

    def __init__(self, code):
        self.code = ''
        self.code = code
        self.remove_comments()

    def get_code_lines(self):
        code_lines = []
        for i in self.code.split('\n'):
            code_lines.append(i)
        return code_lines

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

    def get_operators(self):
        operators_list_old = ["+", "-", "*", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=", "&&",
                              "||", "!", "|", "^", "~", ",",
                              ".", "::", "+=", "-=", "*=", "/=", "=",
                              "|=", "&=", "%="]
        operators_list = ["+", "-", "*", "/", "%", "++", "--", "=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=",
                          ">>=",
                          "<=",
                          "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!"]
        operators = []
        y = []
        for i in self.code.split('\n'):
            # y = re.findall("[=<>+/!&|:%\-*~]{1,2}", i.strip())

            x = 0
            for w in i.split(' '):
                if w in operators_list:
                    y.append(w)
            if x == 0:
                n = len(re.findall("[=<>+/!&|:%\-*~]{1,2}", i.strip()))
                x += n
            x = len(y)
            y.clear()

            if "#include " in i:
                x = 0
            operators.append(x * self.W_OPERATOR)
        return operators

    # def get_operators(self):
    #     operators = []
    #     for i in self.code.split('\n'):
    #         y = re.findall("[=<>+/!&|:%\-*~.,]{1,2}", i.strip())
    #         x = len(y)
    #         if "include" in i:
    #             x = 0
    #         operators.append(x * self.W_OPERATOR)
    #     return operators

    def get_keywords(self):
        # keyword__list = ["abstract", "assert", "break", "catch", "class", "continue", "default", "enum", "exports",
        #                 "extends", "final", "finally", "implements",
        #                 "import", "instanceof", "module", "native", "new", "package", "private", "protected", "public",
        #                 "requires", "return", "static", "strictfp", "super", "synchronized", "this",
        #                 "throw", "throws", "transient", "try", "var", "void", "volatile", "true", "else", "null", "this"
        #                 ]
        keyword_list = ["asm", "auto", "catch", "class", "const", "const_cast", "default",
                        "delete",
                        "do",
                        "dynamic_cast", "else", "enum", "explict", "export", "extern", "false", "for", "friend",
                        "inline",
                        "return", "signed", "sizeof", "static", "static_cast", "struct", "template", "this",
                        "throw", "true",
                        "try", "typedef", "typeid", "typename", "union", "unsigned", "using", "virtual", "void",
                        "volatile",
                        "wchar_t"]
        keyword = []
        for i in self.code.split('\n'):
            count = 0
            for word in i.split(' '):
                w = word.strip()
                if w in keyword_list:
                    count += 1
            if "#include " in i:
                count = 0
            keyword.append(count * self.W_KEYWORD)

        return keyword

    def get_numerical_values(self):
        num_values = []
        for i in self.code.split('\n'):
            x = len(re.findall('[0-9]+', i))
            num_values.append(x * self.W_NUMERICAL_VAL)
        return num_values

    def get_string_literals(self):
        string_literals = []
        for i in self.code.split('\n'):
            count = 0
            x = len(re.findall('"', i))
            if x % 2 == 0:
                x = x / 2
                count = int(x) * self.W_STRING_LIT
            string_literals.append(count)
        return string_literals

    def get_identifiers(self):
        identifier_list = ["bool", "byte", "char", "class", "double", "float", "int", "long", "short", "string",
                           "void", "array"]

        identifiers = []

        for i in self.code.split('\n'):
            count = 0

            for w in i.split(' '):
                if w in identifier_list:
                    count += 1

            if count == 0:
                x = len(re.findall('\\((int|bool|string|short|float|byte)', i))
                count = x
            for w in i.split(' '):
                j = len(re.findall("(?<=.)\w+(?=\.)", w))
                count += j

            # Static identifiers
            for w in i.split(' '):
                c = len(re.findall('^[A-Z][\w]{1,20}[.]', w))
                count += c

            # Commons
            for w in i.split(' '):
                if '"' not in w:
                    c = len(re.findall('^[A-Z][\w]{1,20}', w))
                    count += c

            if "import " in i:
                count = 0

            identifiers.append(count * self.W_IDENTIFIER)

        return identifiers
