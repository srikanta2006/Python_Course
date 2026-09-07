class Employee():
    name = "Harry"
    language = "Python"


person = Employee()
person.language = "Java Script" #instance attribute take preference over class attribute while retieval and assigning

print(person.language)