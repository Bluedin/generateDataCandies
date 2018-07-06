import cx_Oracle as cx


class CAD():
	"""docstring for CAD"""
	def __init__(self):
		#self.localFile = './localFile.json'
		self.connection = cx.connect('pl/123')



	def sendData(data, typeData):
		#TODO Formattage de données

 
		cursor = con.cursor()
		if(typeData=='order'):
			for item in data:
				client = item['client']
				cursor.execute('select ID from Pays where NOM=":Pays"', Pays=client['country'])
				for row in cursor:
					pays = row[0]
				try:
					cursor.execute('insert into Client("ADRESSE", "MAIL", "NOM", "PRENOM", "VILLE", "ID_PAYS") '\
						'  values(:Adresse, :Mail, :Nom, :Prenom, :Ville, :Pays)',\
						Adresse=client['adress'], Mail=client['mail'], Nom=client['surname'], Prenom=client['name'], Ville=client['city'], Pays=pays)
				except cx.DatabaseError as exc:
					error, = exc.args
					print("Code:     ", error.code, file=sys.stderr)
					print("Message   ", error.message.strip(), file=sys.stderr)
					print("Context   ", error.context, file=sys.stderr)
					cx.DatabaseError

				
				cursor.execute('select ID from Client where ADRESSE=:Adresse AND MAIL=:Mail AND NOM=:Nom AND PRENOM=:Prenom AND VILLE=:Ville AND PAYS=:Pays', \
					Adresse=client['adress'], Mail=client['mail'], Nom=client['surname'], Prenom=client['name'], Ville=client['city'], Pays=pays)
				
				for row in cursor:
					idClient = row[0]



				try:
					cursor.execute('insert into Commande("ENVOI", "LIVRAISON", "ID_CLIENT") '\
						'  values(TO_DATE(:Envoi, "dd/mm/yyyy hh24:mi:ss"), TO_DATE(:Livraison, "dd/mm/yyyy hh24:mi:ss"), :ID_Client)',\
						Envoi=item['date'], Livraison=item['date'], ID_Client=idClient)
				except cx.DatabaseError as exc:
					error, = exc.args
					print("Code:     ", error.code, file=sys.stderr)
					print("Message   ", error.message.strip(), file=sys.stderr)
					print("Context   ", error.context, file=sys.stderr)
					cx.DatabaseError

				cursor.execute('select ID from Commande where ENVOI=TO_DATE(:Envoi, "dd/mm/yyyy hh24:mi:ss") AND LIVRAISON=TO_DATE(:Livraison, "dd/mm/yyyy hh24:mi:ss") AND ID_CLIENT=:ID_client',\
					Envoi=item['date'], Livraison=item['date'], ID_Client=idClient)
				for row in cursor:
					idCommande = row[0]
				cursor.execute('select ID from Packetage where PACKETAGE=:Packetage', Packetage=item['container'])
				for row in cursor:
					idPacketage = row[0]

				idCandy = []
				count = 0
				for candyItem in item['contained']:
					cursor.execute('select ID from Bonbon inner join on Bonbon.ID_COULEUR = Couleur.ID inner join on Bonbon.ID_VARIANTE = Variante.ID inner join on Bonbon.ID_TEXTURE = Texture.ID where Bonbon.NOM = :Nom AND Couleur.COULEUR = :Couleur AND Variante.VARIANTE = :Variante AND Texture.TEXTURE = :Texture', \
						Nom = candyItem['name'], Couleur = candyItem['color'], Variante = candyItem['variation'], Texture = candyItem['texture'])
					for row in cursor:
						idCandy[count] = row[0]
				for id in idCandy:
					try:
						cursor.execute('insert into Bonbon_Client("ID_CONTENANT", "ID_COMMANDE", "ID_PACKETAGE", "ID_BONBON") '\
							'  values(:ID_Contenant, :ID_Commande, :ID_Packetage, :ID_Bonbon)',\
							ID_Contenant=1, ID_Commande=idCommande, ID_Packetage=idPacketage, ID_Bonbon=id)
					except cx.DatabaseError as exc:
						error, = exc.args
						print("Code:     ", error.code, file=sys.stderr)
						print("Message   ", error.message.strip(), file=sys.stderr)
						print("Context   ", error.context, file=sys.stderr)
						cx.DatabaseError







		if(typeData=='stockCandy'):
			for candyItem in data:
				cursor.execute('select ID from Bonbon inner join on Bonbon.ID_COULEUR = Couleur.ID inner join on Bonbon.ID_VARIANTE = Variante.ID inner join on Bonbon.ID_TEXTURE = Texture.ID where Bonbon.NOM = :Nom AND Couleur.COULEUR = :Couleur AND Variante.VARIANTE = :Variante AND Texture.TEXTURE = :Texture', \
					Nom = candyItem['name'], Couleur = candyItem['color'], Variante = candyItem['variation'], Texture = candyItem['texture'])
				for row in cursor:
					idCandy = row[0]
				try:
					cursor.execute('insert into stockBonbon("QUANTITE", "ID_BONBON") values(:Quantite, :ID_Bonbon)', \
						Quantite=candyItem['number'], ID_Bonbon=idCandy)
				except cx.DatabaseError as exc:
					error, = exc.args
					print("Code:     ", error.code, file=sys.stderr)
					print("Message   ", error.message.strip(), file=sys.stderr)
					print("Context   ", error.context, file=sys.stderr)
					cx.DatabaseError
			


		if(typeData=='stockMaterial'):
			try: 
				cursor.execute('insert into Stock_Composant("ADDITIF", "AROME", "ENROBAGE", "GELIFIANT", "SUCRE") values(:Additif, :Arome, :Enrobage, :Gelifiant, :Sucre)', \
					Additif=data['additif'], Arome=data['arome'], Enrobage=data['enrobage'], Gelifiant=data['gelifiant'], Sucre=data['sucre'])
			except cx.DatabaseError as exc:
				error, = exc.args
				print("Code:     ", error.code, file=sys.stderr)
				print("Message   ", error.message.strip(), file=sys.stderr)
				print("Context   ", error.context, file=sys.stderr)
				cx.DatabaseError
			

		cursor.close()
		self.connection.commit()

	def __del__(self):
		self.connection.close()

		



