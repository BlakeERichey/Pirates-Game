import pygame
import components.common

from components.common import (coordToPixel, isInt, isAdjacent, Node, addNode, 
  isBehind, removeNode, findDir)

class Path():

  def __init__(self):
    self.head   = Node(None)
    self.dir    = None
    self.tail   = None
    self.length = 0

  #displays path
  def renderArrow(self, background, root): #additional parameter: background
    # part = self.head.getData()
    # background.blit(part.image, coordToPixel(part.pos, root.gridWidth))
    currentNode = self.head
    while(currentNode.getNext() != None):
      tempPart = currentNode.getData()
      background.blit(tempPart.image, coordToPixel(tempPart.pos, root.gridWidth))
      currentNode = currentNode.getNext()
    if currentNode.getData() != None:
      tempPart = currentNode.getData()
      background.blit(tempPart.image, coordToPixel(tempPart.pos, root.gridWidth))


  #updates path to be longer or shorter if needed
  #pos: coord, not pixel location
  def updateArrow(self, pos, root):
    currentNode = self.head
    allCoord = [] #list of all parts of linked list
    #generate list of all parts in linked list, currentNode is set to last Node in linked list
    while(currentNode.getNext() != None):
      allCoord.append(currentNode.getData())
      currentNode = currentNode.getNext()
    if currentNode.getData() != None:
      allCoord.append(currentNode.getData())

    self.tail = currentNode

    #position is adjacent to ship and linked list has no length
    if (pos not in allCoord and isAdjacent(pos, root.shipClicked.pos) and self.head.getData() == None 
    and (not(isBehind(root.shipClicked, pos))) and root.shipClicked.canMove > 0):
      self.head.setData(Part("path", pos))
      self.head.getData().setDir(root.shipClicked.pos, pos)

    #pos in linked list and is equal to the previous position to the last
    if (len(allCoord) >= 2 and pos == allCoord[len(allCoord)-2].pos):
      removeNode(currentNode)

    #return to path length of 0
    if (len(allCoord) == 1 and pos == root.shipClicked.pos):
      self.head = Node(None)

    #if pos is adjacent to the last position in linked list
    if (len(allCoord) > 0):
      lastCoord = allCoord[len(allCoord) - 1]
    if len(allCoord) > 0 and len(allCoord) < root.shipClicked.canMove and pos != lastCoord.pos and isAdjacent(lastCoord.pos, pos): 
      tempPart = Part("path", pos)
      tempPart.setDir(lastCoord.pos, pos)
      addNode(currentNode, Node(tempPart))
    self.length = len(allCoord)

      

#contains an arrow image to represent a part of a Path class
class Part():
  def __init__(self, image, pos):
    if image == "path":
      self.image = pygame.image.load('./resources//images/Arrow.png')
    self.pos = pos
    self.dir = "up"
  
  def setDir(self, pos, newPos):
    self.dir = findDir(pos, newPos)
    if(self.dir != "up"):
      if(self.dir == "right"):
        self.image = pygame.transform.rotate(self.image, -90)
      if(self.dir == "left"):
        self.image = pygame.transform.rotate(self.image, 90)
      if(self.dir == "down"):
        self.image = pygame.transform.rotate(self.image, 180)