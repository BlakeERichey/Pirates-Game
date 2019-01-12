import components.Path
from   components.Path import Path
class State():

  def __init__(self):
    self.flagDrag = False
    self.shipClicked = False
    self.gridWidth = 64
    self.mx = None
    self.my = None
    self.player1Ships = []
    self.allShips = []
    self.path = Path()
    self.select = False
    self.page = "Menu"
    self.canHit = []  #represents list of available places that a ship can hit
    self.attack = None #represents Ship being attacked
    self.showMenu = False #Should top menu bar of game be displayed

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