import random
from game import Game

class Inbetween(Game):
  def __init__(self):
    self.__debug_mode = False # Hidden attribute for debugMode.

    # Setter method for __debugMode.
  def __setDebugMode(self, x):
      self.__debug_mode = x

    # Getter method for __debugMode.
  def __getDebugMode(self):
      return self.__debug_mode

    # Define property debugMode.
    # If True, print computer's choice.
  debugMode = property(__getDebugMode, __setDebugMode)

  # if debugMode == True:


  def play(self):
    
    """ Play a round of game and return the result as:
        1 if the player win.
        -1 if the player lose.
        0: if it is a draw.
    """
    print("Let's play In-between!")
    x = random.randint(1,10)
    y = random.randint(1,10)
    print('{} {}'.format(x,y))

    print("Choose a number (1-10): ")
    num = int(input())
    if num > x and num < y:
      print('Computer chose {} and {}, you chose {}'.format(x,y,num))
      print("You win!")
      return 1
    elif num < x or num > y:
      print('Computer chose {} and {}, you chose {}'.format(x,y,num))
      print("You lost!")
      return -1
    else:
      print('Computer chose {} and {}, you chose {}'.format(x,y,num))
      print("Tie")
      return 0
 

pl1 = Inbetween()
print(pl1.play())
