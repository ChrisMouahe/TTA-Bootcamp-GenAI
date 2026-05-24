
import random
class Game :
      """
    Represents a Rock-Paper-Scissors game.
    """
      def get_user_item(self):
            """
        Ask the user to choose rock, paper, or scissors.

        The function keeps asking until
        the user enters a valid choice.

        Returns:
            str: The user's choice ('r', 'p', or 's').
        """
            self.user_item = ""
            while self.user_item.lower() != "r" and self.user_item.lower() != "p" and self.user_item.lower() != "s" :
                  self.user_item = input(' Select (r)ock, (p)aper or (s)cissors : ')
            
            return self.user_item.lower()

      def get_computer_item(self):
            """
        Randomly select rock, paper, or scissors
        for the computer.

        Returns:
            str: The computer's choice.
        """
            choices = ["r", "p", "s"]
            self.computer_item = random.choice(choices)
            return self.computer_item

      def get_game_result(self, user_item, computer_item):
            self.user_item = user_item
            self.computer_item = computer_item
            self.result = ""

            if self.user_item == "p":
                  if self.computer_item == "s":
                        self.result = "Loss"
                  elif self.computer_item == "r" :
                        self.result = "Won"
                  else :
                        self.result = "Draw"

            elif self.user_item == "r" :
                  if self.computer_item == "s" :
                        self.result = "Won"

                  elif self.computer_item == "p" :
                        self.result = "Loss"

                  else :
                        self.result = "Draw"

            else :
                  if self.computer_item == "p":
                        self.result = "Won"

                  elif self.computer_item == "r" :
                        self.result = "Loss"

                  else :
                        self.result = "Draw"
            return self.result

      def play(self):
            """
        Play one complete game.

        This method:
        - gets the user's choice,
        - gets the computer's choice,
        - determines the game result,
        - displays the final message.

        Returns:
            str: The game result.
        """


            sentences = [
                  "you'll sure win the next time.",
                  "Next time will be better.",
                  "Don't give up, try again.",
                  "No luck this time.",
                  "Next time will be the right one."
            ]
            #recupérer le choix de l'utilisateur 
            user_item1 = self.get_user_item()
            #Tire un objet pour l'ordinateur
            computer_item1 = self.get_computer_item()

            #Déterminer le résultat de jeu
            result_item = self.get_game_result(user_item1, computer_item1) 
            if result_item == "Won" :
                  print(f"You selected {self.user_item}. The computeur selected {self.computer_item}. Congratulations !! You won.")
                  print("Thank you for participating.")
            elif result_item == "Loss" :
                  print(f"You selected {self.user_item}. The computeur selected {self.computer_item}. Damn !! You lose this time. {random.choice(sentences)}")
                  print("Thank you for participating.")
            elif result_item == "Draw" :
                  print(f"You selected {self.user_item}. The computeur selected {self.computer_item}. You drew.")
                  print("Thank you for participating.")


            return result_item
