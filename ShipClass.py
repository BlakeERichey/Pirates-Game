import pygame, common
from   common     import coordToPixel

class Ship():

  #how to rotate an image
  #schSpriteRight = pygame.transform.rotate(schSprite, 90)

  def __init__(self, ship):
    self.type=ship
    self.dir="up"
    self.pos = (0,0)
    self.owner="Player1"
    if(ship == "Galley"):
      self.damage=self.hp=self.masts=self.aRange=self.accuracy=self.speed=self.carry=self.sight=3
      self.image = pygame.image.load('./resources//images/Icon_Galley.png')
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
      self.image = pygame.image.load('./resources//images/Icon_Schooner.png')
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
  
  ##changes self.pos from a grid coordinate to a pizel location
  def getPosition(self, gridWidth):
    x = (self.pos[0] - 1) * gridWidth
    y = (self.pos[1] - 1) * gridWidth
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
    if root.arrow.tail.getData() != None:
      newPos = (coordToPixel(root.arrow.tail.getData().pos, root.gridWidth))
      gridWidth = root.gridWidth
      self.setPosition((newPos), gridWidth)
      self.setDir(root.arrow.tail.getData().dir)

  def setDir(self, newDir):
    self.dir = newDir
    if self.type == "Schooner":
      image = pygame.image.load('./resources//images/Icon_Schooner.png')
    elif self.type == "Galley":
      image = pygame.image.load('./resources//images/Icon_Galley.png')
    #Additional Code for other ships images
    if(self.dir == "up"):
      self.image = image
    if(self.dir == "right"):
      self.image = pygame.transform.rotate(image, -90)
    if(self.dir == "left"):
      self.image = pygame.transform.rotate(image, 90)
    if(self.dir == "down"):
      self.image = pygame.transform.rotate(image, 180)
