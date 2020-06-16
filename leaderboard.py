from player import Player
from operator import itemgetter
class LeaderBoard:
  playerlist =[]
  def load(self):
      filename = 'players.txt'
      f = open( filename, "r" )
      
      a = []
      self.a =a
      for line in f:
        a.append(line)
      self.playerlist.append(Player(a[0],a[1][0],a[1][2],a[1][4],a[1][6],a[1][8]+a[1][9]))
      self.playerlist.append(Player(a[2],a[3][0]+a[3][1],a[3][3]+a[3][4],a[3][6],a[3][8],a[3][8]+a[3][11]+a[3][12]))
      self.playerlist.append(Player(a[4],a[5][0],a[5][2],a[5][4],a[5][6],a[5][8]+a[5][9]))
      self.__sortPlayers(self.playerlist)
      return True

  def __sortPlayers(self,playerlist):
    # self.playerlist = playerlist
    try:
      sorted(playerlist, key=itemgetter(2))
      return true
    except:
      return False
  def save(self):
    var = " "
    with open('output.txt', 'a') as out:
      out.write(var + '\n')

    return True
    
  def display(self):
    name='Player Name'
    p = "P"
    w = "W"
    l ="L"
    t = "T"
    rate ='W-Rate'
    point = 'Points'
    print(name.ljust(30," ")+p.ljust(2," ")+w.ljust(2," ")+l.ljust(2," ")+t.ljust(2," ")+rate.ljust(6," ")+point.ljust(6," "))
    if self.playerlist == None:
      print("No players found")
    else:
      print(self.a[2],self.a[3][0]+self.a[3][1],self.a[3][3]+self.a[3][4],self.a[3][6],self.a[3][8],self.a[3][8]+self.a[3][11]+self.a[3][12])
      print(self.a[0],self.a[1][0],self.a[1][2],self.a[1][4],self.a[1][6],self.a[1][8]+self.a[1][9])
      print(self.a[4],self.a[5][0],self.a[5][2],self.a[5][4],self.a[5][6],self.a[5][8]+self.a[5][9])
    
  def addPlayer(self,name):
    # creating anew instance of the class
    newplayer = Player(name,0,0,0,0,100)
    # checking whether the player exist or not 
    self.__findPlayer(newplayer)
    # adding a new player to the player list
    self.playerlist.append(newplayer)
    # sorting the list after adding the player
    self.__sortPlayers(LeaderBoard.playerlist)

  def __findPlayer(self,newplayer):
    # checking if the player exist
    if newplayer not in LeaderBoard.playerlist:
      return True
    else:
      return False
    
  def removePlayer(self,name):
    # creating a new player
    existplayer = Player(name,0,0,0,0,100)
    # checking whether the player exists
    self.__findPlayer(existplayer)
    # removing the player
    self.playerlist.remove(existplayer)
    
  def getPlayerPoints(self,name):
    player = Player(name,0,0,0,0,100)
    if player not in self.playerlist:
      return -1
    else:
      return player.current_points
  def getWinner(self):
    return None

  def recordGamePlay(name,num_bids,result):
    return 1

