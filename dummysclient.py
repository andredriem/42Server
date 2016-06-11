import socket
import sys



def sendData(string):

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port where the server is listening
	server_address = ('localhost', 8888)
	print >>sys.stderr, 'connecting to %s port %s' % server_address
	sock.connect(server_address)
	data = ''
	sock.sendall(string)

	while '\n' not in data:
		data += sock.recv(2024)
	return data 





    
# Send data
message = 'This is the message.  It will be repeated.'
print >>sys.stderr, 'sending "%s"' % message




#ADICIONA PRATOS NAO APROVADOS PELA PETA NO CARDAPIO
print sendData("""insertDish@['golfinhos','golpfhinhos frescos pescados de barcos
		  japoneses','false','false','false','false','pescados',0.5,99.95]\n""")
print sendData("""insertDish@['golfinhos2','golphinhos frescos pescados de barcos
		  japoneses','false','false','false','false','pescados',0.5,99.95]\n""")
print sendData("""insertDish@['golfinhos3','golphinhos frescos pescados de barcos
		  japoneses','false','false','false','false','pescados',0.5,99.95]\n""")

#EXIBE ELES
print sendData("getMenu@\n")

#INSERE UM REPITIDO PRA SIMULAR UM UPDATE (O CAMPO DE DESCRICAO FOI ALTERADO)
print sendData("""insertDish@['golfinhos3','na verdade sao tubaroes frescos pescados de barcos
		  japoneses','false','false','false','false','pescados',0.5,99.95]\n""")
print sendData("getMenu@\n")


#TESTA DELETE
print sendData("deleteDish@['golfinhos3']\n")

print sendData("getMenu@\n")


#TESTA DELETE EM TODOS OS PRATOS DELETADO + DELETE EM PRATOS NAO EXISTENTES
print sendData("deleteDish@['golfinhos3']\n")
print sendData("deleteDish@['golfinhos2']\n")
print sendData("deleteDish@['golfinhos1']\n")

#EXIBE CARDAPIO QUE DEVERIA ESTAR COMO O ORIGINAL
print sendData("getMenu@\n")


#ADICIONA UM NOVO GOLFINHO PRA FUTUROS TESTES
print sendData("""insertDish@['golfinhos','golpfhinhos frescos pescados de barcos
		  japoneses','false','false','false','false','pescados',0.5,99.95]\n""")


idorder = sendData("""sendOrder@[1]\n""")


print sendData("""changeOrderStatus@[%d,'em preparo']\n"""%(int(idorder)))

print sendData("""addDishToOrder@[%d,'pizza',2,1]\n"""%(int(idorder)))
print sendData("""addDishToOrder@[%d,'golfinhos',2,1]\n"""%(int(idorder)))
print sendData("""addDishToOrder@[%d,'hamburger',2,1]\n"""%(int(idorder)))

print sendData("""getOrder@[%d]\n"""%(int(idorder)))
print sendData("""Order@[%d]\n"""%(int(idorder)))





