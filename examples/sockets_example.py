# https://redixhumayun.github.io/networking/2019/02/14/how-the-internet-speaks.html
'''
Practical example of web sockets for a simple client-server protocol:
	-The client sends a packet with the length of an incoming string
	-Then the client sends the string in bytes
	-The process is repeated until the client sends the "end" string to
	signify the end of transmission (EOT)

Note: for the sake of simplicity I will include both the client and the server
scripts in this same file. Obviously, they should be separated in the real world.
To run this example, separate both the scripts into different files, run the server
script and then the client script.
'''

# The sockets module
import socket


# Client script
# -------------------------------------------------------------------------------------

# List with the strings to be sent to the server (note how "end" is the last one, so the\
# server knows that the transmission is over when it receives this string)
arr = ['hello', 'strings', 'that', 'need', 'to', 'be', 'transferred', 'across', 'the', 'network', 'using', 'sockets', 'end']
# Create a socket for the client
client_socket = socket.socket()
# Connect the client to localhost (127.0.0.1), to port 8000
client_socket.connect( ("127.0.0.1", 8000) )

# Loop through the list of strings to send one at a time. Before sending the actual string\
# (in bytes), send the length of the string (in bytes as well), so that the server knows\
# how many bits to access
for string in arr:
	# Convert the string into its bytes representation
	bytes_string = string.encode("utf-8")
	# Get the length of the bytes representation of the string
	len_of_string = len(bytes_string)
	# Since `len()` returns an int, convert that value to bytes (to send it to the server)
	len_in_bytes = len_of_string.to_bytes(2, byteorder="little")
	# Send the length of the string (in bytes)
	client_socket.send(len_in_bytes)
	# Send the string (in bytes)
	client_socket.send(bytes_string)

# After sending all the strings, close the socket
client_socket.close()

# -------------------------------------------------------------------------------------



# Server script
# -------------------------------------------------------------------------------------

# Create a socket for the server
server_socket = socket.socket()
# Connect the server to the same IP and port of the client (only because these are both
# run on the same computer, usually they would have different IP addresses) 
server_socket.bind( ("127.0.0.1", 8000) )
# The server accepts takes one unaccepted connection before refusing new connections
server_socket.listen(1)

# Accept a new connection (returns a `(conn, address)` pair where the first is a new\
# socket object and the second is the address bound to the first element)
client_socket, address = server_socket.accept()

# Variables to be used in the loop
# True if the next packet will contain the length of the string to be received next;\
# else False (the packet contains the string itself)
receiving_length = True
# Will hold the length of the string (used to adjust how many bytes the socket accepts)
str_length = None

# The loop runs until the end of the transmission
while True:

	# If the client is sending the length of the string
	if receiving_length:
		# The length of the string needs two bytes to be received
		data = client_socket.recv(2)
		# Convert the length of the string back to int
		str_length = int.from_bytes(data, byteorder="little")
		# Now are not expecting the client to send the length of the string in the\
		# next packet
		receiving_length = not receiving_length

	# If the client is sending the string itself
	else:
		# We'll accept from the client as many bytes as the content of the previous\
		# packet specified
		data = client_socket.recv(str_length)
		# Convert the bytes content of the packet back to string
		string = data.decode("utf-8")
		# Now we expect the client to send the length of a string in the next packet
		receiving_length = not receiving_length

		# If the client sent the `"end"` string, then it signifies the end of the transmission
		if string == "end":
			break

		# Print the string sent by the client
		print(string)

# Close the client socket
client_socket.close()

# -------------------------------------------------------------------------------------