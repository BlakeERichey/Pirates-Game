class SetupState():
  def __init__(self):
    self.pointsLeft = 20
    self.schoonerQty = 1
    self.cargoQty = 0
    self.galleyQty = 0
    
  def addShip(self, shipType):
    if shipType == "Schooner":
      self.schoonerQty += 1
      if not(self.isValid()):
        self.schoonerQty -= 1
    elif shipType == "Cargo":
      self.cargoQty += 1
      if not(self.isValid()):
        self.cargoQty -= 1
    elif shipType == "Galley":
      self.galleyQty += 1
      if not(self.isValid()):
        self.galleyQty -= 1
  
  def subShip(self, shipType):
    if shipType == "Schooner":
      self.schoonerQty -= 1
      if not(self.isValid()):
        self.schoonerQty += 1
    elif shipType == "Cargo":
      self.cargoQty -= 1
      if not(self.isValid()):
        self.cargoQty += 1
    elif shipType == "Galley":
      self.galleyQty -= 1
      if not(self.isValid()):
        self.galleyQty += 1
  
  def isValid(self):
    points = self.schoonerQty * 2 - 1
    points += self.cargoQty * 3
    points+= self.galleyQty * 4
    if ((21 - points) >= 0) and self.schoonerQty >= 1 and self.cargoQty >= 0 and self.galleyQty >= 0:
      self.pointsLeft = 21 - points
      return True
    else:
      print("False")
      return False 