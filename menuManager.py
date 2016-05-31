class MenuManagerBD:

	def createMenu():
		# Create SQL
		#cur.execute('CREATE DATABASE ;')
		# Create columns
		cursor.execute ("""
			 CREATE TABLE Menu
			 (
			 name CHAR(150),
			 price FLOAT,
			 tag CHAR(250),
			 description CHAR(600),
			 soyUse INT,
			 lactoUse INT,
			 glutUse INT,
			 )
			 """)

	def getMenu():
	# fetch 'em all
		cursor.execute ("SELECT * FROM Menu")
		rows = cursor.fetchall()
		for row in rows:
			print "%s, %s" % (row[0], row[1])
		print "%d rows were returned" % cursor.rowcount 
			 
	def printMenuNames():
		# for testing proposed ONLY
		for row in cur.fetchall():
			print row[0]

	def insertPlate(name, price, tag, description, soyUse, lactoUse, glutUse):
		cursor.execute("INSERT INTO table VALUES (%s, %s, %s, %s, %d, %d, %d)", 
		(name, price, tag, description, soyUse, lactoUse, glutUse)

	def idFunction(inputString):
		partString = inputString.split('@')
		funcCall = partString[0]
		paramFull = partString[1].split('𝛀')
		if(funcCall == "insertPlate"):
			name = paramFull[0]
			price = paramFull[1]
			tag = paramFull[2]
			description = paramFull[3]
			soyUse = paramFull[4]
			lactoUse = paramFull[5]
			glutUse = paramFull[6]
			insertPlate(name, price, tag, description, soyUse, lactoUse, glutUse)
		if(funcCall == "getMenu"):
			getMenu()
		else: print "deu ruim :/"

			

















	
