class twoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"({self.i},{self.j})")

class threeDVector(twoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
            print(f"({self.i},{self.j},{self.k})")

o = twoDVector(1, 2)

b = threeDVector(1,2,3)

o.show()
b.show()