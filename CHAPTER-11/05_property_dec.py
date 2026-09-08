class Employee:
    a = 1

    def show(self):
        print(f"object attribute -> {self.a}")

    @classmethod
    def showClass(cls):
        print(f"class attribute -> {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]


e = Employee()
e.name = "Srikanta Bellamkonda"
print(e.name)
