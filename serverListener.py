'''
essa classe conecta o back end com o front end
'''

import socket
import menuManager
import orderManager
import SQLExceptions

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

        elif function == 'insertDish':
            	menuManager.insertDish(parameters[0], parameters[1], parameters[2], parameters[3], 
					parameters[4], parameters[5], parameters[6])
		client_connection.send('ok\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
		#print "insertDish of " + parameters[0] + " successful"

	elif function == 'deleteDish':
		menuManager.deleteDish(parameters[0])
		client_connection.send('ok\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
		#print "deleteDish of " + parameters[0] + " successful"

	elif function == 'insertOrder':
		try:
			orderManager.insertOrder(parameters[0],parameters[1])
			client_connection.send('ok\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
			#print "insertOrder of " + parameters[0] + " successful"
		except SQLTableInserionError:
			client_connection.send('error\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
			#print "insertOrder of " + parameters[0] + " error"

	elif function == 'changeOrderStatus':
		try:
			orderManager.changeOrderStatus(parameters[0],parameters[1])
			client_connection.send('ok\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
			#print "changeOrderStatus of " + parameters[0] + " successful"
		except SQLTableInserionError:
			client_connection.send('error\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
			#print "changeOrderStatus of " + parameters[0] + " error"


