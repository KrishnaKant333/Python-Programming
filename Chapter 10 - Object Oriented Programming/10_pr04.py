# import random # instead of importing whole of random we can just :
from random import randint
import time
class Train:
	def __init__(self, trainNo):
		self.trainNo = trainNo

	def bookTicket(self, fro, to):
		print(f"The ticket is successfully booked in train no. {self.trainNo} from {fro} to {to}.")

	def getStatus(self):
		print("Checking train status..")
		time.sleep(1.5)
		print(f"Train no. {self.trainNo} is running on time.")

	def fareInfo(self, fro, to):
		print(f"The ticket fare in train no. {self.trainNo} from {fro} to {to} is {randint(50, 1000)}.")

def getRoute():
		src = input("Enter the source of the journey : ")
		dstn = input("Enter the destination of the journey : ")
		return src, dstn

while True:
	pnr = int(input("Enter the PNR of the train : "))

	if 10000 <= pnr <= 99999:
		T = Train(pnr)

		print("Welcome to Sasta IRCTC Website : ")
		print("Press 1 to book the Ticket : ")
		print("Press 2 to check the running status of the Train : ")
		print("Press 3 to get the fare information of the Train : ")
		print("Press 4 to Exit the portal : ")
		prompt = int(input("Enter your choice : "))

		if prompt == 1:
			src, dstn = getRoute()
			T.bookTicket(src, dstn)

		elif prompt == 2:
			T.getStatus()

		elif prompt == 3:
			src, dstn = getRoute()
			T.fareInfo(src, dstn)

		elif prompt == 4:
			print("Thank you for using our portal.")
			break

		else:
			print("Please enter a valid choice!")
	else:
		print("Please enter a valid 5 digit PNR only!!")
