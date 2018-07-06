from random import * 


class MaterialStock():

	def __init__(self):
		self.additif = 1200000
		self.arome = 1200000
		self.enrobage = 1200000
		self.gelifiant = 1000000
		self.sucre = 1000000


	def getStockMaterial(): 
		return {'additif': self.additif, 'arome': self.arome, 'enrobage': self.enrobage, 'gelifiant': self.gelifiant, 'sucre': self.sucre}


	def addMaterial():
		self.additif = 1200000
		self.arome = 1200000
		self.enrobage = 1200000
		self.gelifiant = 1000000
		self.sucre = 1000000

	def addNumber():
		self.additif += 5000
		self.arome += 4000
		self.enrobage += 4000
		self.gelifiant += 20000
		self.sucre += 20000

	def reduceNumber():
		self.additif -= randint(1, 10)
		self.arome -= randint(1, 10)
		self.enrobage -= randint(1, 10)
		self.gelifiant -= randint(1, 10)
		self.sucre -= randint(1, 10)

	def randomize():
		if((lambda x: x==0)(randint(0,2)))
			self.addNumber()
		if(self.mode == 'random'):
			for i in range(randint(500, 3000)):
				self.reduceNumber()
		if(self.mode == 'critic'):
			for i in range(3000):
				self.reduceNumber()
		if(self.additif <= 0 || self.arome <= 0 || self.enrobage <= 0 || self.gelifiant <= 0 || self.sucre <= 0):
			self.addMaterial()

	def randomMode():
		self.mode = 'random'

	def criticMode():
		self.mode = 'critic'
		



