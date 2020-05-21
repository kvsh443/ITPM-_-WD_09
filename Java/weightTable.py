from db import Database as db


def database_table_retrieval(what_list, table_name):
    table = db("SELECT value from " + table_name + " ORDER BY id;")
    for row in table.result:
        what_list.append(row[0])


class WeightTable:
    variable = []
    size = []
    method = []
    inheritance = []
    coupling = []
    control_structures = []

    def __init__(self,):
        self.run()


    def clear_all(self):
        self.variable.clear()
        self.size.clear()
        self.method.clear()
        self.inheritance.clear()
        self.coupling.clear()
        self.control_structures.clear()

    def get_variable(self):
        return self.variable

    def get_size(self):
        return self.size

    def get_method(self):
        return self.method

    def get_inheritance(self):
        return self.inheritance

    def get_coupling(self):
        return self.coupling

    def get_control_structures(self):
        return self.control_structures

    def run(self):
        database_table_retrieval(self.variable, "variable_complexity")
        database_table_retrieval(self.size, "size_complexity")
        database_table_retrieval(self.method, "method_complexity")
        database_table_retrieval(self.inheritance, "inheritance_complexity")
        database_table_retrieval(self.coupling, "coupling_complexity")
        database_table_retrieval(self.control_structures, "control_structure_complexity")
