from flask import Flask
from flask_restful import Resource,Api, reqparse

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api=Api(app)

class Add(Resource):
    def get(self,n1,n2):
        return float(n1)+float(n2)

api.add_resource(Add, '/<n1>/<n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5051,
        host="0.0.0.0"
    )
