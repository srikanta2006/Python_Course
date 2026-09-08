class Employee:
    company = "ITC"
    name = "Default"
    def show(self):
        print(f"Name of employee is {self.name}")

class Coder:
    language = "python"
    def showLanguage(self):
        print(f"The language choosen is {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    name = "Default"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}")

a = Employee()
b = Programmer()

b.show()
b.showLanguage()