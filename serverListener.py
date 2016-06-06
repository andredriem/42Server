'''
essa classe conecta o back end com o front end
'''

import socket
import menuManager

menuManager.getMenu()

HOST, PORT = 'localhost', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(('localhost', PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
#http_response = idFunction(inputString)



while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	while '\n' not in request:
		 request += client_connection.recv(1024)
	if not request:
		client_connection.close()
		print 'conexao terminada'
	else:
                function = request.split('@')[0]
                tam = len(function)
                parameters = request[tam+1:-1]
                parameters = parameters.split("','")

        if function == 'getMenu':
                menu = menuManager.getMenu()
                client_connection.send(menu)
        #elif function == 'insertDish':
        #    try:
                
            
        
		#print type(request)
		#print request
		#client_connection.send(http_response)
