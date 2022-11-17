class Recipe:
    
    def __init__(self, name, cooking_lvl, cooking_time, 
    ingredients, recipe_type, description=""):
        try:
            self.name = str(name)
            if len(name) == 0:
                raise Exception("Recipe name can't be empty!")
            self.cooking_lvl = int(cooking_lvl)
            if not int(cooking_lvl) in range(1, 5):
                    raise Exception("Cooking level must be in range 1 to 5")
            self.cooking_time = int(cooking_time)
            if int(cooking_time) < 0:
                raise Exception("Cooking time can't be negative")
            self.ingredients = list(ingredients)
            if len(ingredients) == 0:
                raise Exception("You need ingredients to cook!")
            self.recipe_type = str(recipe_type)
            if recipe_type not in ["starter", "lunch", "dessert"]:
                raise Exception("Recipe must be either a starter, a lunch or a dessert")
            self.description = str(description)
        except(Exception, ValueError) as e:
            print("An Exception was raised: ", e)
            exit()

    def __str__(self):

        """ Return the string to print with the recipe info """

        txt = "\nRecipe for " + (self.name) + ":\n\n"
        txt += "- Ingredients list:\n"
        txt += ", ".join(self.ingredients) + "\n"
        txt += "- Cooking time: " + str(self.cooking_time) + " minutes\n"
        txt += "- Level of difficulty: " + str(self.cooking_lvl)+ " out of 5\n"
        txt += "To be eaten for " + (self.recipe_type) + "\n"
        if len(self.description) != 0:
            txt += (self.description)+ "\n"
        return txt
        

#if __name__ == '__main__':
#
#    tourte = recipe('Tourte', 3, 45, ["flour", "butter", "eggs", "stuffing", "sauce"], "lunch", "typical english meal!") 
#    to_print = str(tourte) 
#    print(to_print)

#    mousse = Recipe('Mousse', 2, 15, ["chocolate", "eggs", "sugar"], "dessert") 
#    to_print = str(mousse) 
#    print(to_print)
""" exceptions """
#    tourte = recipe('veggies\' tourte', 3, -45, ["flour", "butter", "eggs", "veggies", "sauce"], "lunch", "typical english meal!") 
#    to_print = str(tourte) 
#    print(to_print)
#    mousse = Recipe('Mousse', 6, 15, ["chocolate", "eggs", "sugar"], "dessert") 
#    to_print = str(mousse)
#    mousse = Recipe('Mousse', 2, 15, ["chocolate", "eggs", "sugar"], "snack") 
#    to_print = str(mousse) 
