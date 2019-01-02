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