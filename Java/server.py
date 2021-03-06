
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_restful.utils import cors
from Helper import Helper as code_measurer
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#db = SQLAlchemy(app)  # just created the db for future purposes.
CORS(app)
api = Api(app)


@app.route("/")
def hello():
    return "hello! Pat me at <a href='https://itpm-wd-09.azurewebsites.net/'> here </a>"

class CodeComplexity(Resource):
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter code

    def post(self):
        code = request.form['code']
        print(str(code))
        cm = code_measurer(code)
        return cm.get_result()


class SizeComplexity(Resource):
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter code

    def post(self):
        code = request.form['code']
        print(str(code))
        cm = code_measurer(code)
        return cm.size_complexity


class MethodComplexity(Resource):
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter code

    def post(self):
        code = request.form['code']
        print(str(code))
        cm = code_measurer(code)
        return cm.method_complexity


class VariableComplexity(Resource):
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter code

    def post(self):
        code = request.form['code']
        print(str(code))
        cm = code_measurer(code)
        return cm.variable_complexity


class ControlStructureComplexity(Resource):
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter code

    def post(self):
        code = request.form['code']
        print(str(code))
        cm = code_measurer(code)
        return cm.control_structure_complexity


class CouplingComplexity(Resource):
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter code

    def post(self):
        code = request.form['code']
        print(str(code))
        cm = code_measurer(code)
        return cm.coupling_complexity


class FinalResult(Resource):
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter code

    def post(self):
        code = request.form['code']
        print(str(code))
        cm = code_measurer(code)
        return cm.get_final_result()


class InheritanceComplexity(Resource):
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter code

    def post(self):
        code = request.form['code']
        print("Inhertance:- " + str(code))
        cm = code_measurer(code)
        return cm.inheritance_complexity

class File_Result(Resource):
    @cors.crossdomain(origin='*')
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter

    @cors.crossdomain(origin='*')
    def post(self):
        code = request.form['code']
        print(str(code))
        cm = code_measurer(code)
        return "" + str(cm.file_complexity) + ""

class File_Result_All(Resource):
    @cors.crossdomain(origin='*')
    def get(self):
        return "Error : Please Enter your code"  # Return Error to enter

    @cors.crossdomain(origin='*')
    def post(self):
        code = request.form['code']
        print(str(code))
        cm = code_measurer(code)
        response = [cm.file_cs, cm.file_cv, cm.file_cm, cm.file_ccp, cm.file_ccs, cm.file_ci, cm.file_complexity]
        return {'Total': response}

api.add_resource(CodeComplexity, '/codecomplexity')  # Route_1
api.add_resource(SizeComplexity, '/codecomplexity/size')  # Route_2
api.add_resource(MethodComplexity, '/codecomplexity/methods')  # Route_3
api.add_resource(VariableComplexity, '/codecomplexity/variables')  # Route_4
api.add_resource(ControlStructureComplexity, '/codecomplexity/control_structures')  # Route_5
api.add_resource(CouplingComplexity, '/codecomplexity/coupling_structures')  # Route_7
api.add_resource(InheritanceComplexity, '/codecomplexity/inheritance')  # Route_6
api.add_resource(FinalResult, '/codecomplexity/final')  # Route_8
api.add_resource(File_Result, '/codecomplexity/file')  # Route_9
api.add_resource(File_Result_All, '/codecomplexity/All')  # Route_10


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0',port=port)
