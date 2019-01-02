def Pirates():   
  ##GUI Main Game
  import pygame, time, sys
  import ShipClass, StateClass
  from   StateClass import State
  from   ShipClass import Ship

  #State manager
  root = State()

  #Set Player Ships
  x = Ship("Schooner")
  x.pos=(3,3)
  y = Ship("Galley")
  y.pos = (4,4)
  Player1Ships = [x, y] 
  playerShips = [ship for ship in Player1Ships]
  

  #Takes coordinate and determines which ship if any it corresponds to
  def getShip(coordinate, allShips):
    for ship in allShips:
      #for square in ship.pos:
      if(coordinate == ship.pos):
        return ship
    return False #if no ship contains coordinate, return false
  
  #Take a coordinate that represents a pixel and returns the grid location
  def pixelToCoord(pixelCoord, gridWidth):
    x = int(pixelCoord[0]/gridWidth) + 1
    y = int(pixelCoord[1]/gridWidth) + 1
    return (x,y)


  def run_game():
    #Set Player Ships
    x = Ship("Schooner")
    x.pos=(3,3)
    y = Ship("Galley")
    y.pos = (4,4)
    z = Ship("Schooner")
    z.pos = (1,1)
    Player1Ships = [x, y, z] 
    playerShips = [ship for ship in Player1Ships]

    pygame.init()

    #background = (51, 70, 242)
    battlefieldBackground=pygame.image.load('./resources/images/background-battlefield.jpg')

    display_width = 1920
    display_height = 1080

    #Set GUI Size and title
    gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
    pygame.display.set_caption('Pirates PC!')
    clock = pygame.time.Clock()

    #Check for events
    while True:
      gridWidth = 64 #Width of square on battlefield
      mx = None 
      my = None
    
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

        #Monitor when keyboard key is pressed
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

        #Monitor when mouse is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
          #if left mouse button is pressed, 
          #get position of mouse and save it ss mx and my
          if (pygame.mouse.get_pressed()[0] == 1):
            mx, my = pygame.mouse.get_pos()
        
          #If ship was clicked, set state of flagDrag to true
          if(mx != None):
            coord = pixelToCoord((mx, my), gridWidth)
            root.shipClicked = getShip(coord, playerShips)
            if(root.shipClicked):
              root.flagDrag = True
              print("You clicked a", root.shipClicked.type)
        
        #if left mouse button is released, move ship that was clicked
        if (pygame.mouse.get_pressed()[0] == 0) and root.flagDrag == True:
          print("key lifted")
          newMx, newMy = pygame.mouse.get_pos()
          root.shipClicked.setPosition((newMx, newMy), gridWidth)
          root.flagDrag = False
          root.shipClicked = False

      #Load and Fill Background
      gameDisplay.blit(battlefieldBackground, (0,0))

      #Load Sprites
      for ship in playerShips:
        gameDisplay.blit(ship.image, ship.getPosition(gridWidth))
      
      #Rerender
      pygame.display.update()

      time.sleep(0.03)
  run_game()

Pirates()