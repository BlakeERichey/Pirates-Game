import pygame
import common

from common import coordToPixel, isInt

class Arrow():

  def __init__(self):
    self.part1 = None
    self.part2 = None
    self.part3 = None
    self.part4 = None
    self.part5 = None
    self.head  = None
    self.dir   = None

  #displays arrow
  def renderArrow(self, background): #additional parameter: background
    parts = [self.part1, self.part2, self.part3, self.part4, self.part5]
    for part in parts:
      if part:
        background.blit(part.image, part.pos)

  #updates arrow to be longer or shorter if needed
  #pos: coord, not pixel location
  def updateArrow(self, pos, root):
    if pos and pos != root.shipClicked.pos:
      pos = coordToPixel(pos, root.gridWidth)
      if self.part1 == None:
        self.part1 = Part("arrow", pos)
      elif self.part1 and pos != self.part1.pos and self.part2 == None:
        self.part2 = Part("arrow", pos)
      print(self.part1, self.part2)
    if(pos == False):
      self.part1 = None
      self.part2 = None

class Part():
  def __init__(self, image, pos):
    if image == "arrow":
      self.image = pygame.image.load('./resources//images/Arrow.png')
    self.pos = pos

