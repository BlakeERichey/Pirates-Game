##Functions that are used in several places are located here
import pygame

def pixelToCoord(pixelCoord, gridWidth):
  if gridWidth:
    x = int(pixelCoord[0]/gridWidth) + 1
    y = int(pixelCoord[1]/gridWidth) + 1
    return (x,y)
  else:
    x = int((coord[0]-1) * 64)
    y = int((coord[1]-1) * 64)
    return (x,y)


def coordToPixel(coord, gridWidth):
  if gridWidth:
    x = int((coord[0]-1) * gridWidth)
    y = int((coord[1]-1) * gridWidth)
    return (x, y)
  else:
    x = int((coord[0]-1) * 64)
    y = int((coord[1]-1) * 64)
    return (x, y)

def isInt(value):
  try:
    int(value)
    return True
  except:
    return False

def findDistance(a, b):
  distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
  return distance

def isAdjacent(pos1, pos2):
  distanceX=abs(pos1[0]-pos2[0])
  distanceY=abs(pos1[1]-pos2[1])
  if distanceX > 1 or distanceY > 1:
    return False
  a = (distanceX == 1)
  b = (distanceY == 1)
  return (a and not b) or (not a and b)

def findDir(pos, newPos):
  x = newPos[0] - pos[0]
  y = newPos[1] - pos[1]
  if x == -1:
    return "left"
  elif x == 1:
    return "right"
  elif y == -1:
    return "up"
  elif y == 1:
    return "down"

def isBehind(ship, newPos):
  pos = ship.pos
  dir = ship.dir
  if dir == "up" and (newPos[1] - pos[1] == 1):
    return True
  elif dir == "down" and (newPos[1] - pos[1] == -1):
    return True
  elif dir == "left" and (newPos[0] - pos[0] == 1):
    return True
  elif dir == "right" and (newPos[0] - pos[0] == -1):
    return True
  else:
    return False

class Node():

  def __init__(self, val):
    self.next = None
    self.prev = None
    self.data = None
    if val != None:
      self.data = val

  def getData(self):
    return self.data

  def getNext(self):
    return self.next
  
  def getPrev(self):
    return self.prev
  
  def setData(self, data):
    self.data = data
  
  def setNext(self, node):
    self.next = node
  
  def setPrev(self, node):
    self.prev = node

def addNode(currentNode, newNode):
  currentNode.setNext(newNode)
  newNode.setPrev(currentNode)

def removeNode(currentNode):
  currentNode.getPrev().setNext(None)

#validates if cursor is located between the defined parameters
def cursorLocated(minX, maxX, minY, maxY):
  mx, my = pygame.mouse.get_pos()
  if mx >= minX and mx < maxX and my > minY and my < maxY:
    return True
  return False