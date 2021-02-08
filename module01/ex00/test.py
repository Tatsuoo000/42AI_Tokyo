from book import Book
from recipe import Recipe

cake = Recipe('cake', 2, 1, ['apple', 'bake'], 'startera')
print(cake.name)

tourte = Recipe("tourte", 1, 5, ['apple', 'bagle'], 'starter')
tourte.description = "abctest"
to_print = str(tourte)
print(to_print)