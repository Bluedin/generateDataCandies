from random import *
from randomized import Randomized as ran


class Client(ran):

	
	ran.clientName = ['John', 'Rémi', 'Jacques', 'Flora', 'Patrick', 'Jaqueline', 'Amélie', 'Karl']
	ran.surname = ['Dupon', 'Altran', 'Marx', 'Oltiv', 'Pretinka', 'Doe']
	ran.city = ['Berlin', 'Vienne', 'Bruxelles', 'Sofia', 'Nicosie', 'Zagreb', 'Copenhague', 'Madrid', 'Tallinn', 'Helsinki', 'Paris', 'Athènes', 'Budapest', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'La Valette', 'Amsterdam', 'Varsovie', 'Lisbonne', 'Prague', 'Bucarest', 'Londres', 'Bratislava', 'Ljubljana', 'Stockholm', 'Washington', 'Ottawa', 'Mexico', 'Tokyo', 'Pékin', 'Pretoria']
	ran.country = ['Allemagne', 'Autriche', 'Belgique', 'Bulgarie', 'Chypre',  'Croatie', 'Danemark', 'Espagne', 'Estonie', 'Finlande', 'France', 'Grèce', 'Hongrie', 'Irelande', 'Italie', 'Lettonie', 'Lituanie', 'Luxembourg', 'Malte', 'Pays-Bas', 'Pologne', 'Portugal', 'République tchèque', 'Roumanie', 'Royaume-Uni', 'Slovaquie', 'Slovénie', 'Suède', 'USA', 'Canada', 'Mexique', 'Japon', 'Chine', 'Afrique du sud']
	ran.adress = "Aldebaran Street"
	ran.mail = "@gmail.com"
	ran.instance = ['john', 'Dupon', "Berlin", "Allemagne", "Aldebaran Street", "john.Dupon@gmail.com"]

	def getData(ran):
		for instance in ran.instance:
			print(instance)


	def randomize(ran):
		ran.instance[0] = sample(ran.clientName, 1)[0]
		ran.instance[1] = sample(ran.surname, 1)[0]
		ran.instance[2] = sample(ran.city, 1)[0]
		ran.instance[3] = ran.country[ran.city.index(ran.instance[2])]
		ran.instance[4] = ran.adress
		ran.instance[5] = ran.instance[0] + '.' + ran.instance[1] + ran.mail


