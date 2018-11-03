import BloodTest
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class bloodTester(Resource):
    def get(self, first_number, second_number):
        return {'Num': BloodTest.get_blood_cell_count()}

api.add_resource(bloodTester, '/bloodtest/')

if __name__ == '__main__':
     app.run()