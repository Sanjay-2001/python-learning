from random import randint


class Train:

    def __init__(self, trainNo, fro, to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to

    def book(self):
        print(
            f"Ticket is booked in train no : {self.trainNo}. From {self.fro} to {self.to}")

    def getStatus(self, time):
        print(f"Train no : {self.trainNo} is running {time}")

    def getFare(self):
        print(
            f"The ticket fare in train no : {self.trainNo} from {self.fro} to {self.to} is {randint(222,5555)}")


t = Train(12399, "Pune", "Howrah")
t.book()
t.getStatus("not on time")
t.getFare()
