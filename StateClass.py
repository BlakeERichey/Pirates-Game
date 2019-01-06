import Arrow
from   Arrow import Arrow
class State():

  def __init__(self):
    self.flagDrag = False
    self.shipClicked = False
    self.gridWidth = 64
    self.mx = None
    self.my = None
    self.allShips = []
    self.arrow = Arrow()
    self.color = ""
    self.page = "Menu"