import components.Path
from   components.Path import Path
class State():

  def __init__(self):
    self.flagDrag = False
    self.shipClicked = False
    self.gridWidth = 64
    self.mx = None
    self.my = None
    self.allShips = []
    self.path = Path()
    self.select = False
    self.page = "Menu"