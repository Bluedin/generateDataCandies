from random import *
from randomized import Randomized as ran

class Candy(ran):

	def __init__(ran):
		ran.name = ['Acidofilo', 'Bouteille cola', 'Brazil pik', 'Color Schtroummpf pik', 'Langues acides', 'London pik', 'Miami pik', 'Pasta Basta', 'Pasta frutta', 'Sour snup', 'Dragibus', 'Carensac', 'Fraizibus', 'Grain de millet', 'Starmint', 'Florent violette', 'Kimono', 'Pain Zan', 'Rotella', 'Zanoïd', 'Fraise tagada', 'Croco', 'Chamallows', 'Polka', 'Banane', 'Ourson', 'Filament']
		ran.color = ['Rouge', 'Orange', 'Jaune', 'Vert', 'Bleu', 'Violet', 'Noir', 'Marron']
		ran.variation = ['Acide', 'Sucré', 'Gélifié']
		ran.texture = ['Mou', 'Dur']
		ran.instance = {'name': 'Acidofilo', 'color': 'Rouge', 'variation': "Acide", 'texture': "Mou"}

	def getData(ran):
		return ran.instance


	def randomize(ran):
		ran.instance['name'] = sample(ran.name, 1)[0]
		ran.instance['color'] = sample(ran.color, 1)[0]
		ran.instance['variation'] = sample(ran.variation, 1)[0]
		ran.instance['texture'] = sample(ran.texture, 1)[0]


