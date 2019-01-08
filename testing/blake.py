import pygame, time, sys, os
# import components.ShipClass, components.StateClass, components.common, components.Path
# from   components.ShipClass  import Ship
os.system("StateClass.py")
from   StateClass import State
# from   components.Path       import Path
# from   components.common     import pixelToCoord, coordToPixel, findDistance
# root = State()

# display_width  = 1920
# display_height = 1080
# root.gridWidth = 64

# def renderCanHit(root):
#   maxX = int(display_width / root.gridWidth)
#   maxY = int(display_height / root.gridWidth)
#   allPossibleCoords = []
#   for x in range(1, maxX):
#     for y in range(1, maxY):
#       allPossibleCoords.append((x,y))
#   print(allPossibleCoords)

# renderCanHit(root)
root = State()
print(root.shipClicked)