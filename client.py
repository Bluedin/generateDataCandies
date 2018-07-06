"""extends Randomized
"""
from random import *
from randomized import Randomized as ran


class Client(ran):

	"""Client
	"""
	
	ran.clientName = ['John', 'Rémi', 'Jacques', 'Flora', 'Patrick', 'Jaqueline', 'Amélie', 'Karl']
	ran.surname = ['Dupon', 'Altran', 'Marx', 'Oltiv', 'Pretinka', 'Doe']
	ran.city = ['Berlin', 'Vienne', 'Bruxelles', 'Sofia', 'Nicosie', 'Zagreb', 'Copenhague', 'Madrid', 'Tallinn', 'Helsinki', 'Paris', 'Athènes', 'Budapest', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'La Valette', 'Amsterdam', 'Varsovie', 'Lisbonne', 'Prague', 'Bucarest', 'Londres', 'Bratislava', 'Ljubljana', 'Stockholm', 'Washington', 'Ottawa', 'Mexico', 'Tokyo', 'Pékin', 'Pretoria']
	ran.country = ['Allemagne', 'Autriche', 'Belgique', 'Bulgarie', 'Chypre',  'Croatie', 'Danemark', 'Espagne', 'Estonie', 'Finlande', 'France', 'Grèce', 'Hongrie', 'Irelande', 'Italie', 'Lettonie', 'Lituanie', 'Luxembourg', 'Malte', 'Pays-Bas', 'Pologne', 'Portugal', 'République tchèque', 'Roumanie', 'Royaume-Uni', 'Slovaquie', 'Slovénie', 'Suède', 'USA', 'Canada', 'Mexique', 'Japon', 'Chine', 'Afrique du sud']
	ran.adress = "Aldebaran Street"
	ran.mail = "@gmail.com"
	ran.instance = {'name': 'john', 'surname': 'Dupon', 'city': "Berlin", 'country': "Allemagne", 'adress': "Aldebaran Street", 'mail': "john.Dupon@gmail.com"}

	def getData(ran):
		"""get caracteristic of client
		
		Args:
		    ran (Randomized): self
		
		Returns:
		    list: caracteristic of client
		"""
		return ran.instance


	def randomize(ran):
		"""Summary
		
		Args:
		    ran (Randomized): self
		"""
		ran.instance['name'] = sample(ran.clientName, 1)[0]
		ran.instance['surname'] = sample(ran.surname, 1)[0]
		ran.instance['city'] = sample(ran.city, 1)[0]
		ran.instance['country'] = ran.country[ran.city.index(ran.instance['city'])]
		ran.instance['adress'] = ran.adress
		ran.instance['mail'] = ran.instance['name'] + '.' + ran.instance['surname'] + ran.mail


