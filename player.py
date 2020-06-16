class Player:
  def __init__(self,name,games_played,games_won,games_lost,games_tied,current_points):
    self.name = name
    self.games_played = games_played 
    self.games_won = games_won
    self.games_lost = games_lost 
    self.games_tied = games_tied 
    self.current_points = current_points
    games_played =0
    games_won =0
    games_lost =0
    games_tied = 0
    current_points=100


  def string_conversion(self):
    # John Doe has 75 points and a winning rate of 57.1%
    if(self.games_played != 0):
      self.winning_rate = (int(self.games_won) / int(self.games_played)) * 100
    else:
      self.winning_rate = 0
    return('{} has {} points and a winning rate of {}'.format(self.name,self.current_points,self.winning_rate))

# print(string_conversion())


  # number of games played
  # number of games won
  # number of games lost
  # number of games tied
  # An integer, current points