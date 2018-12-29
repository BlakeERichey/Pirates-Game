class Ship():
##    type = ""
##    dir = "up"
##    pos
##    owner
##    damage = -1
##    hp = -1
##    masts = -1
##    aRange = -1 #attack range
##    accuracy = -1
##    speed = -1
##    carry = -1
##    sight = -1

    def __init__(self, ship):
      self.type=ship
      self.dir="up"
      self.pos = (0,0)
      self.owner="Player1"
      if(ship == "Galley"):
        self.damage=self.hp=self.masts=self.aRange=self.accuracy=self.speed=self.carry=self.sight=3
      elif(ship=="Cargo"):
        self.damage=1
        self.aRange=self.accuracy=self.speed=2
        self.masts=self.sight=3
        self.hp=4
        self.carry=5
      elif(ship == "Schooner"):
        self.damage=self.carry=1
        self.hp=self.masts=self.aRange=2
        self.accuracy=3
        self.speed=self.sight=5
      elif(ship=="Frigate"):
        self.damage=self.aRange=self.accuracy=self.sight=4
        self.hp=self.masts=3
        self.speed=self.carry=2
            
    def __str__(self):
      rv = "Ship:\nType: " + str(self.type) + "\nDirection: " + str(self.dir)
      rv += "\nPosition: " + str(self.pos) + "\nOwner: " + str(self.owner)
      rv += "\nDamage: " + str(self.damage)
      rv += "\nHp: " + str(self.hp) + "\nMasts: " + str(self.masts)
      rv += "\nRange: " + str(self.aRange) + "\nAccuracy: " + str(self.accuracy)
      rv += "\nSpeed: " + str(self.speed) + "\nCarry " + str(self.carry) + "\nSight: " + str(self.sight)
      return rv
    
    def getPosition(self):
      x = (self.pos[0] - 1) * 64
      y = (self.pos[1] - 1) * 64
      return (x, y)
    
    #Accepts tuple of new coodinate in pixel form and transforms it to a 
    #grid coordinate then sets the ships location
    def setPosition(self, newPos):
      x = int(newPos[0]/64) + 1
      y = int(newPos[1]/64) + 1
      self.pos = (x,y)
