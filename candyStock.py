from random import *
from candy import Candy

class CandyStock():

	def __init__(self):

		self.mode = 'random'
		self.candies = []
		self.chosenCritic = []
		for name in Candy.name:
			for color in Candy.color:
				for variation in Candy.variation:
					for texture in Candy.texture:
						self.candies.append(Candy(name, color, variation, texture))

	def checkStockCandy(candySpec):
		ind = Candy.texture.index(candySpec['texture']) + Candy.variation.index(candySpec['variation']) * len(Candy.texture) + Candy.color.index(candySpec['color']) * len(Candy.texture) * len(Candy.variation) + Candy.name.index(candySpec['name']) * len(Candy.texture) * len(Candy.variation) * len(Candy.name)
		return (lambda x: x < 3000 )(self.candies[ind].getNumber())


	def getStockCandy():
		stockCandy = []
		for item in self.candies:
			candyInStock = item.getCandy()
			candyInStock['number'] = item.getNumber()
			stockCandy.add(candyInStock)
		return stockCandy

	def randomize():
		
		done = []
		for item in self.candies:
			if(item.added):
				continue
			if(item.getCandy()['variation'] in done):
				continue
			item.addNumber()
			done.add(item.getCandy()['variation'])
			item.added = True
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
		self.mode = 'random'

	def criticMode():
		self.mode = 'critic'
		self.chosenCritic = []
		self.chosenCritic.add(randint(0, len(self.candies)))
		self.chosenCritic.add(randint(0, len(self.candies)))
		self.chosenCritic.add(randint(0, len(self.candies)))

