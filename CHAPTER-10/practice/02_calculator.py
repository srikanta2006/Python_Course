class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number**2

    def cube(self):
        return self.number**3

    def squareRoot(self):
        return self.number**0.5

    def printResult(self):
        print(f"number : {self.number},  square : {self.square()}, cube : {self.cube()}, squareRoot : {self.squareRoot()}")


n = int(input("Enter the number to calculate: "))

cal = Calculator(n)

cal.printResult()
