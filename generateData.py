from random import *
from client import Client
from order import Order
from CAD import CAD
from candyStock import CandyStock
from materialStock import MaterialStock
import time

#client = Client()
#client.randomize()
#for instance in client.getData():
#	print instance
#print(client.getData())

cad = CAD()


order = Order()
order.randomize()
cad.sendData(order.getData(), 'order')

candyStock = CandyStock()
candyStock.randomize()
cad.sendData(candyStock.getData(), 'stockCandy')

materialStock = MaterialStock()
materialStock.randomize()
cad.sendData(materialStock.getData(), 'stockMaterial')



#for i in range(30):
	#order.randomize()
	#print(order.getData())
	#print('#####')
	#print('#####')
	#print('#####')²
#print('################################################################')
#print('################################################################')
#print('################################################################')
#print('################################################################')
#print('################################################################')
#print('################################################################')
#order.changeMode('random')
#for i in range(30):
	#order.randomize()
	#print(order.getData())
	#print('#####')
	#print('#####')
	#print('#####')
