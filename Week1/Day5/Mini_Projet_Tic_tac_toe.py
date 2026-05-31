
def display_board():
      board=[
            " "," "," ",
            " "," "," ",
            " "," "," "]
      board[0]= "X"
      print (f"{board[0]} | {board[1]} | {board[2]}")
      print (f"{board[3]} | {board[4]} | {board[5]}")
      print (f"{board[6]} | {board[7]} | {board[8]}")

def player_input(player):
      players = [1, 2]

      for  player in player :
            nombers = [1, 2, 3]
            raw = int(input('Enter row : '))
            columns = int(input('Enter column : '))
            



