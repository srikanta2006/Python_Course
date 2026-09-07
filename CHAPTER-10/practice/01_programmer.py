class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

    def getInfo(self):
        print(f"Name of the employee is {self.name}, salary being {self.salary} and stays at pincode {self.pincode}")

p = Programmer("Srikanta", 130000, 500039)

r = Programmer("Rohan", 120000, 500039)

p.getInfo()
r.getInfo()