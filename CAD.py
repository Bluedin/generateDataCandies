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
				cursor.execute('select ID from Pays where Nom=":Pays"', Pays=client['country'])
				for row in cursor:
					pays = row[0]
				try:
					cursor.execute('insert into Client("Adresse", "Mail", "Nom", "Prenom", "Ville", "ID_Pays") '\
						'  values(:Adresse, :Mail, :Nom, :Prenom, :Ville, :Pays)',\
						Adresse=client['adress'], Mail=client['mail'], Nom=client['surname'], Prenom=client['name'], Ville=client['city'], Pays=pays)
				except cx.DatabaseError as exc:
					error, = exc.args
					print("Code:     ", error.code, file=sys.stderr)
					print("Message   ", error.message.strip(), file=sys.stderr)
					print("Context   ", error.context, file=sys.stderr)
					cx.DatabaseError

				
				cursor.execute('select ID from Client where Adresse=:Adresse AND Mail=:Mail AND Nom=:Nom AND Prenom=:Prenom AND Ville=:Ville AND Pays=:Pays', \
					Adresse=client['adress'], Mail=client['mail'], Nom=client['surname'], Prenom=client['name'], Ville=client['city'], Pays=pays)
				
				for row in cursor:
					idClient = row[0]



				try:
					cursor.execute('insert into Commande("Envoi", "Livraison", "ID_Client") '\
						'  values(TO_DATE(:Envoi, "dd/mm/yyyy hh24:mi:ss"), TO_DATE(:Livraison, "dd/mm/yyyy hh24:mi:ss"), :ID_Client)',\
						Envoi=item['date'], Livraison=item['date'], ID_Client=idClient)
				except cx.DatabaseError as exc:
					error, = exc.args
					print("Code:     ", error.code, file=sys.stderr)
					print("Message   ", error.message.strip(), file=sys.stderr)
					print("Context   ", error.context, file=sys.stderr)
					cx.DatabaseError

				cursor.execute('select ID from Commande where Envoi=TO_DATE(:Envoi, "dd/mm/yyyy hh24:mi:ss") AND Livraison=TO_DATE(:Livraison, "dd/mm/yyyy hh24:mi:ss") AND ID_Client=:ID_client',\
					Envoi=item['date'], Livraison=item['date'], ID_Client=idClient)
				for row in cursor:
					idCommande = row[0]
				cursor.execute('select ID from Packetage where Packetage=:Packetage', Packetage=item['container'])
				for row in cursor:
					idPacketage = row[0]

				idCandy = []
				count = 0
				for candyItem in item['contained']:
					cursor.execute('select ID from Bonbon inner join on Bonbon.ID_Couleur = Couleur.ID inner join on Bonbon.ID_Variante = Variante.ID inner join on Bonbon.ID_Texture = Texture.ID where Bonbon.Nom = :Nom AND Couleur.Couleur = :Couleur AND Variante.Variante = :Variante AND Texture.Texture = :Texture', \
						Nom = candyItem['name'], Couleur = candyItem['color'], Variante = candyItem['variation'], Texture = candyItem['texture'])
					for row in cursor:
						idCandy[count] = row[0]
				for id in idCandy:
					try:
						cursor.execute('insert into Bonbon_Client("ID_Contenant", "ID_Commande", "ID_Packetage", "ID_Bonbon") '\
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
				cursor.execute('select ID from Bonbon inner join on Bonbon.ID_Couleur = Couleur.ID inner join on Bonbon.ID_Variante = Variante.ID inner join on Bonbon.ID_Texture = Texture.ID where Bonbon.Nom = :Nom AND Couleur.Couleur = :Couleur AND Variante.Variante = :Variante AND Texture.Texture = :Texture', \
					Nom = candyItem['name'], Couleur = candyItem['color'], Variante = candyItem['variation'], Texture = candyItem['texture'])
				for row in cursor:
					idCandy = row[0]
				try:
					cursor.execute('insert into stockBonbon("Quantite", "ID_Bonbon") values(:Quantite, :ID_Bonbon)', \
						Quantite=candyItem['number'], ID_Bonbon=idCandy)
				except cx.DatabaseError as exc:
					error, = exc.args
					print("Code:     ", error.code, file=sys.stderr)
					print("Message   ", error.message.strip(), file=sys.stderr)
					print("Context   ", error.context, file=sys.stderr)
					cx.DatabaseError
			


		if(typeData=='stockMaterial'):
			try: 
				cursor.execute('insert into Stock_Composant("Additif", "Arome", "Enrobage", "Gelifiant", "Sucre") values(:Additif, :Arome, :Enrobage, :Gelifiant, :Sucre)', \
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

		



