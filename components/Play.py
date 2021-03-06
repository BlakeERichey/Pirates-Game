def Play(root):   
  ##GUI Main Game
  import pygame, time, sys, random
  import components.ShipClass, components.StateClass, components.common, components.Path
  from   components.ShipClass  import Ship
  from   components.StateClass import State
  from   components.Path       import Path
  from   components.common     import pixelToCoord, coordToPixel, findDistance, cursorLocated 

  #Set Resolution
  display_width = 1920
  display_height = 1080

  #initalize music
  pygame.mixer.music.load('./resources/music/music.mp3')
  pygame.mixer.music.play(loops=-1, start=0.0)

  # newShip = Ship("Frigate", (3,4))
  # newShip.owner = "Player2"
  playerShips = [ship for ship in root.player1Ships]
  playerShips += [ship for ship in root.player2Ships]
  # playerShips.append(newShip)
  root.allShips = playerShips
  root.setPlayers(2)  #sets number of players
  

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

    if root.path.length > ship.canMove: #needs to be path distance
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

  #sets root.shipClicked.canHit to all locations active ship can hit that contains an enemy ship
  def findCanHit(root):
    if root.shipClicked:
      root.shipClicked.canHit = [] #reset canHit
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
      
      #if enemy ship location point is within range of ship clicked, add point to root.shipClicked.canHit
      for point in allPossibleCoords:
        for coord in root.shipClicked.coords:
          if findDistance(coord, point) <= root.shipClicked.aRange and point in otherShipsCoords:
            if point not in root.shipClicked.canHit:  
              root.shipClicked.canHit.append(point)
  
  #finds points that a ship can fire at that it can also broadside
  def findCanBroadside(root):
    root.shipClicked.canBroadside = [] #reset canBroadside
    #find available locations that can be broadsided to right/left of ship
    if root.shipClicked.dir == "up" or root.shipClicked.dir == "down":
      for shipCoord in root.shipClicked.coords:  #check y values
        for canHitCoord in root.shipClicked.canHit:
          if shipCoord[1] == canHitCoord[1]:
            if canHitCoord not in root.shipClicked.canBroadside:
              root.shipClicked.canBroadside.append(canHitCoord)
    elif root.shipClicked.dir == "left" or root.shipClicked.dir == "right":
       for shipCoord in root.shipClicked.coords:  #check x values
        for canHitCoord in root.shipClicked.canHit:
          if shipCoord[0] == canHitCoord[0]:
            if canHitCoord not in root.shipClicked.canBroadside:
              root.shipClicked.canBroadside.append(canHitCoord)


  #displays orange box everywhere active ship can hit an enemy ship
  def renderCanHit(root, display, hitIcon, broadsideIcon):
    if root.shipClicked and root.shipClicked.canAtk:
      findCanHit(root)
      findCanBroadside(root)
      for point in root.shipClicked.canHit:
        if point not in root.shipClicked.canBroadside:
          display.blit(hitIcon, coordToPixel(point, root.gridWidth))
      for point in root.shipClicked.canBroadside:
        display.blit(broadsideIcon, coordToPixel(point, root.gridWidth))
    else:
      root.shipClicked.canHit = []

  
  def makeAttack(root, coord):
    if root.shipClicked and root.shipClicked.canAtk == True:
      ship = root.shipClicked
      ship.canAtk = False
      if coord in root.shipClicked.canBroadside:
        hits = 0
        for atk in range (0, ship.cannons):
          check = random.choice(range(1,6))
          print("fired, accuracy:", check)
          if((False, True)[check <= ship.accuracy]): #determine if hit by accuracy
            hits+=1
        print("shit hit ", hits, " Number of times")
        for shot in range (0, hits):
          root.attack.hp -= root.shipClicked.damage
          print("hit")
      else:
        miss = (False, True)[random.choice(range(1,6)) > ship.accuracy] #determine if hit by accuracy
        if not(miss):
          root.attack.hp -= root.shipClicked.damage
          print("hit")
        else:
          print("miss")
      print(root.attack.type, "Health after attack is", root.attack.hp)
      if root.attack.hp <= 0:
        root.allShips.remove(root.attack)
    root.attack = None
    root.shipClicked = None

  #checks to see if all other players ship are destoryed
  def checkForWinner(root):
    winner = root.allShips[0].owner
    for ship in root.allShips:
      if ship.owner != winner:
        return False
    print(winner)
    root.page = "GameOver"
    return winner

  def run_game():
    pygame.init()

    #background = (51, 70, 242)
    battlefieldBackground=pygame.image.load('./resources/images/background-battlefield.jpg').convert()
    hitIcon=pygame.image.load('./resources/images/Hit.png')
    broadsideIcon = pygame.image.load('./resources/images/Broadside.png')

    #Set GUI Size and title
    gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
    pygame.display.set_caption('Pirates PC!')
    clock = pygame.time.Clock()

    #Check for events
    while root.page == "Play":
      checkForWinner(root)
      root.mx = None
      root.my = None

      #check for if menu bar should be displayed
      if cursorLocated(0, 1920, -10, 10) and root.showMenu == False:
        root.showMenu = True
      elif root.showMenu == True and not(cursorLocated(0, 1920, -10, 30)):
        root.showMenu = False

      for event in pygame.event.get():

        #Monitor when mouse is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
          #if left mouse button is pressed, 
          #get position of mouse and save it as mx and my
          if (pygame.mouse.get_pressed()[0] == 1) and root.flagDrag== False:
            root.mx, root.my = pygame.mouse.get_pos()

            #if menu shown and click on a button perform specified action
            if cursorLocated(-1, 63, -1, 30) and root.showMenu:
              print(root.currentPlayer.getData() + "'s turn is over.")
              root.endTurn()
              print("It is now " + root.currentPlayer.getData() + "'s turn.")
              root.mx = None
              root.my = None
            elif cursorLocated(1856, 1921, -1, 30) and root.showMenu:
              print("Exiting Game")
              pygame.quit()
              exit()
        
          #If ship was clicked, set state of flagDrag to true
          if(root.mx != None):
            coord = pixelToCoord((root.mx, root.my), root.gridWidth)
            if root.shipClicked and coord in root.shipClicked.canHit:  #if clicked an attackable ship, make attack
                root.attack = getShip(coord, playerShips)
                makeAttack(root, coord)
            else:
              root.shipClicked = getShip(coord, playerShips)
              if(root.shipClicked):
                if root.shipClicked.owner != root.currentPlayer.getData():
                  root.shipClicked = False
                else:
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
          #activate ship instead of moving ship
          if coord in root.shipClicked.coords:
            print("Ship Active but not dragging")
            print("movement left", root.shipClicked.canMove)
            root.flagDrag = False
          else: #Move ship
            res = moveIsValid(root.shipClicked, (newMx, newMy))
            print("Move is valid: ", res)
            if(res):
              root.shipClicked.moveShip(root)
            root.flagDrag = False
            root.shipClicked = False
            root.path = Path()


      ##Render
      #Load and Fill Background
      gameDisplay.blit(battlefieldBackground, (0,0))

      if(root.path):
        root.path.renderArrow(gameDisplay, root)

      #Load Sprites
      for ship in playerShips:
        gameDisplay.blit(ship.image, ship.getPosition(root.gridWidth))
        ship.renderHealthBar(gameDisplay, root)
      if root.shipClicked:
        renderCanHit(root, gameDisplay, hitIcon, broadsideIcon) #ship shooting locations

      #Define text
      smallFont   = pygame.font.SysFont("Arial", 16, True)
      endTurn     = smallFont.render("End Turn", True, [0, 0, 0], None)
      exitGame    = smallFont.render("Exit Game", True, [0, 0, 0], None)

      #Show menu bar
      if root.showMenu == True:
        pygame.draw.rect(gameDisplay, (32,32,32), [0,0,display_width,30]) #draw grey bar
        pygame.draw.rect(gameDisplay, (105,105,105), [0,0,63,30]) #draw first menu option
        pygame.draw.rect(gameDisplay, (200,0,0), [1856,0,64,30]) #draw exit menu option
        gameDisplay.blit(endTurn, (1,3))
        gameDisplay.blit(exitGame, (1856,3))

      pygame.display.update()

      time.sleep(0.03)
  run_game()