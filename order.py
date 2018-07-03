from random import *
from randomized import Randomized as ran
from client import Client
from candy import Candy

class Order(ran):

	def __init__(ran):
		ran.container = ['Echantillon', 'Sachet', 'Boite']
		ran.containerNumber = {'Echantillon': 3, 'Sachet': 10, 'Boite': 25}
		ran.client = Client()
		ran.contained = Candy()
		ran.instance = {'container': 'Echantillon', 'contained': [], 'client': 0}

	def getData(ran):
		return ran.instance

	def randomize(ran):
		ran.instance['container'] = sample(ran.container, 1)[0]
		ran.contained.randomize()
		ran.instance['client'] = ran.contained.getData()
		print(ran.instance['container'])
		print(ran.containerNumber[ran.instance['container']])

		for i in range(ran.containerNumber[ran.instance['container']]):
			ran.contained.randomize()
			ran.instance['contained'].append(ran.contained.getData())


