import pygame

class Arrow():

  def __init__(self):
    self.part1 = Part("arrow", (192, 128))
    self.part2 = None
    self.part3 = None
    self.part4 = None
    self.part5 = None
    self.head  = None
    self.dir   = None

  #displays arrow
  def renderArrow(self, background): #additional parameter: background
    background.blit(self.part1.image, self.part1.pos)

  #updates arrow to be longer or shorter if needed
  def updateArrow(self, pos):
    if part1 == None:
      part1 = Part("arrow", pos)
    return self.part1

class Part():
  def __init__(self, image, pos):
    if image == "arrow":
      self.image = pygame.image.load('./resources//images/Arrow.png')
    self.pos = pos

