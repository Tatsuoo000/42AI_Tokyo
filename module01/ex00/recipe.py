import typing as tp

class Recipe:
	# name = ""
	# cooking_lvl = 1
	# cooking_time= 0
	# ingredients = []
	# description = ""
	# recipe_type = ""

	def __init__(self, name:str, cooking_lvl:int, cooking_time:int, ingredients:list,  recipe_type:str):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = ""
		self.recipe_type = recipe_type
		if not type(self.name) is str:
			print("name Error")
			exit()
		if not (type(self.cooking_lvl) is int and (1 <= self.cooking_lvl <= 5)):
			print("cooking_lvl Error")
			exit()
		if not (type(self.cooking_time) is int and self.cooking_time > 0):
			print("cooking_time Error")
			exit()
		if (type(self.ingredients) is list):
			for x in self.ingredients:
				if not type(x) is str:
					print("cooking_time Error")
					exit()
		else:
			print("cooking_time Error")
			exit()
		if not self.recipe_type in ['starter', 'lunch', 'dessert']:
			print("recipe_type Error")
			exit()

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = self.description
		"""Your code goes here"""
		return txt