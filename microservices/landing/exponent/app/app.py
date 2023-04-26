from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)


class Exponent(Resource):
    def get(self, n1, n2):
        return str(float(n1)**float(n2))


api.add_resource(Exponent, '/<n1>/<n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5057,
        host="0.0.0.0"
    )
