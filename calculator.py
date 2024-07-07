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

# Now, we can retrieve the result from the calculator endpoint
calculator_endpoint = base_url + "get_result"
calculator_response = requests.get(calculator_endpoint)

if calculator_response.status_code == 200:
    calculator_result = calculator_response.json()
    print(f"Result from calculator: {calculator_result['result']}")
else:
    print(f"Failed to retrieve result from calculator: {calculator_response.status_code}")
#Explanation
