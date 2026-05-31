# # Exercise 1: Converting Lists into Dictionaries
# # Key Python Topics:

# # Creating dictionaries
# # Zip function or dictionary comprehension

# # Instructions

# # You are given two lists. 
# # Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

# # Lists:

# # keys = ['Ten', 'Twenty', 'Thirty']
# # values = [10, 20, 30]

# # Expected Output:

# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

diction = dict(zip(keys, values))
print(diction)


# # Exercise 2: Cinemax #2
# # Key Python Topics:

# # Looping through dictionaries
# # Conditionals
# # Calculations

# # Instructions

# # Write a program that calculates the total cost of movie tickets for a family based on their ages.

# # Family members’ ages are stored in a dictionary.
# # The ticket pricing rules are as follows:
# # Under 3 years old: Free
# # 3 to 12 years old: $10
# # Over 12 years old: $15

# # Family Data:

# # family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# # Loop through the dictionary to calculate the total cost.family
# # Print the ticket price for each family member.
# # Print the total cost at the end.


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price = []
total = 0
for key, value in family.items():
      if value < 3 :
            print ('The ticket of ', key, ' is free.')
            price.append(0)
      elif value >= 3 and value <= 12 :
            print ('The ticket price of ',key, ' is 10$.' )
            price.append(10)
      else :
            print ('The ticket price of ',key, ' is 15$')
            price.append(15)
total = sum(price)
print(price, '\nThe total ticket cost is ',total,'$.')


# # Bonus:

# # Allow the user to input family members’ names and ages, then calculate the total ticket cost.

reponse = ""
liste_nom = []
liste_age = []
while reponse.lower() != "no" :
      liste_nom.append(input('Type the name of the family member : '))
      liste_age.append(int(input('Type the age of this person : ')))
      reponse = (input('would add another member ? (YES or NO) : '))
print(liste_nom,'\n',liste_age)

memb_dict = dict(zip(liste_nom, liste_age))
print(memb_dict)
price = []
total = 0
for key, value in memb_dict.items():
      if value < 3 :
            print ('The ticket of ', key, ' is free.')
            price.append(0)
      elif value >= 3 and value < 12 :
            print ('The ticket price of ',key, ' is 10$.' )
            price.append(10)
      else :
            print ('The ticket price of ',key, ' is 15$')
            price.append(15)
      total = sum(price)
print(price, '\nThe total ticket cost is ',total,'$.')


# # Exercise 3: Zara
# # Key Python Topics:

# # Creating dictionaries
# # Accessing and modifying dictionary elements
# # Dictionary methods like .pop() and .update()

# # Instructions

# # Create and manipulate a dictionary that contains information about the Zara brand.

# # Brand Information:

# # name: Zara
# # creation_date: 1975
# # creator_name: Amancio Ortega Gaona
# # type_of_clothes: men, women, children, home
# # international_competitors: Gap, H&M, Benetton
# # number_stores: 7000
# # major_color: 
    # # France: blue, 
    # # Spain: red, 
    # # US: pink, green

# # Create a dictionary called brand with the provided data.
# # Modify and access the dictionary as follows:
# # Change the value of number_stores to 2.
# # Print a sentence describing Zara’s clients type_of_clothes using the key.
# # Add a new key country_creation with the value Spain.
# # Check if international_competitors exists and, if so, add “Desigual” to the list.
# # Delete the key creation_date.
# # Print the last item in international_competitors.
# # Print the major colors in the US.
# # Print the number of keys in the dictionary.
# # Print all keys of the dictionary.


# # Bonus:

# # Create another dictionary called more_on_zara with creation_date and number_stores. 
# # Merge this dictionary with the original dictionary brand and print the result. 


brand = {
      "name": "Zara", 
      'creation_date': 1975,
      'creator_name': "Amancio Ortega Gaona",
      'type_of_clothes': ['men', 'women', 'children', 'home'],
      'international_competitors': ['Gap', 'H&M', 'Benetton'],
      'number_stores': 7000,
      'major_color': {
            'France': 'blue', 
            'Spain': 'red', 
            'US': ['pink', 'green']
            }
}
brand['number_stores'] = 2
print('Zara provides clothes for ',brand['type_of_clothes'][0],',',brand['type_of_clothes'][1],'and',brand['type_of_clothes'][2],'. Feel as at ',brand['type_of_clothes'][3])
brand['country_creation'] = ['Spain']
if brand['international_competitors'] :
      brand['international_competitors'].append('Desigual')
