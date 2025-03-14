class Animal: 
    def __init__(self, name, species):
        self.name = name
        self.species = species 
        
    def make_sound(self): #gets overriden 
        return "Generic animal sound"
        
    def info(self):
        return f"{self.name} is a {self.species} and makes a {self.make_sound()} sound."
        
class Bear(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color 
        
    def make_sound(self):
        return "roar"
        
    def info(self):
        return f"{self.name} is a bear of the {self.species} species with {self.fur_color} fur! It makes a {self.make_sound} sound."
        
class Elephant(Animal):
    def __init__(self, name, species, weight):
        super().__init__(name, species)
        self.weight = weight
        
    def make_sound(self):
        return "trumpet"
        
    def info(self):
        return f"{self.name} is an elephant of the {self.species} species that weighs {self.weight} kg! It makes a {self.make_sound} sound."
class Penguin(Animal):
    def __init__(self, name, species, height):
        super().__init__(name, species)
        self.height = height 
        
    def make_sound(self):
        return "squawk"
        
    def info(self):
        return f"{self.name} is a penguin of the {self.species} species and has a height of {self.height} feet! It makes a {self.make_sound} sound."
        
def main():
    zoo = [] #holds all animals 
    
    while True: 
        print("\n--------Zoo Menu--------") #formatting
        print("1: Add Animals ")
        print("2: Print All")
        print("3: Print Specific")
        print("4: Exit")
        print("------------------------")
        
        choice = input("Please choose an option from the menu above: ")
        
        if choice == "1":
            print("\n--------Add Menu--------")
            print("1. Add Bear")
            print("2. Add Elephant")
            print("3. Add Penguin")
            print("------------------------")
            
            animal_choice = input("Please choose an option from the menu above: ")
            
            name = input("Enter the animal name: ")
            species = input("Enter the animal species: ")
            
            if animal_choice == "1":
                fur_color = input("Please enter the fur color: ")
                zoo.append(Bear(name, species, fur_color))
                
            elif animal_choice == "2":
                weight = float(input("Please enter weight (in kg): "))
                zoo.append(Elephant(name, species, weight))
            
            elif animal_choice == "3":
                height = float(input("Please enter height (in ft): "))
                zoo.append(Penguin(name, species, height))
                
        elif choice == "2":
            for animal in zoo:
                print(animal.info())
                
        elif choice == "3":
            print("\n--------Print Menu--------")
            print("1: Print Bear")
            print("2: Print Elephant")
            print("3: Print Penguin")
            print("--------------------------")
            
            specific_choice = input("Please enter choice from menu above: ")

            for animal in zoo:
                if specific_choice == "1" and isinstance(animal, Bear):
                    print(animal.info())
                elif specific_choice == "2" and isinstance(animal, Elephant):
                    print(animal.info())
                elif specific_choice == "3" and isinstance(animal, Penguin):
                    print(animal.info())

        elif choice == "4":
            break
                    
if __name__ == '__main__':
    main()
