from random import *
from randomized import Randomized as ran

class CandyOrder(ran):

	def __init__(ran):
		ran.name = ['Acidofilo', 'Bouteille cola', 'Brazil pik', 'Color Schtroummpf pik', 'Langues acides', 'London pik', 'Miami pik', 'Pasta Basta', 'Pasta frutta', 'Sour snup', 'Dragibus', 'Carensac', 'Fraizibus', 'Grain de millet', 'Starmint', 'Florent violette', 'Kimono', 'Pain Zan', 'Rotella', 'Zanoïd', 'Fraise tagada', 'Croco', 'Chamallows', 'Polka', 'Banane', 'Ourson', 'Filament']
		ran.color = ['Rouge', 'Orange', 'Jaune', 'Vert', 'Bleu', 'Violet', 'Noir', 'Marron']
		ran.variation = ['Acide', 'Sucré', 'Gélifié']
		ran.texture = ['Mou', 'Dur']
		ran.instance = {'name': 'Acidofilo', 'color': 'Rouge', 'variation': "Acide", 'texture': "Mou"}
		ran.nameRandRange = {'Echantillon': 1, 'Sachet': 1, 'Boite': 1}
		ran.colorRandRange = {'Echantillon': 1, 'Sachet': 1, 'Boite': 1}
		ran.variationRandRange = {'Echantillon': 1, 'Sachet': 1, 'Boite': 1}
		ran.textureRandRange = {'Mou': 1, 'Dur': 1}

	def getData(ran):
		return ran.instance


	def randomize(ran):
		ran.instance['name'] = sample(ran.name, 1)[0]
		ran.instance['color'] = sample(ran.color, 1)[0]
		ran.instance['variation'] = sample(ran.variation, 1)[0]
		ran.instance['texture'] = sample(ran.texture, 1)[0]

	def randomMode(ran):
		for do in ran.nameRandRange:
			ran.nameRandRange[do] = 1
		for do in ran.colorRandRange:
			ran.colorRandRange[do] = 1
		for do in ran.variationRandRange:
			ran.variationRandRange[do] = 1
		for do in ran.textureRandRange:
			ran.textureRandRange[do] = 1

	def criticMode(ran, toFocus=0):
		if(toFocus==0):
			toFocusName = sample(ran.name, 3)
			toFocusColor = sample(ran.color, 2)
			toFocusVariation = sample(ran.variation, 1)
			toFocusTexture = sample(ran.texture, 1)
			toFocus = {}
		else:
			toFocusName = toFocus['name']
			toFocusColor = toFocus['color']
			toFocusVariation = toFocus['variation']
			toFocusTexture = toFocus['texture']
		print(toFocusName)
		print(toFocusColor)
		print(toFocusVariation)
		print(toFocusTexture)
		for do in toFocusName:
			ran.nameRandRange[do] = 50
		for do in toFocusColor:
			ran.colorRandRange[do] = 10
		for do in toFocusVariation:
			ran.variationRandRange[do] = 10
		for do in toFocusTexture:
			ran.textureRandRange[do] = 10
		toFocus['name'] = toFocusName
		toFocus['color'] = toFocusColor
		toFocus['variation'] = toFocusVariation
		toFocus['texture'] = toFocusTexture
		return toFocus



	def changeMode(ran, mode):
		switcher = {'random': ran.randomMode, 'critic': ran.criticMode}
		func = switcher.get(mode, lambda: 'invalid mode')
		func()
