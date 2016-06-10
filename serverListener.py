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
	print 'start iteration'
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	while '\n' not in request:
		 request += client_connection.recv(1024)

	print request
	if not request:
		client_connection.close()
		print 'conexao terminada'
	else:
                function = request.split('@')[0]
                tam = len(function)
                parameters = request[tam+1:-1]
                parameters = parameters.split(",")
		print parameters
	print function
        if function == 'getMenu':
                menu = menuManager.getMenu()
		
                client_connection.send(menu+'\n')

        elif function == 'insertDish':
		try:
		    	menuManager.insertDish(parameters[0][2:-1],
			parameters[1][1:-1], parameters[2][1:-1],
		        parameters[3][1:-1],parameters[4][1:-1],
			parameters[5][1:-1], parameters[6][1:-1],
			parameters[7],parameters[8][:-1])
		except:
			client_connection.send('false\n')
		else:
			client_connection.send('true\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
		#print "insertDish of " + parameters[0] + " successful"

	elif function == 'deleteDish':
		try:
			menuManager.deleteDish(parameters[0][2:-2])
		except:
			client_connection.send('false\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
		else:
			client_connection.send('true\n')
		#print "deleteDish of " + parameters[0] + " successful"

	elif function == 'sendOrder':
		
		try:
			print parameters[0]
			return_value = orderManager.insertOrder(parameters[0][1:-1],'solicitado')
			#print "insertOrder of " + parameters[0] + " successful"
		except:
			client_connection.send('false\n')
		else:
			client_connection.send(str(return_value)+'\n')
	
		
		#print "insertOrder of " + parameters[0] + " error"

	elif function == 'changeOrderStatus':
		try:
			orderManager.changeOrderStatus(parameters[0][1:],parameters[1][1:-2])
			#print "changeOrderStatus of " + parameters[0] + " successful"
		except:
			client_connection.send('false\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
			#print "changeOrderStatus of " + parameters[0] + " error"
		else:
			client_connection.send('true\n')
	elif function == 'addDishToOrder':
		try:
			orderManager.addDishToOrder(parameters[0][1:],parameters[1][1:1],parameters[2],parameters[3][:-1])
			#print "changeOrderStatus of " + parameters[0] + " successful"
		except:
			client_connection.send('false\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
			#print "changeOrderStatus of " + parameters[0] + " error"
		else:
			client_connection.send('true\n')

	elif function == 'ressetOrder':

		try:
			orderManager.deleteAllDishesFromOrder(parameters[0][1:-1])
		except:
			client_connection.send('false\n') #REVISAR MENSAGEM QUE DEVE SER O RETORNO
		else:
				client_connection.send('true\n')
		#print "deleteDish of " + parameters[0] + " successful"










