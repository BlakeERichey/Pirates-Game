import components.Path, components.common
from   components.Path  import Path
from   components.common import Node

class PlayerTurn():

    def __init__(self, numPlayers):
      self.head = Node("Player1")
      self.createList(numPlayers)
    
    #takes arguement for number of plays and creates a circular linked list of players
    def createList(self, numPlayers):
      currentPlayer = 2
      currentNode = self.head
      for x in range(2, numPlayers + 1):
        print("Adding `" + "Player" + str(x) + "` to the list")
        if x != numPlayers:
          tempNode=Node("Player" + str(x))
          currentNode.setNext(tempNode)
          currentNode.getNext().setPrev(currentNode)
          currentNode = currentNode.getNext()
        else:
          tempNode=Node("Player" + str(x))
          tempNode.setNext(self.head)
          currentNode.setNext(tempNode)
          currentNode.getNext().setPrev(currentNode)

class State():

  def __init__(self):
    self.flagDrag = False
    self.shipClicked = False
    self.gridWidth = 64
    self.mx = None
    self.my = None
    self.player1Ships = []
    self.player2Ships = []
    self.allShips = []
    self.path = Path()
    self.select = False
    self.page = "Menu"
    self.canHit = []  #represents list of available places that a ship can hit
    self.attack = None #represents Ship being attacked
    self.showMenu = False #Should top menu bar of game be displayed
    self.currentPlayer = None #contains a node that contains the next player and current player. To access current player call .getData()

  def __str__(self):
    rv = "FlagDrag: "       + str(self.flagDrag)
    rv += "\nShipClicked "  + str(self.shipClicked)
    rv += "\nGridwidth "    + str(self.gridWidth)
    rv += "\n(mx, my): "    + str((self.mx, self.my))
    rv += "\nAllShips: "    + str(self.allShips)
    rv += "\nPath: "        + str(self.path)
    rv += "\nSelect: "      + str(self.select)
    rv += "\nPage: "        + str(self.page)
    rv += "\ncanHit: "      + str(self.canHit)
    rv += "\nattack: "      + str(self.attack)
    return rv

  def setPlayers(self, numPlayers):
    playerList = PlayerTurn(numPlayers)
    self.currentPlayer = playerList.head
  
  def endTurn(self):
    currentPlayer = self.currentPlayer.getData()
    #reset ships movement and atk settings at end of turn
    for ship in self.allShips:
      if ship.owner == currentPlayer:
        ship.canMove = ship.speed
        ship.canAtk  = True
    self.currentPlayer = self.currentPlayer.getNext() #move to new player
