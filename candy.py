from random import *

class Candy:

	"""Candy
	
	Attributes:
	    added (bool): if the number of candy has been increased in candyStock; reset when all candy has been increased once
	    color (list): color of candy
	    name (list): name of candy
	    number (int): number of candy
	    texture (list): texture of candy
	    variation (list): variation of candy
	"""
	
	self.name = ['Acidofilo', 'Bouteille cola', 'Brazil pik', 'Color Schtroummpf pik', 'Langues acides', 'London pik', 'Miami pik', 'Pasta Basta', 'Pasta frutta', 'Sour snup', 'Dragibus', 'Carensac', 'Fraizibus', 'Grain de millet', 'Starmint', 'Florent violette', 'Kimono', 'Pain Zan', 'Rotella', 'Zanoïd', 'Fraise tagada', 'Croco', 'Chamallows', 'Polka', 'Banane', 'Ourson', 'Filament']
	self.color = ['Rouge', 'Orange', 'Jaune', 'Vert', 'Bleu', 'Violet', 'Noir', 'Marron']
	self.variation = ['Acide', 'Sucré', 'Gélifié']
	self.texture = ['Mou', 'Dur']

	def __init__(self, name, color, variation, texture):
		"""initialize candy with value input
		
		Args:
		    name (TYPE): name of candy
		    color (TYPE): color of candy
		    variation (TYPE): variation of candy
		    texture (TYPE): texture of candy
		"""
		self.name = name
		self.color = color
		self.variation = variation
		self.texture = texture
		self.number = 3000
		self.added = False


	def getNumber():
		"""get number of candy
		
		Returns:
		    TYPE: int
		"""
		return self.number

	def getCandy():
		"""get caracteristic of candy
		
		Returns:
		    TYPE: list
		"""
		candySpec = {'name': self.name, 'color': self.color, 'variation': self.variation, 'texture': self.texture}
		return candySpec

	def addNumber():
		"""increase number of candy based on variation
		"""
		addNumberByVariation = {'Acide': 750, 'Sucré': 1230, 'Gélifié': 625}
		self.number += randint(addNumberByVariation[self.variation])

	def decreaseNumber():
		"""decrease number of candy randomly between 1 and 25
		"""
		self.number -= randint(1, 25)


