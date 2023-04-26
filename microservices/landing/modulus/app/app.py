from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api=Api(app)

class Modulus(Resource):
    def get(self,n1,n2):
        if(n2==0):
            return 'Undefined'
        else:
            return int(n1)%int(n2)
        
api.add_resource(Modulus, '/<n1>/<n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5056,
        host="0.0.0.0"
    )
