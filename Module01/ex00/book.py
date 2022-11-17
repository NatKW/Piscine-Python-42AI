from recipe import Recipe
from datetime import datetime

class Book:

    def __init__(self, name):
        self.name = str(name)
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipe_list = {"starter":[], "lunch":[], "dessert":[]}

    def add_recipe(self, recipe):

        """ Add a recipe to the book and update last_update """
        
        if not isinstance(recipe, Recipe):
            print("Invalid recipe")
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    def get_recipe_by_name(self, name):

        """ Prints a recipe with the name \texttt{name} and returns the instance """
        
        for recipes in self.recipe_list.values():
            for recipe in recipes:
                if recipe.name == name:
                    return recipe
        print("recipe not found in cookbook...")
    
    def get_recipes_by_type(self, recipe_type):

        """ Get all recipe names for a given type """
        
        if recipe_type in self.recipe_list.keys():
            list_by_type = [recipe.name for recipe in self.recipe_list[recipe_type]]
            return list_by_type
        print("Only starter, lunch or dessert in this cookbook")
        return