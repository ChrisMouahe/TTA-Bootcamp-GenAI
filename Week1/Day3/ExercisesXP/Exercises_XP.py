# # Exercise 1: Cats

# # Instructions:

# # Use the provided class to create three cat objects. Then, create a function to find the oldest cat and print its details.Cat

# # Step 1: Create Cat Objects

# # Use the class to create three cat objects with different names and ages.Cat

# # Step 2: Create a Function to Find the Oldest Cat

# # Create a function that takes the three cat objects as input.
# # Inside the function, compare the ages of the cats to find the oldest one.
# # Return the oldest cat object.

# # Step 3: Print the Oldest Cat’s Details

class Cat() :
      cats = []
      def __init__(self, name, age) :
            self.name = name
            self.age = age
            Cat.cats.append(self)

      # Create a Function to Find the Oldest Cat
      @classmethod
      def oldest_cat(cls) :
            oldest = cls.cats[0]
            for cat in cls.cats :
                  if cat.age > oldest.age :
                        oldest = cat
            return f"The oldest cat is {oldest.name} and it's {oldest.age} years old."
            
      def __str__(self):
            return f"{self.Cat}"

cat1 = Cat("chat",2)
cat2 = Cat("chaton",5)
cat3 = Cat("chacha",4)

print(Cat.oldest_cat())


# # Exercise 2 : Dogs
# # Goal: Create a class, instantiate objects, call methods, and compare dog sizes.Dog

# # Instructions:

# # Create a class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.Dog

# # Step 1: Create the Dog Class

# # Step 2: Create Dog Objects

# # Create and objects with their respective names and heights.davids_dogsarahs_dog

# # Step 3: Print Dog Details and Call Methods

# # Print the name and height of each dog.
# # Call the and methods for each dog.bark()jump()

# # Step 4: Compare Dog Sizes

class Dog():
      def __init__(self, name, height):
            self.name = name
            self.height = height
            print(self)

      def bark(self):
             print(f"{self.name} goes woof!")
      
      def jump(self):
            x = self.height * 2
            print(f"{self.name} jumps {x}cm high!")
      def __str__(self):           
            return f"{self.name:<10} : {self.height}"

davids_dog = Dog('Wafle', 6)
sarahs_dog = Dog("Rex", 9)

davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

maximum = max(davids_dog.height, sarahs_dog.height)
print(f"The biggest is {maximum}cm")


# # Exercise 3 : Who’s the song producer?
# # Goal: Create a class to represent song lyrics and print them.Song

# # Instructions:

# # Create a class with a method to print song lyrics line by line.Song

# # Step 1: Create the Song Class

# # Create a class called .Song
# # In the method, take (a list) as a parameter and create a corresponding attribute.__init__lyrics
# # Create a method that prints each element of the list on a new line.sing_me_a_song()lyrics

class Song():
      def __init__(self, lyrics):
            self.lyrics = lyrics
            lyrics = []

      def sing_me_a_song(self):
            for lyrics in self.lyrics :
                  print(f"{lyrics}")

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()



# # Exercise 4 : Afternoon at the Zoo
# # Goal:

# # Create a class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.Zoo

# # Instructions
# # Step 1: Define the ClassZoo
# # 1. Create a class called .Zoo

# # 2. Implement the method:__init__()

# # It takes a string parameter , representing the name of the zoo.zoo_name
# # Initialize an empty list called to keep track of animal names.animals
# # 3. Add a method :add_animal(new_animal)

# # This method adds a new animal to the list.animals
# # Do not add the animal if it is already in the list.
# # 4. Add a method :get_animals()

# # This method prints all animals currently in the zoo.
# # 5. Add a method :sell_animal(animal_sold)

# # This method checks if a specified animal exists on the animals list and if so, remove from it.
# # 6. Add a method :sort_animals()

# # This method sorts the animals alphabetically.
# # It also groups them by the first letter of their name.
# # The result should be a dictionary where:
# # Each key is a letter.
# # Each value is a list of animals that start with that letter.

# # 7. Add a method :get_groups()

# # This method prints the grouped animals as created by .sort_animals()

# # Step 2: Create a Zoo Object
# # Create an instance of the class and pass a name for the zoo.Zoo

# # Step 3: Call the Zoo Methods
# # Use the methods of your object to test adding, selling, displaying, sorting, and grouping animals.Zoo

# # Bonus: Modify the method to get so you dont need to repeat the method each time for a new animal, 
# # you can pass multiple animals names separated by a comma.add_animal()*args


   class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.groups = {}

    # Add one or multiple animals
    def add_animal(self, *args):
        for new_animal in args:
            if new_animal not in self.animals:
                self.animals.append(new_animal)

    # Display all animals
    def get_animals(self):
        print(f"\nAnimals in {self.zoo_name}:\n")

        for animal in self.animals:
            print(animal)

    # Remove an animal from the zoo
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"\n{animal_sold} has been sold.")
        else:
            print(f"\n{animal_sold} is not in the zoo.")

    # Sort and group animals alphabetically
    def sort_animals(self):
        self.animals.sort()

        grouped = {}

        for animal in self.animals:
            first_letter = animal[0]

            if first_letter not in grouped:
                grouped[first_letter] = []

            grouped[first_letter].append(animal)

        self.groups = grouped

        return grouped

    # Display grouped animals
    def get_groups(self):
        print("\nGrouped Animals:\n")

        for letter, animals in self.groups.items():
            print(f"{letter}: {animals}")


# Create a zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Add animals
brooklyn_safari.add_animal(
    "Giraffe",
    "Bear",
    "Baboon",
    "Lion",
    "Zebra",
    "Cat",
    "Cougar"
)

# Display animals
brooklyn_safari.get_animals()

# Sell an animal
brooklyn_safari.sell_animal("Bear")

# Display animals after selling
brooklyn_safari.get_animals()

# Sort and group animals
brooklyn_safari.sort_animals()

# Display grouped animals
brooklyn_safari.get_groups()
