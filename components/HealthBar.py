import pygame, components.common
from components.common import pixelToCoord, coordToPixel

class HealthBar():
  def __init__(self, pos):
    self.percent = 1
    self.size = 1
    if pos:
      self.pos = pos
    else:
      self.pos = None
    #length, pos, percent of hp

  def setPercent(self, ship):
    self.percent = ship.hp / float(ship.maxHp)

  #changes pos and size by getting direction and location of ship
  def move(self, ship):
    self.pos = ship.imagePos
    if ship.size != 1:
      if ship.dir != "up" and ship.dir != "down":
        self.size = ship.size
      else:
        self.size = 1
    else:
      self.size = 1