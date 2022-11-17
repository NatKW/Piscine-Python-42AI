from recipe import Recipe
from book import Book
from time import sleep

if __name__ == "__main__":

    my_cookbook = Book("My Cookbook")

    tourte = Recipe('Tourte', 3, 45, ["flour", "butter", "eggs", "stuffing"], "lunch", "typical english meal!") 
    my_cookbook.add_recipe(tourte)

    mousse = Recipe('Mousse', 1, 15, ["chocolate", "eggs", "sugar"], "dessert") 
    my_cookbook.add_recipe(mousse)

    salad = Recipe('Caesar Salad', 2, 15, ["lettuce", "eggs", "croutons", "cheese", "anchovy sauce"], "lunch")
    my_cookbook.add_recipe(salad)

    print(my_cookbook.name)
    print("was last update : ", my_cookbook.last_update)
    print("was created: ", my_cookbook.creation_date)
    print("______________________________\n")
    print("Get a recipe by its name(mousse) : \n" + str(my_cookbook.get_recipe_by_name("Mousse")))
    print("______________________________\n")
    print("Get a recipe by its name(salad) : \n" + str(my_cookbook.get_recipe_by_name("Caesar Salad")))
    print("______________________________\n")
    print("Get a list of recipes by type(lunch) : " + str(my_cookbook.get_recipes_by_type("lunch")))
    print("Get a list of recipes by type(dessert) : " + str(my_cookbook.get_recipes_by_type("dessert")))