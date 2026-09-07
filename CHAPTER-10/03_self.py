class Employee:
    name = "Srikanta" #class attribute
    role = "Data science"
    salary = 1200000


    def getInfo(self):
        print(f"The role is {self.role} and salary is {self.salary}")

    @staticmethod #decorator to mention static method
    def greet(): # self not needed
        print("Good morning!")

person = Employee()

person.getInfo()
person.greet()