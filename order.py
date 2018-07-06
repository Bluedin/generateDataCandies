
from random import *
from randomized import Randomized as ran
from client import Client
from candyOrder import CandyOrder

class Order(ran):

	"""The order which contains list of candy ordered, the container and the client
	Randomly create order ('random') or create order following a trend ('critic')
	"""
	
	def __init__(ran):
		"""initialize possible data to be chosen from
		as well as probality
		
		Args:
		    ran (randomized): self
		"""
		ran.container = ['Echantillon', 'Sachet', 'Boite']
		ran.containerNumber = {'Echantillon': 3, 'Sachet': 10, 'Boite': 25}
		ran.containerRandRange = {'Echantillon': 1, 'Sachet': 1, 'Boite': 1}
		ran.personalized = 0
		ran.personalizedRandRange = [1, 1]
		ran.maxIncreaseSecond = 7200
		ran.client = Client()
		ran.contained = []
		for i in range(ran.containerNumber['Boite']):
			ran.contained.append(CandyOrder())
			#print('ok')
		ran.containedMode = 'random'
		ran.year = 2018
		ran.month = 5
		ran.day = 8 
		ran.hour = 00
		ran.minute = 00
		ran.second = 00
		ran.date = '08-05-2018 00:00:00'
		ran.instance = {'container': 'Echantillon', 'contained': [], 'client': 0, 'date': '0', 'personalized': 0}

	def getData(ran):
		"""Summary
		
		Args:
		    ran (randomized): self
		
		Returns:
		    TYPE: Description
		"""
		return ran.instance

	def randomize(ran):
		"""randomly change value of order
		random: no particular trend followed
		critic: a random trend is created when changing mode to critic \
		 and followed until we change mode
		
		Args:
		    ran (randomized): self
		"""
		randRange = 0
		for do in ran.containerRandRange:
			randRange += ran.containerRandRange[do]
		chosen = randint(0, randRange-1)
		count = 0
		randRangeUnit = 0
		for do in ran.containerRandRange:
			randRangeUnit += ran.containerRandRange[do]
			if(ran.containerRandRange[do] == 0):
				count += 1
				continue
			if(chosen < randRangeUnit):
				break
			else:
				count += 1
		ran.instance['container'] = ran.container[count]

		randRange = 0
		for do in ran.personalizedRandRange:
			randRange += do
		chosen = randint(0, randRange-1)
		count = 0
		randRangeUnit = 0
		for do in ran.personalizedRandRange:
			randRangeUnit += ran.personalizedRandRange[do]
			if(ran.personalizedRandRange[do] == 0):
				count += 1
				continue
			if(chosen < randRangeUnit):
				break
			else:
				count += 1
		ran.personalized = count
		ran.instance['personalized'] = ran.personalized

		ran.client.randomize()
		ran.instance['client'] = ran.client.getData()
		ran.randomIncreaseDate()
		ran.compileDate()
		ran.instance['date'] = ran.date
		#print(ran.instance['container'])
		#print(ran.containerNumber[ran.instance['container']])
		ran.instance['contained'] = []
		if(ran.personalized == 0):
			for i in range(ran.containerNumber[ran.instance['container']]):
				ran.contained[0].randomize()
				ran.instance['contained'].append(ran.contained[0].getData())
		else:
			for i in range(ran.containerNumber[ran.instance['container']]):
				#print(i)
				ran.contained[i].randomize()
				ran.instance['contained'].append(ran.contained[i].getData())

	def compileDate(ran):
		"""set date of order base on unit value of time in the order
		
		Args:
		    ran (randomized): self
		"""
		if(ran.hour <= 10):
			hour = '0' + str(ran.hour)
		else:
			hour = str(ran.hour)
		if(ran.minute <= 10):
			minute = '0' + str(ran.minute)
		else:
			minute = str(ran.minute)
		if(ran.second <= 10):
			second = '0' + str(ran.second)
		else:
			second = str(ran.second)
		ran.date = str(ran.day) + '-' + str(ran.month) + '-' + str(ran.year) + ' ' + hour + ':' + minute + ':' + second

	def randomIncreaseDate(ran):
		"""randomly increase the date and time of order based on precedent
		random: between 0 and 2 hours
		critic: between 0 and 20 seconds
		
		Args:
		    ran (randomized): self
		"""
		secondIncrease = randint(1, ran.maxIncreaseSecond)
		hourIncrease = secondIncrease//3600
		secondIncrease = secondIncrease%3600
		minuteIncrease = secondIncrease//60
		secondIncrease = secondIncrease%60
		ran.second = (ran.second+secondIncrease)
		ran.minute = (ran.minute + minuteIncrease + ran.second//60)
		ran.second %= 60 
		ran.hour = (ran.hour + hourIncrease + ran.minute//60)
		ran.minute %= 60 
		ran.day = (ran.day + ran.hour//24)
		ran.hour %= 24
		ran.year = (ran.year + ran.day//365)
		ran.day %= 365

	def randomMode(ran):
		"""set mode to 'random'
		
		Args:
		    ran (randomized): self
		"""
		ran.containedMode = 'random'
		for do in ran.containerRandRange:
			ran.containerRandRange[do] = 1
		for i in range(ran.containerNumber['Boite']):
			ran.contained[i].changeMode(ran.containedMode)
		ran.maxIncreaseSecond = 7200

	def criticMode(ran):
		"""set mode to 'critic'
		
		Args:
		    ran (randomized): self
		"""
		ran.containedMode = 'critic'
		ran.containerRandRange[sample(ran.container, 1)[0]] = 10
		toFocus = ran.contained[0].criticMode()
		print(toFocus)
		for i in range(ran.containerNumber['Boite']):
			ran.contained[i].criticMode(toFocus)
		print(ran.containerRandRange)
		ran.maxIncreaseSecond = 20



	def changeMode(ran, mode):
		"""call either criticMode() or randomMode()
		
		Args:
		    ran (randomized): self 
		    mode (string): etheir 'random' or 'random'
		"""
		switcher = {'random': ran.randomMode, 'random': ran.criticMode}
		func = switcher.get(mode, lambda: 'invalid mode')
		func()

