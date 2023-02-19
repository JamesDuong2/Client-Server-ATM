#James Duong
#010639834
import socket
#created menu for ATM
def menu():
	print("**************Welcome to Duong's ATM***************")
	print("Press 1 for deposit.")
	print("Press 2 for withdraw.")
	print("Press 3 for Balance.")
	print("Press 4 to quit.")
HOST = socket.gethostname()#gets local machine
PORT = 27000 #give a port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: #creates object named sock
	# Connect to server and send data
	serverConnect = True
	print('The client has successfully connected to the server.')
	sock.connect((HOST, PORT))
	connectionMsg = "The client has connected to " + str(sock.getsockname()) + " on port " + str(PORT)
	sock.send(bytes(str(connectionMsg), "utf-8"))
	bankMenu = True
	while bankMenu:#menu choices that checks for general error and valid input from user
		menu()
		menuChoice = input()
		if menuChoice == "1" or menuChoice == "2":
			sock.send(bytes(str(menuChoice), "utf-8"))
			bankMsg = str(sock.recv(1024), "utf-8")
			print(bankMsg)
			bankUser = input()
			checkValid = False
			while not checkValid:#checks if input is valid 
				try:
					bankUser = int(bankUser)
					if bankUser > 0:
						checkValid = True
					else:
						print('Invalid input. Please try again.')
						bankUser = input()
				except ValueError:
					print('Invalid input. Please try again.')
					bankUser = input()
			sock.send(bytes(str(bankUser), "utf-8"))
			bankMsg = str(sock.recv(1024), "utf-8")
			print(bankMsg)
		elif menuChoice == "3":
			sock.send(bytes(str(menuChoice), "utf-8"))
			received = str(sock.recv(1024), "utf-8")
			print('Your current balance is: $' + received)
		elif menuChoice == "4":#closes the client and sends to server to close
			bankMenu = False
			sock.send(bytes(str('4'), "utf-8"))
		else:
			print('Invalid input. Please try again')
	closingMessage = 'The client has disconnected from ' + str(sock.getsockname())#sends message to server that tells user that it is closed
	sock.send(bytes(closingMessage + "\n", "utf-8"))
	
print('Thank you for using our bank!')