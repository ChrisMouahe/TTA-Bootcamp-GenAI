

import random
from game import Game

jeu = Game()

results = {
            "Won": 0,
            "Loss": 0,
            "Draw": 0
            }
def get_user_menu_choice():
      make_choices = [
            '(1): Play a new game', 
            '(2): Show scores', 
            '(3): Quit'
            ]
      print ('What do you want ?')
      print('\n'.join(make_choices))
      choice = int(input('>>> '))
      return choice

def print_results(results):
      
      if result == "Won" :
            results['Won'] += 1
      elif result == "Loss" : 
            results['Loss'] += 1
      else :
            results['Draw'] += 1
      
      return results

def main() :
      while True :
            menu_choice = get_user_menu_choice()

            if menu_choice == 1 :
                  result = jeu.play()

                  results[result] += 1
            elif menu_choice == 2 :
                  print(results)
            elif menu_choice == 3 :
                  print("Thank you for playing. See you next time.")
                  break


print(main())
