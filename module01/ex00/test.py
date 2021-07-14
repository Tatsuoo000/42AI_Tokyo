from book import Book
from recipe import Recipe

cake = Recipe('cake', 2, 1, ['apple', 'bake'], 'starter')
print(cake.name)

tourte = Recipe("tourte", 1, 5, ['apple', 'bagle'], 'starter')
tourte.description = "abctest"
to_print = str(tourte)
print(to_print)

book1 = Book('book1')
book1.add_recipe(cake)
book1.get_recipe_by_name('cake')
book1.add_recipe(tourte)
book1.get_recipes_by_types('starter')