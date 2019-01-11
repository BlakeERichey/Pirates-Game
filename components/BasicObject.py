class BasicObject():
  def __init__(self):
    self.pointsLeft = 20
    self.schoonerQty = 1
    self.cargoQty = 0
    self.galleyQty = 0
    
  def addShip(self, shipType):
    if shipType == "Schooner":
      self.schoonerQty += 1
    elif shipType == "Cargo":
      self.cargoQty += 1
    elif shipType == "Galley":
      self.galleyQty += 1
  
  def subShip(self, shipType):
    if shipType == "Schooner":
      self.schoonerQty -= 1
    elif shipType == "Cargo":
      self.cargoQty -= 1
    elif shipType == "Galley":
      self.galleyQty -= 1
      