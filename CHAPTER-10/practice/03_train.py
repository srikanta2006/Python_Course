class Train:
    name = "Venkatadri express"
    number = 12797
    type = "Super fast express"
    start = "Hyderabad"
    end = "chittoor"
    fare = 500
    available_seats = 20

    def getStatus(self):
        print(f"{self.available_seats} seats are available for booking")

    def getFare(self):
        print(f"The fare of each ticket is {self.fare}")

    def bookTickets(self, n):
        if(self.available_seats<n):
            print(f"{n} seats are not available, please check status")

        else:
            price = n*self.fare
            self.available_seats = self.available_seats-n
            print(f"{n} Tickets booking successfull, amount payable is {price}")

user = Train()
user.getStatus()
user.getFare()
user.bookTickets(25)
user.bookTickets(4)
user.getStatus()
