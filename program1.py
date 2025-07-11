class Calculator:   
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def calculate(self, operation):
        if(operation == "addition"):
            print(self.a + self.b)
            print("Type of operation:", operation)
        elif(operation == "subtraction"):
            print(self.a - self.b)
            print("Type of operation:", operation)
        elif(operation == "multiplication"):
            print(self.a * self.b)
            print("Type of operation:", operation)
        elif(operation == "division"):
            print(self.a / self.b)
            print("Type of operation:", operation)
        else:
            print("Invalid operation")
calculatorOutput = Calculator(2,3)
calculatorOutput.calculate("multiplication")