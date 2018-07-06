"""Summary
"""
from random import * 


class MaterialStock():

	"""stock of material
	
	Attributes:
	    additif (int): number of additif
	    arome (int): number of arome
	    enrobage (int): number of enrobage
	    gelifiant (int): number of gelifiant
	    mode (str): mode either 'random' or 'critical'
	    sucre (int): number of sucre
	"""
	
	def __init__(self):
		"""initiate material number to base value
		"""
		self.additif = 1200000
		self.arome = 1200000
		self.enrobage = 1200000
		self.gelifiant = 1000000
		self.sucre = 1000000


	def getStockMaterial(): 
		"""get list of material with number
		
		Returns:
		    list: material and number of material pair
		"""
		return {'additif': self.additif, 'arome': self.arome, 'enrobage': self.enrobage, 'gelifiant': self.gelifiant, 'sucre': self.sucre}


	def addMaterial():
		"""set stock of material to base value (emergency stocking)
		could be used to send alert(evolution)
		"""
		self.additif = 1200000
		self.arome = 1200000
		self.enrobage = 1200000
		self.gelifiant = 1000000
		self.sucre = 1000000

	def addNumber():
		"""increase stock of material by set value
		"""
		self.additif += 5000
		self.arome += 4000
		self.enrobage += 4000
		self.gelifiant += 20000
		self.sucre += 20000

	def reduceNumber():
		"""reduce stock of material randomly between 1 and 10 for each material
		"""
		self.additif -= randint(1, 10)
		self.arome -= randint(1, 10)
		self.enrobage -= randint(1, 10)
		self.gelifiant -= randint(1, 10)
		self.sucre -= randint(1, 10)

	def randomize():
		"""randomize data in materialStock
		randomly increase or decrease stock of material
		"""
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
		"""set mode to 'random'
		"""
		self.mode = 'random'

	def criticMode():
		"""set mode to 'critic'
		"""
		self.mode = 'critic'
		



