from random import randint


if __name__ == "__main__":

    print('This is an interactive guessing game!\nYou have to enter a number between 1 & 99 to find out the secret number.\nType \'exit\' to end the game.\nGood Luck!\n')
    num_to_guess = randint(1, 99)
    print('Nombre =', num_to_guess)
    choice = input("What's your guess between 1 and 99?\n")
    count = 0
    while (int(choice) == num_to_guess):
        if choice == "exit":
            exit('Goodbye!')
        count =+ 1  
        if choice.isdigit() == False:
            exit('That\'s not a number.')
        elif int(choice) == 42:
            print("The answer to the ultimate question of life, "
				+ "the universe and everything is 42.")
            print("Congratulations! You got it on your first try!")
            exit()
        elif int(choice) == num_to_guess:
            print("Congratulations, you've got it!")
            print("You won in", count, "attemps!")
            exit()
        elif int(choice) > num_to_guess:
            print("Too high!")
        else:
            print("Too low!")

