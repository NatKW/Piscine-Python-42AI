class GotCharacter(object):

    """ A class to represent GoT Characters. """

    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.isalive = is_alive

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

class Stark(GotCharacter):

    """ A class representing the Stark family. Or when bad things happen to good people. """
        
    def __init__(self, first_name=None, is_alive=True):
        super(Stark, self).__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

class Lannister(GotCharacter):

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar!"

if __name__ == "__main__":
        arya = Stark("Arya")
        print(arya.__dict__)
        arya.print_house_words()
        print(arya.isalive)
        arya.die()
        print(arya.isalive)
        print(arya.__doc__)
        cersei = Lannister("Cersei")
        print(cersei.__dict__)
        cersei.print_house_words()
        print(cersei.isalive)
        cersei.die()
        print(cersei.isalive)
        print(cersei.__doc__)
        print(GotCharacter.__doc__)
