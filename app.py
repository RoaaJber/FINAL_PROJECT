# app.py

from flask import Flask, request, jsonify
from calculator import Calculator

app = Flask(__name__)
calculator = Calculator()

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = calculator.add(data['x'], data['y'])
    return jsonify(result=result)

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = calculator.subtract(data['x'], data['y'])
    return jsonify(result=result)

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = calculator.multiply(data['x'], data['y'])
    return jsonify(result=result)

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    try:
        result = calculator.divide(data['x'], data['y'])
        return jsonify(result=result)
    except ValueError as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
