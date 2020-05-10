from Tools import SizeComplexityMeasurer as SizeMeasurer
from Tools import VariableComplexityMeasurer as VariableMeasurer
from Tools import MethodComplexityMeasurer as MethodMeasurer
from Tools import ControlStructureComplexityMeasurer as ControlStructureMeasurer
from Tools import InheritanceComplexityMeasurer as InheritanceMeasurer
from Tools import CouplingComplexityMeasurer as CouplingMeasurer


# don't change the order unless you change order accordingly in calculate.php
class Helper:
    code = ""
    result = {}
    method_complexity = {}
    size_complexity = {}
    variable_complexity = {}
    control_structure_complexity = {}
    inheritance_complexity = {}
    coupling_complexity = {}
    lines = {}
    complete = False

    def __init__(self, code):
        if code:
            self.code = code
            self.run()

    def get_result(self):
        if self.complete:
            return self.result

    def run(self):
        #############################################################
        # Size Complexity
        m = SizeMeasurer.SizeComplexityMeasurer(self.code)
        lines = m.get_code_lines()
        self.lines = lines
        o = m.get_operators()
        k = m.get_keywords()
        n = m.get_numerical_values()
        s = m.get_string_literals()
        ide = m.get_identifiers()

        complexity = {}
        size_complexity = {"names": ['Code', 'Nkw', 'Nid', 'Nop', 'Nnv', 'Nsl', 'Cs']}

        for i in range(0, len(lines)):
            total = k[i] + ide[i] + o[i] + n[i] + s[i]
            size_complexity[i] = [lines[i], k[i], ide[i], o[i], n[i], s[i], total]

        complexity["size_complexity"] = size_complexity
        self.size_complexity = size_complexity

        #############################################################
        # Variable Complexity
        v = VariableMeasurer.VariableComplexityMeasurer(self.code)

        variable_complexity = {"names": ['Code', 'Wvs', 'Npdtv', 'Ncdtv', 'Cv']}

        for i in range(0, len(lines)):
            variable_complexity[i] = [lines[i], v.get_variable_scope_weight()[i], v.get_number_of_primitive_data()[i],
                                      v.get_number_of_composite_data()[i], v.get_variable_complexity()[i]]

        complexity["variable_complexity"] = variable_complexity
        self.variable_complexity = variable_complexity

        #############################################################
        # Method Complexity
        m = MethodMeasurer.MethodComplexityMeasurer(self.code)

        method_complexity = {"names": ['Code', 'Wmrt', 'Npdtp', 'Ncdtp', 'Cm']}

        for i in range(0, len(lines)):
            method_complexity[i] = [lines[i], m.get_weight_return_type()[i], m.get_number_of_primitive_params()[i],
                                    m.get_number_of_composite_params()[i], m.get_method_complexity()[i]]

        complexity["method_complexity"] = method_complexity
        self.method_complexity = method_complexity
        #############################################################
        # Coupling Complexity
        c = CouplingMeasurer.CouplingComplexityMeasurer(self.code)

        coupling_complexity = {
            "names": ['Code', 'Nr ', 'Nmcms', 'Nmcmd', 'Nmcrms', 'Nmcrmd', 'Nrmcrms', 'Nrmcrmd', 'Nrmcms', 'Nrmcmd',
                      'Nmrgvs', 'Nmrgvd',
                      'Nrmrgvs', 'Nrmrgvd', 'Çcp']}

        for i in range(0, len(lines)):
            total = c.total[i]
            coupling_complexity[i] = [lines[i], 0, c.rm_to_rm_inside[i],
                                      c.rm_to_rm_outside[i], c.rm_to_rcm_inside[i],
                                      c.rm_to_rcm_outside[i], c.rcm_rcm_inside[i], c.rcm_to_rcm_outside[i],
                                      c.rcm_to_rm_inside[i],
                                      c.rcm_to_rm_outside[i], c.rm_to_global_inside[i], c.rm_to_global_outside[i],
                                      c.rcm_to_global_inside[i], c.rcm_to_global_outside[i], total]

        complexity["coupling_complexity"] = coupling_complexity
        self.coupling_complexity = coupling_complexity

        #############################################################
        # Control Structures Complexity
        c = ControlStructureMeasurer.ControlStructureComplexityMeasurer(self.code)

        control_structure_complexity = {"names": ['Code', 'Wtcs', 'NC', 'Ccspps', 'Ccs']}

        for i in range(0, len(lines)):
            control_structure_complexity[i] = [lines[i], c.get_weight_due_to_type()[i], c.get_number_of_conditions()[i],
                                               c.get_weight_due_to_nest()[i], c.get_control_structure_complexity()[i]]

        complexity["control_structure_complexity"] = control_structure_complexity
        self.control_structure_complexity = control_structure_complexity
        ##############################################################
        # inheritance Complexity
        ih = InheritanceMeasurer.InheritanceComplexityMeasurer(self.code)

        inheritance_complexity = {"names": ['Code', 'Ndi', 'Nidi', 'Ti', 'Ci']}

        for i in range(0, len(lines)):
            inheritance_complexity[i] = [lines[i], ih.get_ndi()[i], ih.get_nidi()[i],
                                         ih.get_ti()[i], ih.get_complexity()[i]]

        complexity["inheritance_complexity"] = inheritance_complexity
        self.inheritance_complexity = inheritance_complexity

        #############################################################

        # Total Complexity

        complexity["final"] = self.get_final_result()
        self.result = complexity
        self.complete = True

    def get_final_result(self):
        final_complexity = {"names": ["code", "Cs", "Cv", "Cm", "Ccp", "Ccs", "Ci", "Total"]}

        inheritance = InheritanceMeasurer.InheritanceComplexityMeasurer(self.code)

        index = 0
        for l in self.lines:
            cs = self.size_complexity[index][len(self.size_complexity[index]) - 1]
            cv = (self.variable_complexity[index])[len(self.variable_complexity[index]) - 1]
            cm = (self.method_complexity[index])[len(self.method_complexity[index]) - 1]
            ccp = (self.coupling_complexity[index])[len(self.coupling_complexity[index]) - 1]
            ccs = (self.control_structure_complexity[index])[len(self.control_structure_complexity[index]) - 1]
            ci = inheritance.get_complexity()[index]
            total = cs + cv + cm + ccs + ci
            final_complexity[index] = [
                l,
                cs,
                cv,
                cm,
                ccp,
                ccs,
                ci,
                total
            ]
            index += 1

        return final_complexity