del brand['creation_date']
print(brand['international_competitors'][len(brand['international_competitors']) - 1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())

# # Bonus:

# # Create another dictionary called more_on_zara with creation_date and number_stores. 
# # Merge this dictionary with the original dictionary brand and print the result. 

more_on_zara = {
      'creation_date': 1975,
      'number_stores': 7000,
}
merged = brand | more_on_zara 
print('the merge is : ',merged)


# # Exercise 4 : Some Geography
# # Goal: Create a function that describes a city and its country.

# # Key Python Topics:

# # Functions with multiple parameters
# # Default parameter values
# # String formatting

# # Step 1: Define a Function with Parameters

# # Define a function named describe_city().
# # This function should accept two parameters: city and country.
# # Give the country parameter a default value, such as “Unknown”.

# # Step 2: Print a Message

# # Inside the function, set up the code to display a sentence like “ is in “.
# # Replace and with the parameter values.<city><country>

# # Step 3: Call the Function

# # Call the function describe_city()  with different city and country combinations.
# # Try calling it with and without providing the country argument to see the default value in action.
# # Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").

# # Expected Output:

# # Reykjavik is in Iceland.
# # Paris is in Unknown.

def describe_city(city, country ='unknown') :
      print(city ,'is in', country)
describe_city("bouake", )


# # Exercise 5 : Random
# # Goal: Create a function that generates random numbers and compares them.

# # Key Python Topics:

# # random module
# # random.randint() function
# # Conditional statements (, ifelse)

# # Step 1: Import the random Module

# # At the beginning of your script, use to access the random number generation functions.import random

# # Step 2: Define a Function with a Parameter

# # Create a function that accepts a number between 1 and 100 as a parameter.

# # Step 3: Generate a Random Number

# # Inside the function, use to generate a random integer between 1 and 100.random.randint(1, 100)

# # Step 4: Compare the Numbers

# # If they are the same, print a success message. Otherwise, print a fail message and display both numbers.

# # Step 5: Call the Function

# # Call the function with a number between 1 and 100.

# # Expected Output:

# # Success! (if the numbers match)
# # Fail! Your number: 50, Random number: 23 (if they don't match)

import random
def random_numb () :
      n = int(input('Type a number : '))
      if not (1 <= n <= 100):
        raise ValueError("Le nombre doit être compris entre 1 et 100 inclus.")
      number = random.randint(1, 100)
      if n == number :
            print('Success!')
      else :
            print('Fail! Your number: ',n, 'Random number: ',number)
random_numb()


# # Exercise 6 : Let’s create some personalized shirts !
# # Goal: Create a function to describe a shirt’s size and message, with default values.

# # Key Python Topics:

# # Functions with parameters and default values
# # Keyword arguments

# # Step 1: Define a Function with Parameters

# # Define a function called .make_shirt()
# # This function should accept two parameters: and .sizetext

# # Step 2: Print a Summary Message

# # Set up the function to display a sentence summarizing the shirt’s size and message.

# # Step 3: Call the Function

# # Step 4: Modify the Function with Default Values

# # Modify the function make_shirt() so that size has a default value of “large” and text has a default value of “I love Python”.

# # Step 5: Call the Function with Default and Custom Values

# # Call make_shirt() to make a large shirt with the default message.
# # Call make_shirt() to make a medium shirt with the default message.
# # Call make_shirt() to make a shirt of any size with a different message.

def make_shirt(size = "large", text ='I love python') :
      print("The size of the shirt is ",size, " and the text is ", text)
make_shirt()
make_shirt("medium",)
make_shirt("anysize","That's cool")

# # Step 6 (Bonus): Keyword Arguments

# # Call make_shirt() using keyword arguments (e.g., ).make_shirt(size="small", text="Hello!")

# # Expected Output:

# # The size of the shirt is large and the text is I love Python.
# # The size of the shirt is medium and the text is I love Python.
# # The size of the shirt is small and the text is Custom message.

def make_shirt(**kvars) :
     for key, value in kvars.items() :
            if key =="size" :
                  print("The size of the shirt is",value, end="")
            else :
                  print(" and the text is ",value)
make_shirt(size="large", text="I love Python")
make_shirt(size="medium", text="I love Python")
make_shirt(size="small", text="custome message")



