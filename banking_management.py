#source udemy

from abc import ABCMeta, abstractmethod
import random
class Account(metaclass = ABCMeta):
	@abstractmethod
	def createAccount():
		return 0
	@abstractmethod
	def authenticate():
		return 0
	@abstractmethod
	def withdraw():
		return 0
	@abstractmethod
	def deposite():
		return 0
	@abstractmethod
	def displayBalance():
		return 0

class SavingsAccount(Account):
	#map name and account no dictionary
	def __init__(self):
		self.SavingsAccount = {}
	def createAccount(self, name, initialDeposite):
		self.accountNumber = random.randint(10000, 99999)
		self.SavingsAccount[self.accountNumber] = [name, initialDeposite]
		print("Your account no is : ", self.accountNumber)
	def authenticate(self, name, accountNumber):
		if accountNumber in self.SavingsAccount.keys():
			if self.SavingsAccount[accountNumber][0] == name:
				print("Authentication successfull")
				self.accountNumber = accountNumber
				return True
			else: 
				print("Authentication fail")
				return False
		else:
			print("Authentication fail")
			return False

	def withdraw(self, withdrawlAmount):
		if withdrawlAmount > self.SavingsAccount[self.accountNumber][1]:
			print("Insufficient balance")
		else:
			self.SavingsAccount[self.accountNumber][1] -= withdrawlAmount
			print("Withdrawl was successfull, Available balance")
			displayBalance()
	def deposite(self, depositeAmount):
		self.SavingsAccount[self.accountNumber][1] =+depositeAmount
		print("Deposite was successfull, Available balance is")
		displayBalance()
	def displayBalance(self):
		print("Available balance :" , self.SavingsAccount[self.accountNumber][1])
savingsAccount = SavingsAccount()
while True:
	print("Enter 1 to create new account ")
	print("Enter 2 to access existing account ")
	print("Enter 3 for quit ")
	userchoice = int(input())
	if userchoice is 1:
		print("Enter name")
		name = input()
		print('Enter your initial deposite')
		deposite_ = int(input())
		savingsAccount.createAccount(name, deposite_)
	elif userchoice is 2:
		print("Enter name")
		name = input()
		print("Enter his account no")
		accountNumber = int(input())
		authenticationStatus = savingsAccount.authenticate(name, accountNumber)
		if authenticationStatus is True:
			while True:
				print("Enter 1 to withdraw")
				print("Enter 2 to deposite")
				print("Enter 3 to display available balance")
				print("Go back to previous menu")
				userchoice = int(input())
				if userchoice is 1:
					print("Enter a withdrawl amount")
					withdrawlAmount = int(input())
					savingsAccount.withdrawl(withdrawlAmount)
				elif userchoice is 2:
					print("Enter an amount to be deposited")
					depositeAmount = int(input())
					savingsAccount.deposite(depositeAmount)
				elif userchoice is 3:
					savingsAccount.displayBalance()
				elif userchoice is 4:
					break
	elif userchoice is 3:
		quit()




