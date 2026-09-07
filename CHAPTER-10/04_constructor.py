class Employee:
    def __init__(self, name, role, salary): #dunder method which is automatically called
        self.name = name
        self.role = role
        self.salary = salary

    def getInfo(self):
        print(f"{self.name} works as {self.role} and salary is {self.salary}")

person = Employee("Srikanta", "Data Scienctist", 120000)
person.getInfo()