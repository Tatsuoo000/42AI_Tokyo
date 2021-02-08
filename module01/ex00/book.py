import time

class Book:
	def __init__(self, name):
		self.name = name
		self.last_update = time.now
		self.creation_date = time.now
		self.recipes_list = {
			'starter': [],
			'lunch': [],
			'dessert': []
		}
		pass
