class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3


e = Employee()
p = Programmer()
m = Manager()

print(e.a)
print(p.a, p.b)
print(m.a, m.b, m.c)