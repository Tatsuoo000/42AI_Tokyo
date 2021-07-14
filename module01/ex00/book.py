from datetime import datetime

class Book:
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.now
		self.creation_date = datetime.now
		self.recipes_list = {
			'starter': [],
			'lunch': [],
			'dessert': []
		}
		pass

	def get_recipe_by_name(self, name):
		for x in ['starter', 'lunch', 'dessert']:
			for n in self.recipes_list[x]:
				if (n.name == name):
					print(n.name)
					return (n)
		pass

	def get_recipes_by_types(self, recipe_type):
		for i in self.recipes_list[recipe_type]:
			print(i.name)
		pass

	def add_recipe(self, recipe):
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = datetime.now
		pass