##This is a testing page for debugging code and testing methods 
import pygame
import common

from common import coordToPixel, isInt, isAdjacent, Node

head = Node(None)
head.setData(13)
tempNode = Node(None)
tempNode.setData(14)
head.setNext(tempNode)

currentNode = head
acc = 0

allCoord = []
#currentNode set to last Node in list
while(currentNode.getNext() != None):
  acc += 1
  allCoord.append(currentNode.getData())
  currentNode = currentNode.getNext()
if currentNode.getData != None:
  allCoord.append(currentNode.getData())
print(acc, allCoord)