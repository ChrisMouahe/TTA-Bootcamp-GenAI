# # Bonus: Expand The Farm

# # Step 6: Implement the get_animal_types Method

# # Add a method called get_animal_types to the class Farm.
# # This method should return a sorted list of all animal types (animals keys from the dictionary). 
# # Use the function to sort the list.sorted()

# # Step 7: Implement the get_short_info Method

# # Add a method called class get_short_info to the Farm.
# # This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
# # Call the method get_animal_types to get the list of animals.
# # Construct the string, adding an “s” to the animal name if its count is greater than 1.
# # Use string formatting to create the output.

# # Step 8: upgrade the add_animal Method

# # use for **kwargs passing multiple animals. The keys will be the animal name and the value will be the quantity.
# # Then you can call the method this way: macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)



# Creation of Farm class
class Farm() :
      def __init__(self, Farm_name):
            self.Farm_name = Farm_name
            self.animals = {}

# creation of add_animals method
      def add_animals(self, animal_type, count=1) :
            if animal_type in self.animals :
                  self.animals[animal_type] += count
            else :
                  self.animals[animal_type] = count

# Création of get_info method
      def get_info(self):
            info = f"the Farm is {self.Farm_name}\n\n"

            for animal_type, count in self.animals.items() :
                  info += f"{animal_type:<8} : {count} \n"

            info += f"\nE-I-E-I-0"
            return info
# creation of a magic method for print clearly the value of Farm
      def __str__(self) :
            return f"{self.Farm_name}"

# # Implement the get_animal_types Method 
      def get_animal_types(self) :
            get_type = sorted(self.animals.keys())
            return get_type

# Implement the get_short_info Method
      def get_short_info(self) :
            infos = f"{self.Farm_name}'s farm has "

            # verifying which animal_type takes s or not
            for animal_type, count in self.animals.items() :
                  if count == 1 :
                        infos += f"{animal_type} "
                  elif count > 1 :
                        infos += f"{animal_type}s "

            infos +="."

            return infos

# upgrade the add_animal Method
      def add_animal(self, **kwargs):
            print(kwargs.items())
            

# Test of the code
macdonald = Farm("McDonald")
macdonald.add_animals('cow', 5)
macdonald.add_animals('sheep')
macdonald.add_animals('sheep')
macdonald.add_animals('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
macdonald.add_animal(cow=5, sheep=2, goat=12)
