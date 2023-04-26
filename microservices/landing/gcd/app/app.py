from flask import Flask
from flask_restful import Resource,Api
import math

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api=Api(app)

class Gcd(Resource):
    def get(self,n1,n2):
        return math.gcd(int(n1),int(n2))
        

api.add_resource(Gcd, '/<n1>/<n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5055,
        host="0.0.0.0"
    )
