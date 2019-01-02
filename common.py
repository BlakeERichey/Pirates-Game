##Functions that are used in several places are located here
def pixelToCoord(pixelCoord, gridWidth):
    x = int(pixelCoord[0]/gridWidth) + 1
    y = int(pixelCoord[1]/gridWidth) + 1
    return (x,y)