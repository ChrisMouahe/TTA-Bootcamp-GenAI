

import random
from game import Game

jeu = Game()

results = {
            "Won": 0,
            "Loss": 0,
            "Draw": 0
            }
def get_user_menu_choice():
      """
    Display the main menu
    and return the user's choice.

    Menu options:
    1 - Play a new game
    2 - Show scores
    3 - Quit the program

    Returns:
        int: The selected menu option.
    """

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
      """
    Display the current game scores.

    Args:
        results (dict): Dictionary containing
        the number of wins, losses, and draws.

    Returns:
        dict: Updated results dictionary.
    """

      if result == "Won" :
            results['Won'] += 1
      elif result == "Loss" : 
            results['Loss'] += 1
      else :
            results['Draw'] += 1
      
      return results

def main() :
      """
    Run the main game loop.

    The player can:
    - start a new game,
    - display scores,
    - quit the program.
    """
    
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
