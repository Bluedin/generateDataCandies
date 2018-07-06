"""used import are random and class Candy
"""
from random import *
from candy import Candy

class CandyStock():

	"""CandyStock : contains list of candy with their number
	is also used to modify the number of candy
	has multiple mode of automatic modification
	
	Attributes:
	    candies (list): list of candy
	    chosenCritic (list): candy chosen to be decreased in priority
	    mode (str): mode of the randomization : 'random' or 'critic'
	"""
	
	def __init__(self):
		"""instanciation 
		mode by default is 'random'
		instanciate list of all candy based on possible candy in Candy base value
		"""
		self.mode = 'random'
		self.candies = []
		self.chosenCritic = []
		for name in Candy.name:
			for color in Candy.color:
				for variation in Candy.variation:
					for texture in Candy.texture:
						self.candies.append(Candy(name, color, variation, texture))

	def checkStockCandy(candySpec):
		"""check if a candy has a number under 3000
		
		Args:
		    candySpec (TYPE): candy to check
		
		Returns:
		    TYPE: boolean / true if number above 3000
		"""
		ind = Candy.texture.index(candySpec['texture']) + Candy.variation.index(candySpec['variation']) * len(Candy.texture) + Candy.color.index(candySpec['color']) * len(Candy.texture) * len(Candy.variation) + Candy.name.index(candySpec['name']) * len(Candy.texture) * len(Candy.variation) * len(Candy.name)
		return (lambda x: x > 3000 )(self.candies[ind].getNumber())


	def getStockCandy():
		"""get list of candy with their number 
		
		Returns:
		    TYPE: list of string : string 
		    + string : int
		"""
		stockCandy = []
		for item in self.candies:
			candyInStock = item.getCandy()
			candyInStock['number'] = item.getNumber()
			stockCandy.append(candyInStock)
		return stockCandy

	def randomize():
		"""Modify number of candy
		Each time called increase the number of 4 different candy
		until all candy has been increased once then redo 
		Then decrease the number of a candy 15 times in 'random' mode
		or decrease the number of one the chosen candy 25 times in 'critic' mode
		"""
		done = []
		for item in self.candies:
			if(item.added):
				continue
			if(item.getCandy()['variation'] in done):
				if(item.getCandy()['variation'] == 'Acide' or (item.getCandy()['variation'] != 'Acide' and done.count(item.getCandy()['variation'])<2)):
					continue
			item.addNumber()
			done.append(item.getCandy()['variation'])
			item.added = True
			if(len(done) >= 4):
				break
		if(len(done)==0):
			for item in self.candies:
				item.added = False
		if(self.mode=='random'):
			for i in range(15):
				self.candies[randint(0,len(self.candies))].decreaseNumber()
		if(self.mode=='critic'):
			for i in range(25)
				self.candies[sample(self.chosenCritic, 1)[0]].decreaseNumber()

	def randomMode():
		"""set mode to 'random'
		"""
		self.mode = 'random'

	def criticMode():
		"""set mode to 'critic'
		randomly choose 3 candy to decrease in priority
		"""
		self.mode = 'critic'
		self.chosenCritic = []
		self.chosenCritic.append(randint(0, len(self.candies)))
		self.chosenCritic.append(randint(0, len(self.candies)))
		self.chosenCritic.append(randint(0, len(self.candies)))

