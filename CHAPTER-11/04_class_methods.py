class Employee:
    a = 1

    def show(self):
        print(f"object attribute -> {self.a}")

    @classmethod
    def showClass(cls):
        print(f"class attribute -> {cls.a}")

e = Employee()
e.a = 18

e.show()
e.showClass()