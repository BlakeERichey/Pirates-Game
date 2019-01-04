##Functions that are used in several places are located here
def pixelToCoord(pixelCoord, gridWidth):
    x = int(pixelCoord[0]/gridWidth) + 1
    y = int(pixelCoord[1]/gridWidth) + 1
    return (x,y)

def coordToPixel(coord, gridWidth):
  x = int((coord[0]-1) * gridWidth)
  y = int((coord[1]-1) * gridWidth)
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
  distanceY=abs(pos1[1] - pos2[1])
  if distanceX > 1 or distanceY > 1:
    return False
  a = (distanceX == 1)
  b = (distanceY == 1)
  return (a and not b) or (not a and b)

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
