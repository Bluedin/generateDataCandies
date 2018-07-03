from random import *
from client import Client
from order import Order
import time

client = Client()


client.randomize()
#for instance in client.getData():
#	print instance
print(client.getData())

order = Order()
order.randomize()
print(order.getData())
