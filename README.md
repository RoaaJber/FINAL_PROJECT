# calculator.py

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

** This class is designed to handle basic arithmetic operations for integers and floats, and it raises an error if we have tried to devide any numer over Zero.
=======================================================================================================================================================================++
# app.py

from flask import Flask, request, jsonify
from calculator import Calculator

app = Flask(__name__)
calculator = Calculator()

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()
        result = calculator.add(data['x'], data['y'])
        return jsonify(result=result)
    else:
        return "This endpoint supports POST requests only.", 405

## Description: Handles both GET and POST requests to /add.
## POST: Expects JSON data with keys x and y, performs addition using calculator.add, and returns the result as JSON.
## GET: Returns a 405 Method Not Allowed error with a message indicating that only POST requests are supported. 

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = calculator.subtract(data['x'], data['y'])
    return jsonify(result=result)

## Description: Handles POST requests to /subtract.
## POST: Expects JSON data with keys x and y, performs subtraction using calculator.subtract, and returns the result as JSON.

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = calculator.multiply(data['x'], data['y'])
    return jsonify(result=result)

## Description: Handles POST requests to /multiply.
## POST: Expects JSON data with keys x and y, performs multiplication using calculator.multiply, and returns the result as JSON.

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

## Flask: Imports the Flask framework for creating web applications.
## calculator: Imports the Calculator class from calculator.py that provides arithmetic operations.


#########################################################################################################################
in the above code we have the FLASK application and This Flask application defines several routes for performing arithmetic operations (add, subtract, multiply, divide) using a Calculator class imported from calculator.py. 
# Example for the addtion:
 >> Endpoint /add
 Method: POST
Input: JSON payload with keys x and y representing numbers.
Output: JSON response with the sum of x and y.


# Example input (POST request body):
{
    "x": 5,
    "y": 3
}
# Expected output:
{
    "result": 8
}

and the above will be applied to the other mathmatic methods. 







