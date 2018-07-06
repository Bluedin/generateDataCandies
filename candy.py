from random import *

class Candy:

	self.name = ['Acidofilo', 'Bouteille cola', 'Brazil pik', 'Color Schtroummpf pik', 'Langues acides', 'London pik', 'Miami pik', 'Pasta Basta', 'Pasta frutta', 'Sour snup', 'Dragibus', 'Carensac', 'Fraizibus', 'Grain de millet', 'Starmint', 'Florent violette', 'Kimono', 'Pain Zan', 'Rotella', 'Zanoïd', 'Fraise tagada', 'Croco', 'Chamallows', 'Polka', 'Banane', 'Ourson', 'Filament']
	self.color = ['Rouge', 'Orange', 'Jaune', 'Vert', 'Bleu', 'Violet', 'Noir', 'Marron']
	self.variation = ['Acide', 'Sucré', 'Gélifié']
	self.texture = ['Mou', 'Dur']

	def __init__(self, name, color, variation, texture):
		self.name = name
		self.color = color
		self.variation = variation
		self.texture = texture
		self.number = 3000
		self.added = False


	def getNumber():
		return self.number

	def getCandy():
		candySpec = {'name': self.name, 'color': self.color, 'variation': self.variation, 'texture': self.texture}
		return candySpec

	def addNumber():
		addNumberByVariation = {'Acide': 750, 'Sucré': 1230, 'Gélifié': 625}
		self.number += randint(addNumberByVariation[self.variation])

	def decreaseNumber():
		self.number -= randint(1, 25)


