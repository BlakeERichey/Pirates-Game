import pygame
import common

from common import coordToPixel, isInt, isAdjacent, Node, addNode, removeNode

class Arrow():

  def __init__(self):
    self.head  = Node(None)
    self.dir   = None

  #displays arrow
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


  #updates arrow to be longer or shorter if needed
  #pos: coord, not pixel location
  def updateArrow(self, pos, root):
    currentNode = self.head
    allCoord = []
    #generate list of all parts in linked list, currentNode is set to last Node in linked list
    while(currentNode.getNext() != None):
      allCoord.append(currentNode.getData())
      currentNode = currentNode.getNext()
    if currentNode.getData() != None:
      allCoord.append(currentNode.getData())

    #position is adjacent to ship and linked list has no length
    if pos not in allCoord and isAdjacent(pos, root.shipClicked.pos) and self.head.getData() == None:
      self.head.setData(Part("arrow", pos))

    #pos in linked list and is equal to the previous position to the last
    if len(allCoord) >= 2 and pos == allCoord[len(allCoord)-2].pos:
      removeNode(currentNode)

    print("allcoord",[x.pos for x in allCoord])
    #if pos is adjacent to the last position in linked list
    if (len(allCoord) > 0):
      lastCoord = allCoord[len(allCoord) - 1]
    if len(allCoord) > 0 and len(allCoord) < root.shipClicked.speed and pos != lastCoord.pos and isAdjacent(lastCoord.pos, pos): 
      addNode(currentNode, Node(Part("arrow", pos)))
      


class Part():
  def __init__(self, image, pos):
    if image == "arrow":
      self.image = pygame.image.load('./resources//images/Arrow.png')
    self.pos = pos