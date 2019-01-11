def Play(root):   
  ##GUI Main Game
  import pygame, time, sys
  import components.ShipClass, components.StateClass, components.common, components.Path
  from   components.ShipClass  import Ship
  from   components.StateClass import State
  from   components.Path       import Path
  from   components.common     import pixelToCoord, coordToPixel, findDistance

  #Set Resolution
  display_width = 1920
  display_height = 1080

  #initalize music
  pygame.mixer.music.load('./resources/music/music.mp3')
  pygame.mixer.music.play(loops=-1, start=0.0)

  #Set Player Ships
  a = Ship("Schooner", (1,1))
  newShip = Ship("Galley", (10,7))
  newShip.owner = "Player2"
  b = Ship("Cargo", (10,2))
  x = Ship("Schooner", (3,3))
  y = Ship("Galley", (4,4))
  y.owner = "Player2"
  z = Ship("Frigate", (5,5))
  Player1Ships = [x, y, z, a, b, newShip] 
  playerShips = [ship for ship in Player1Ships]
  root.allShips = playerShips
  

  #Takes coordinate and determines which ship if any it corresponds to
  def getShip(coordinate, allShips):
    for ship in allShips:
      #for square in ship.pos:
      if(coordinate in ship.coords):
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
    
    #create a temporary ship and test that the new ships locations dont cross another ship
    #excluding the ship being moved
    otherShips = root.allShips[:]
    otherShips.remove(ship)
    tempShip = Ship(ship.type, ship.pos)
    tempShip.moveShip(root)
    for point in tempShip.coords:
      if getShip(point, otherShips):
        return False
    return True

  def findCanHit(root):
    root.canHit = [] #reset canHit in event no ship is clicked
    if root.shipClicked:
      maxX = int(display_width / root.gridWidth) + 1
      maxY = int(display_height / root.gridWidth) + 2
      allPossibleCoords = []
      for x in range(1, maxX):
        for y in range(1, maxY):
          allPossibleCoords.append((x,y))
      
      #determine enemy ships
      otherShips = []
      for ship in root.allShips:
        if ship.owner != root.shipClicked.owner:
          otherShips.append(ship)
      
      #find enemy ships locations
      otherShipsCoords = []
      for ship in otherShips:
        for point in ship.coords:
          otherShipsCoords.append(point) 
      
      #if enemy ship location point is within range of ship clicked, add point to root.canHit
      for point in allPossibleCoords:
        for coord in root.shipClicked.coords:
          if findDistance(coord, point) <= root.shipClicked.aRange and point in otherShipsCoords:
            if point not in root.canHit:
              root.canHit.append(point)     

  def renderCanHit(root, display, icon):
    findCanHit(root)
    for point in root.canHit:
      display.blit(icon, coordToPixel(point, root.gridWidth))
  
  def makeAttack(root):
    print("hit")
    root.attack.hp -= root.shipClicked.damage
    print(root.attack.type, "Health after attack is", root.attack.hp)
    if root.attack.hp <= 0:
      root.allShips.remove(root.attack)
    root.attack = None
    root.shipClicked = None

  def run_game():
    pygame.init()

    #background = (51, 70, 242)
    battlefieldBackground=pygame.image.load('./resources/images/background-battlefield.jpg')
    dangerIcon=pygame.image.load('./resources/images/danger.png')

    #Set GUI Size and title
    gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
    pygame.display.set_caption('Pirates PC!')
    clock = pygame.time.Clock()

    #Check for events
    while root.page == "Play":
      root.mx = None
      root.my = None
    
      for event in pygame.event.get():
        # print("\n\n\n\n" + root)
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
            if coord in root.canHit:
                root.attack = getShip(coord, playerShips)
                makeAttack(root)
            else:
              root.shipClicked = getShip(coord, playerShips)
              if(root.shipClicked):
                root.flagDrag = True
                print("You clicked a", root.shipClicked.type)
              
        if root.flagDrag:
          mx, my = pygame.mouse.get_pos()
          coord = pixelToCoord((mx, my), root.gridWidth)
          root.path.updateArrow(coord, root)

        #if left mouse button is released, move ship that was clicked
        if (pygame.mouse.get_pressed()[0] == 0) and root.flagDrag == True:
          print("key lifted")
          newMx, newMy = pygame.mouse.get_pos()
          coord = pixelToCoord((newMx, newMy), root.gridWidth)
          if coord in root.shipClicked.coords:
            print("Ship Active but not dragging")
            print(root.canHit)
            root.flagDrag = False
          else:
            res = moveIsValid(root.shipClicked, (newMx, newMy))
            print("Move is valid: ", res)
            if(res):
              root.shipClicked.moveShip(root)
            root.flagDrag = False
            root.shipClicked = False
            root.path = Path()


      #Load and Fill Background
      gameDisplay.blit(battlefieldBackground, (0,0))

      if(root.path):
        root.path.renderArrow(gameDisplay, root)

      #Load Sprites
      for ship in playerShips:
        gameDisplay.blit(ship.image, ship.getPosition(root.gridWidth))
      renderCanHit(root, gameDisplay, dangerIcon) #ship shooting locations

      pygame.draw.rect(gameDisplay, (0,255,0), [0,0,64,10])
      pygame.draw.rect(gameDisplay, (255,0,0), [32,0,32,10])
      
      #Rerender
      pygame.display.update()

      time.sleep(0.03)
  run_game()