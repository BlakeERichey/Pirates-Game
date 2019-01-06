def Play(root):   
  ##GUI Main Game
  import pygame, time, sys
  import ShipClass, StateClass, common, Arrow
  from   StateClass import State
  from   ShipClass  import Ship
  from   common     import pixelToCoord, coordToPixel
  from   Arrow      import Arrow

  #State manager
  # root = State()

  #Set Player Ships
  a = Ship("Schooner")
  a.pos=(1,1)
  newShip = Ship("Galley")
  newShip.pos = (17,7)
  b = Ship("Schooner")
  b.pos=(12, 15)
  x = Ship("Schooner")
  x.pos=(3,3)
  y = Ship("Galley")
  y.pos = (4,4)
  z = Ship("Schooner")
  z.pos = (1,3)
  Player1Ships = [x, y, z, a, b, newShip] 
  playerShips = [ship for ship in Player1Ships]
  root.allShips = playerShips
  

  #Takes coordinate and determines which ship if any it corresponds to
  def getShip(coordinate, allShips):
    for ship in allShips:
      #for square in ship.pos:
      if(coordinate == ship.pos):
        return ship
    return False #if no ship contains coordinate, return false

  #Takes ship that is being moved and where it is being moved to, in pixel 
  #coords, and verifies it is a valid location that ship can be moved to
  def moveIsValid(ship, newCoord):
    newCoord = pixelToCoord(newCoord, root.gridWidth)

    ship2 = getShip(newCoord, root.allShips)
    distance = abs(ship.pos[0] - newCoord[0]) + abs(ship.pos[1] - newCoord[1])

    if distance > ship.speed:
      print("distance too great")
      return False 
    if (ship2):
      print("ship exist here")
      return False
    return True
  
  def run_game():
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
    while root.page == "Play":
      root.mx = None
      root.my = None
    
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
          #get position of mouse and save it as mx and my
          if (pygame.mouse.get_pressed()[0] == 1):
            root.mx, root.my = pygame.mouse.get_pos()
        
          #If ship was clicked, set state of flagDrag to true
          if(root.mx != None):
            coord = pixelToCoord((root.mx, root.my), root.gridWidth)
            root.shipClicked = getShip(coord, playerShips)
            if(root.shipClicked):
              root.flagDrag = True
              print("You clicked a", root.shipClicked.type)
              
        if root.flagDrag:
          mx, my = pygame.mouse.get_pos()
          coord = pixelToCoord((mx, my), root.gridWidth)
          root.arrow.updateArrow(coord, root)

        #if left mouse button is released, move ship that was clicked
        if (pygame.mouse.get_pressed()[0] == 0) and root.flagDrag == True:
          print("key lifted")
          newMx, newMy = pygame.mouse.get_pos()
          res = moveIsValid(root.shipClicked, (newMx, newMy))
          print("Move is valid: ", res)
          if(res):
            root.shipClicked.moveShip(root)
          root.flagDrag = False
          root.shipClicked = False
          root.arrow = Arrow()


      #Load and Fill Background
      gameDisplay.blit(battlefieldBackground, (0,0))

      if(root.arrow):
        root.arrow.renderArrow(gameDisplay, root)

      #Load Sprites
      for ship in playerShips:
        gameDisplay.blit(ship.image, ship.getPosition(root.gridWidth))
      
      #Rerender
      pygame.display.update()

      time.sleep(0.03)
  run_game()