import pygame, components.common, components.HealthBar
from   components.HealthBar  import HealthBar
from   components.common     import coordToPixel


class Ship():

  #how to rotate an image
  #schSpriteRight = pygame.transform.rotate(schSprite, 90)

  def __init__(self, ship, pos):
    self.type=ship
    self.dir="up"
    self.pos = pos
    self.owner="Player1"
    self.coords = []
    if(ship == "Galley"):
      self.size=self.cannons=2
      self.damage=self.maxHp=self.aRange=self.accuracy=self.speed=self.carry=self.sight=3
      self.image = pygame.image.load('./resources//images/Icon_Galley.png')
      self.imagePos = (self.pos)
    elif(ship=="Cargo"):
      self.damage=1
      self.aRange=self.accuracy=self.speed=self.size=self.cannons=2
      self.sight=3
      self.maxHp=4
      self.carry=5
      self.imagePos = (self.pos)
      self.image = pygame.image.load('./resources//images/Icon_Cargo.png')
    elif(ship == "Schooner"):
      self.damage=self.carry=self.size=self.cannons=1
      self.maxHp=self.aRange=2
      self.accuracy=3
      self.speed=self.sight=5
      self.imagePos = (self.pos)
      self.image = pygame.image.load('./resources//images/Icon_Schooner.png')
    elif(ship=="Frigate"):
      self.damage=self.aRange=self.accuracy=self.sight=4
      self.maxHp=self.cannons=self.size=3
      self.speed=self.carry=2
      self.imagePos = (self.pos)
      self.image = pygame.image.load('./resources//images/Icon_Frigate.png')
    self.maxHp = 2 * self.maxHp
    self.hp = self.maxHp
    self.setCoords()
    self.healthBar = HealthBar(self.pos)
    
          
  def __str__(self):
    rv = "Ship:\nType: " + str(self.type) + "\nDirection: " + str(self.dir)
    rv += "\nPosition: " + str(self.pos) + "\nOwner: " + str(self.owner)
    rv += "\nDamage: " + str(self.damage)
    rv += "\nHp: " + str(self.hp) + "\nCannons: " + str(self.cannons)
    rv += "\nRange: " + str(self.aRange) + "\nAccuracy: " + str(self.accuracy)
    rv += "\nSpeed: " + str(self.speed) + "\nCarry " + str(self.carry) + "\nSight: " + str(self.sight)
    rv += "\nimagePos" + str(self.imagePos) + "\nCoords: " + str(self.coords)
    return rv
  
  ##changes self.pos from a grid coordinate to a pizel location
  def getPosition(self, gridWidth):
    x = (self.imagePos[0] - 1) * gridWidth
    y = (self.imagePos[1] - 1) * gridWidth
    return (x, y)
  
  #Accepts tuple of new coodinate in pixel form and transforms it to a 
  #grid coordinate then sets the ships location
  def setPosition(self, newPos, gridWidth):
    x = int(newPos[0]/gridWidth) + 1
    y = int(newPos[1]/gridWidth) + 1
    self.pos = (x,y)

  #moves ship to newPos
  #newPos: pixel coordinate of new position for ship to be moved to
  def moveShip(self, root):
    if root.path.tail.getData() != None:
      newPos = (coordToPixel(root.path.tail.getData().pos, root.gridWidth))
      gridWidth = root.gridWidth
      self.setPosition((newPos), gridWidth)
      self.setDir(root.path.tail.getData().dir)
      self.setImagePos(root)
      self.setCoords()
      self.healthBar.move(self)

  #sets direction of ship to newDir then sets image to match
  def setDir(self, newDir):
    self.dir = newDir
    if self.type == "Schooner":
      image = pygame.image.load('./resources//images/Icon_Schooner.png')
    elif self.type == "Galley":
      image = pygame.image.load('./resources//images/Icon_Galley.png')
    elif self.type == "Cargo":
      image = pygame.image.load('./resources//images/Icon_Cargo.png')
    elif self.type == "Frigate":
      image = pygame.image.load('./resources//images/Icon_Frigate.png')
    #Additional Code for other ships images
    if(self.dir == "up"):
      self.image = image
    if(self.dir == "right"):
      self.image = pygame.transform.rotate(image, -90)
    if(self.dir == "left"):
      self.image = pygame.transform.rotate(image, 90)
    if(self.dir == "down"):
      self.image = pygame.transform.rotate(image, 180)

  #relocates where ship image renders based on the size of the ship
  def setImagePos(self, root):
    ship = root.shipClicked
    if ship.type != "Schooner":
      if ship.dir == "right":
        if ship.type == "Frigate":
          ship.imagePos = (ship.pos[0] - 2, ship.pos[1]) 
        elif ship.type == "Galley":
          ship.imagePos = (ship.pos[0] - 1, ship.pos[1])
        elif ship.type == "Cargo":
          ship.imagePos = (ship.pos[0] - 1, ship.pos[1])  
      elif ship.dir == "down":
        if ship.type == "Frigate":
          ship.imagePos = (ship.pos[0], ship.pos[1] - 2) 
        elif ship.type == "Galley":
          ship.imagePos = (ship.pos[0], ship.pos[1] - 1)
        elif ship.type == "Cargo":
          ship.imagePos = (ship.pos[0], ship.pos[1] - 1) 
      else:
        ship.imagePos = ship.pos
    else:
      ship.imagePos = ship.pos
  
  #sets location of all points the ship
  def setCoords(self):
    start = self.pos
    coords = []
    for x in range(0, self.size):
      if self.dir == "up":
        coords.append((start[0], start[1]+x))
      if self.dir == "down":
        coords.append((start[0], start[1]-x))
      if self.dir == "right":
        coords.append((start[0]-x, start[1]))
      if self.dir == "left":
        coords.append((start[0]+x, start[1]))
    self.coords = coords

  def renderHealthBar(self, display, root):
    x, y = coordToPixel(self.healthBar.pos, root.gridWidth)
    width = root.gridWidth * self.healthBar.size
    self.healthBar.setPercent(self)
    pygame.draw.rect(display, (255,0,0), [x+5,y,width-10,5]) #draw red bar
    pygame.draw.rect(display, (0,255,0), [x+5,y,width*self.healthBar.percent-10,5]) #draw green bar