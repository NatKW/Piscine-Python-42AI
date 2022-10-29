cookbook = {
		"sandwich" : 
		{
			"ingredients" :	(["ham", "bread", "cheese", "tomatoes"]),
			"meal" : "lunch",
			"prep_time" : "10"
		},
		"cake" : 
		{
			"ingredients" :	(["flour", "sugar", "eggs"]),
			"meal" : "dessert",
			"prep_time" : "60"
		},
		"salad" : 
		{
			"ingredients" :	(["avocado", "arugula", "tomatoes", "spinach"]),
			"meal" : "lunch",
			"prep_time" : "15"
		}
	}

def print_cookbook():
    print("In this cookbook, you'll find recipes for: ")
    for k in cookbook.keys():
        print('-',k)
        
def check_a_recipe():
    print_cookbook()
    recipe = input('Which of theese recipe do you want to see ? ')
    try:
        print(f"\nRecipe for {recipe}:")
        print(f"Ingredients list: {cookbook[recipe]['ingredients']}")
        print(f"To be eaten for {cookbook[recipe]['meal']}.")
        print(f"Takes {cookbook[recipe]['prep_time']} minutes of cooking.\n")
    except KeyError:
        print("\nRecipe not found on the cookbook.\n")

def delete_recipe():
    print_cookbook()
    recipe = input('Which of theese recipe do you want to delete ? ')
    try:
        del cookbook[recipe]
        print(f"\nRecipe {recipe} removed from the cookbook.\n")
    except KeyError:
        print(f"\nRecipe not found on this cookbook.\n")     

def add_recipe(verbose: bool = True):
    recipe = input('Enter a name for your recipe: ')
    t_meal = input('Enter a type of meal: ')
    ingredients = input('Enter ingredients: ')
    time = input('Enter a preparation time: ')
    cookbook[recipe] = {"meal" : t_meal, "prep_time" : time, "ingredients" : ingredients}
    if (verbose):
        print("%s's recipe is added\n" %recipe)

def quit_ft():
    print('\nCookbook closed. Goodbye!\n')

def main():
    choice = 0
    options = {1 : ["Add a recipe", add_recipe],
            2 : ["Delete a recipe", delete_recipe],
            3 : ["Check a recipe", check_a_recipe],
            4 : ["Print the cookbook", print_cookbook], 5 : ["Quit", quit_ft]}

    while (choice != 5):
        print("\nWelcome to the Python Cookbook!")
        print("List of available option:")
        for item in options:
            print("%d : %s" %(item, options[item][0]))
        try:
         choice = int(input("\nPlease select an option ? : "))
        except ValueError:
            choice = 0
        if (choice > 0 and choice < 6):
            options[choice][1]()
        else:
            print("\nSorry this option does not exist.\n")


if __name__ == '__main__':
    main()