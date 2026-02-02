# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
import random

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train number: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train number: {self.trainNo} is on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train number: {self.trainNo} from {fro} to {to} is {random.randint(333, 937)}")


t = train(12345)
t.book("Kochi", "Hyderabad")
t.getstatus()
t.getfare("Kochi", "Hyderabad")
