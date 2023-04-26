from flask import Flask, render_template, request, flash

import requests

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


# def minus(n1, n2):
#     return n1-n2


# def multiply(n1, n2):
#     return n1*n2


# def divide(n1, n2):
#     return n1/n2


@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')

    result = 0
    if operation == 'add':
        response = requests.get(
            'http://add-service:5051/{n1}/{n2}'.format(n1=number_1, n2=number_2))

        result = response.text
    elif operation == 'minus':
        response = requests.get(
            'http://sub-service:5052/{n1}/{n2}'.format(n1=number_1, n2=number_2))
        result = response.text
    elif operation == 'multiply':
        response = requests.get(
            'http://mul-service:5053/{n1}/{n2}'.format(n1=number_1, n2=number_2))
        result = response.text
    elif operation == 'divide':
        response = requests.get(
            'http://div-service:5054/{n1}/{n2}'.format(n1=number_1, n2=number_2))
        result = response.text
    elif operation == 'gcd':
        response = requests.get(
            'http://gcd-service:5055/{n1}/{n2}'.format(n1=number_1, n2=number_2))
        result = response.text
    elif operation == 'mod':
        response = requests.get(
            'http://mod-service:5056/{n1}/{n2}'.format(n1=number_1, n2=number_2))
        result = response.text
    elif operation == 'exponent':
        response = requests.get(
            'http://exponent-service:5057/{n1}/{n2}'.format(n1=number_1, n2=number_2))
        result = response.text

    flash(
        f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
