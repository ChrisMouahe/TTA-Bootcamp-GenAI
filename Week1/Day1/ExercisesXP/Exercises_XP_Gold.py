# # Exercise 1: What is the Season?

# # 1. Ask the user to input a month (1 to 12).
# # 2. Display the season of the month received:
      # # - Spring runs from March (3) to May (5)
      # # - Summer runs from June (6) to August (8)
      # # - Autumn runs from September (9) to November (11)
      # # - Winter runs from December (12) to February (2)

month = int(input("Type a month number please from 1 to 12 : "))
if month >= 3 and month <=5 :
      print("The season of the month recieved is Spring. ")
elif month >=6 and month <= 8 :
      print("The season of the month recieved is Summer. ")
elif month >=9 and month <= 11 :
      print("The season of the month recieved is Autumn. ")
elif month == 12 or month <=2 :
      print("The season of the month recieved is Winter. ")


# # Exercise 2: For Loop

# # Key Python Topics:

# # Loops (for)
# # Range and indexing

# # Instructions:

# # Write a for loop to print all numbers from 1 to 20, inclusive. 
# # Write another for loop that prints every number from 1 to 20 where the index is even.

liste = []
for i in range(20) :
      liste.append(i + 1)
print(liste)
j = 1
indice = 0
for numb in liste :
      indice = get_index(liste, liste[j])
      if indice % 2 == 0 :
            print(numb)
