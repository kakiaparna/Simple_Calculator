class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a -self.b
    def multiply(self):
        return self.a*self.b
    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"
    def square(self):
        return self.a ** 2, self.b ** 2
    def modulus(self):
        if self.b != 0:
            return self.a % self.b
        else:
            return "Cannot divide by zero"
    def floor(self):
        if self.b != 0:
            return self.a // self.b
        else:
            return "Cannot divide by zero"

a=int(input("enter a:"))
b=int(input("enter b:"))
operation = input("Choose operation (+, -, *, /, //,**,%): ")

calc = calculator(a, b)

if operation == '+':
    print("Result:", calc.add())
elif operation == '-':
    print("Result:", calc.subtract())
elif operation == '*':
    print("Result:", calc.multiply())
elif operation == '/':
    print("Result:", calc.div())
elif operation == '//':
    print("Result:", calc.floor())
elif operation == '**':
    print("Result:", calc.square())
elif operation == '%':
    print("Result:", calc.modulus())
else:
    print("Invalid operation.")