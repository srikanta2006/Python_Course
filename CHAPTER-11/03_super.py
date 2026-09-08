class Employee:
    def __init__(self):
        print("Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Programmer")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Manager")
    c=3


e = Employee()
p = Programmer()
m = Manager()

# print(e.a)
# print(p.a, p.b)
# print(m.a, m.b, m.c)