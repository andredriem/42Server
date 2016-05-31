
import socket
import copy

HOST, PORT = 'localhost', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(('localhost', PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
http_response = "pizza:0:30:uma pizza:ture:false:false:true&salada:1:50:uma salada:false:true:true:false&BigCopyrightInringmentMac:2:99.99:nao e um big mac:false:true:true:false\n"

print http_response


while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	while '\n' not in request:
		 request += client_connection.recv(1024)
	if not request:
		client_connection.close()
		print 'conexao terminada'
	else:
		print type(request)
		print request
		client_connection.send(http_response)
		temp = request.split('@')
		if temp[0] == 'sendDish':
			
			print temp[1]
			http_response = copy.copy(http_response[:-1]) + '&' + copy.copy(temp[1]) 
			print http_response
	
