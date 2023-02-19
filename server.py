#James Duong
#010639834
import socket

class Server():#Created class to implement deposit and withdraw
	def __init__(self):
		self.balance = 100
	def Deposit(self, statement):
		self.balance += statement
	def Withdraw(self, statement):
		if self.balance - statement < 0:
			return False
		self.balance -= statement
		return True

if __name__ == "__main__":
	HOST = socket.gethostname()#local host
	PORT = 27000
	bankAccount = Server()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.bind((HOST, PORT))#binds the socket
		sock.listen(5)
		connection, address = sock.accept()
		serverConnect = connection.recv(1024).decode()
		print(serverConnect)
		menuChoice = 0
		while menuChoice != "4":
			menuChoice = connection.recv(1024).decode()
			if menuChoice ==  "1":#sends to client how much they want to deposit and then displays the balance after deposit
				bankSentence = 'Please enter the amount you want to deposit'
				connection.send(bytes(str(bankSentence), "utf-8"))
				bankMsg = connection.recv(1024).decode()
				bankAccount.Deposit(int(bankMsg))
				bankSentence = ('With the deposit you made, your current balance is: $' + str(bankAccount.balance))
				connection.sendall(bytes(str(bankSentence), "utf-8"))
			if menuChoice == "2":#sends to client the amount withdrawn and the balance after
				bankSentence = ('How much would you like to withdraw?')
				connection.send(bytes(str(bankSentence), "utf-8"))
				bankMsg = connection.recv(1024).decode()
				if bankAccount.Withdraw(int(bankMsg)):
					bankSentence = ('With the withdraw you made, your new balance is: $' + str(bankAccount.balance))
				else:
					bankSentence = ('Insufficient funds. Try again.')
				connection.send(bytes(str(bankSentence), "utf-8"))
			if menuChoice == "3":#sends to client the balance
				connection.send(bytes(str(bankAccount.balance), "utf-8"))
			if menuChoice == "4":#closes server side
				bankMsg = connection.recv(1024).decode()
				print(bankMsg)
				connection.close()

