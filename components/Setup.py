##Setup ships for player 1 and player 2
import pygame
import components.common, components.SetupState, components.ShipClass
from components.ShipClass  import Ship
from components.SetupState import SetupState
from components.common import coordToPixel, isInt, isAdjacent, Node, pixelToCoord

def Setup(root):
  pygame.init()
  state = SetupState()

  background = (51, 70, 242)
  cargo=pygame.image.load('./resources/images/Icon_Cargo.png')
  galley=pygame.image.load('./resources/images/Icon_Galley.png')
  schooner=pygame.image.load('./resources/images/Icon_Schooner.png')
  battlefieldBackground=pygame.image.load('./resources/images/background-battlefield.jpg')

  display_width = 1920
  display_height = 1080

  #Set GUI Size and title
  gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
  pygame.display.set_caption('Pirates PC!')
  clock = pygame.time.Clock()

  #Check for events
  while root.page=="Setup":

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      #Monitor when keyboard key is pressed
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          exit()

      #Left mouse button is clicked
      if event.type == pygame.MOUSEBUTTONDOWN:
        if (pygame.mouse.get_pressed()[0] == 1):
          mx, my = pygame.mouse.get_pos()
          if mx >= 480 and mx < 530 and my > 280 and my < 330:
            state.addShip("Schooner")
            print(state.schoonerQty)
          if mx >= 250 and mx < 295 and my > 280 and my < 330:
            state.subShip("Schooner")
          if mx >= 480 and mx < 530 and my > 472 and my < 522:
            state.addShip("Cargo")
          if mx >= 250 and mx < 295 and my > 472 and my < 522:
            state.subShip("Cargo")
          if mx >= 480 and mx < 530 and my > 664 and my < 714:
            state.addShip("Galley")
          if mx >= 250 and mx < 295 and my > 664 and my < 714:
            state.subShip("Galley")

          #submit - add ships for player 1 to root.player1Ships
          if mx >= 850 and mx < 950 and my > 900 and my < 950:
            currentPos = 1
            for qty in range(0, state.schoonerQty):
              tempShip = Ship("Schooner", (currentPos, 1))
              tempShip.setDir("down")
              tempShip.setCoords()
              tempShip.setImagePos()
              tempShip.healthBar.move(tempShip)
              root.player1Ships.append(tempShip)
              currentPos+=1
            for qty in range(0, state.cargoQty):
              tempShip = Ship("Cargo", (currentPos, 2))
              tempShip.setDir("down")
              tempShip.setCoords()
              tempShip.setImagePos()
              tempShip.healthBar.move(tempShip)
              root.player1Ships.append(tempShip)
              currentPos+=1
            for qty in range(0, state.galleyQty):
              tempShip = Ship("Galley", (currentPos, 2))
              tempShip.setDir("down")
              tempShip.setCoords()
              tempShip.setImagePos()
              tempShip.healthBar.move(tempShip)
              root.player1Ships.append(tempShip)
              currentPos+=1
            root.page = "SetupPlayer2" #continue to setting up player2 ships
            SetupPlayer2(root)
             

    gameDisplay.fill(background)
    gameDisplay.blit(battlefieldBackground, (0,0))

    #Define text
    font        = pygame.font.SysFont("Arial", 70, True)
    smallFont   = pygame.font.SysFont("Arial", 24, True)
    subtract    = font.render("–", True, [0, 0, 0], None)
    cargoQty    = font.render(str(state.cargoQty), True, [0, 0, 0], None)
    galleyQty   = font.render(str(state.galleyQty), True, [0, 0, 0], None)
    schoonerQty = font.render(str(state.schoonerQty), True, [0, 0, 0], None)
    addition    = pygame.font.SysFont("Arial", 80, True).render("  +", True, [0, 0, 0], None)
    pointsLeft  = font.render("Points Left: " + str(state.pointsLeft), True, [0, 0, 0], None)
    submit      = smallFont.render("Submit", True, [0, 0, 0], None)
    player1     = font.render("Player 1", True, [0,0,0], None)

    #Render Button
    pygame.draw.rect(gameDisplay, (105,105,105), [850,900,100,50]) #draw grey button

    #Render text
    gameDisplay.blit(pointsLeft, (700,0))
    gameDisplay.blit(cargoQty, (1500, 437))
    gameDisplay.blit(galleyQty, (1500, 636))
    gameDisplay.blit(schoonerQty, (1500, 270))
    gameDisplay.blit(subtract, coordToPixel((5,5), None))
    gameDisplay.blit(addition, coordToPixel((8,5), None))
    gameDisplay.blit(subtract, coordToPixel((5,8), None))
    gameDisplay.blit(addition, coordToPixel((8,8), None))
    gameDisplay.blit(subtract, coordToPixel((5,11), None))
    gameDisplay.blit(addition, coordToPixel((8,11), None))
    gameDisplay.blit(player1, (800, 800))
    gameDisplay.blit(submit, (865, 910))

    #Render ships
    gameDisplay.blit(cargo, (350, 405))
    gameDisplay.blit(galley, (350, 604))
    gameDisplay.blit(schooner, (350, 270))

    pygame.display.update()

    def SetupPlayer2(root):
      pygame.init()
      state = SetupState()

      background = (51, 70, 242)
      cargo=pygame.image.load('./resources/images/Icon_Cargo.png')
      galley=pygame.image.load('./resources/images/Icon_Galley.png')
      schooner=pygame.image.load('./resources/images/Icon_Schooner.png')
      battlefieldBackground=pygame.image.load('./resources/images/background-battlefield.jpg')

      display_width = 1920
      display_height = 1080
      rows=int(display_height/root.gridWidth) + 1
      cols=int(display_width/root.gridWidth)


      #Set GUI Size and title
      gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
      pygame.display.set_caption('Pirates PC!')
      clock = pygame.time.Clock()
      while root.page=="SetupPlayer2":

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()

          #Monitor when keyboard key is pressed
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              pygame.quit()
              exit()

          #Left mouse button is clicked
          if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pressed()[0] == 1):
              mx, my = pygame.mouse.get_pos()
              if mx >= 480 and mx < 530 and my > 280 and my < 330:
                state.addShip("Schooner")
                print(state.schoonerQty)
              if mx >= 250 and mx < 295 and my > 280 and my < 330:
                state.subShip("Schooner")
              if mx >= 480 and mx < 530 and my > 472 and my < 522:
                state.addShip("Cargo")
              if mx >= 250 and mx < 295 and my > 472 and my < 522:
                state.subShip("Cargo")
              if mx >= 480 and mx < 530 and my > 664 and my < 714:
                state.addShip("Galley")
              if mx >= 250 and mx < 295 and my > 664 and my < 714:
                state.subShip("Galley")

              #submit - add ships for player 2 to root.player2Ships
              if mx >= 850 and mx < 950 and my > 900 and my < 950:
                currentPos = 30
                for qty in range(0, state.galleyQty):
                  tempShip = Ship("Galley", (currentPos, rows-1))
                  tempShip.owner="Player2"
                  root.player2Ships.append(tempShip)
                  currentPos-=1
                for qty in range(0, state.cargoQty):
                  tempShip = Ship("Cargo", (currentPos, rows-1))
                  tempShip.owner="Player2"
                  root.player2Ships.append(tempShip)
                  currentPos-=1
                for qty in range(0, state.schoonerQty):
                  tempShip = Ship("Schooner", (currentPos, rows))
                  tempShip.owner="Player2"
                  root.player2Ships.append(tempShip)
                  currentPos-=1
                root.page = "Play" #proceed to game
                

        gameDisplay.fill(background)
        gameDisplay.blit(battlefieldBackground, (0,0))

        #Define text
        font        = pygame.font.SysFont("Arial", 70, True)
        smallFont   = pygame.font.SysFont("Arial", 24, True)
        subtract    = font.render("–", True, [0, 0, 0], None)
        cargoQty    = font.render(str(state.cargoQty), True, [0, 0, 0], None)
        galleyQty   = font.render(str(state.galleyQty), True, [0, 0, 0], None)
        schoonerQty = font.render(str(state.schoonerQty), True, [0, 0, 0], None)
        addition    = pygame.font.SysFont("Arial", 80, True).render("  +", True, [0, 0, 0], None)
        pointsLeft  = font.render("Points Left: " + str(state.pointsLeft), True, [0, 0, 0], None)
        submit      = smallFont.render("Submit", True, [0, 0, 0], None)
        player1     = font.render("Player 2", True, [0,0,0], None)

        #Render Button
        pygame.draw.rect(gameDisplay, (105,105,105), [850,900,100,50]) #draw grey button

        #Render text
        gameDisplay.blit(pointsLeft, (700,0))
        gameDisplay.blit(cargoQty, (1500, 437))
        gameDisplay.blit(galleyQty, (1500, 636))
        gameDisplay.blit(schoonerQty, (1500, 270))
        gameDisplay.blit(subtract, coordToPixel((5,5), None))
        gameDisplay.blit(addition, coordToPixel((8,5), None))
        gameDisplay.blit(subtract, coordToPixel((5,8), None))
        gameDisplay.blit(addition, coordToPixel((8,8), None))
        gameDisplay.blit(subtract, coordToPixel((5,11), None))
        gameDisplay.blit(addition, coordToPixel((8,11), None))
        gameDisplay.blit(player1, (800, 800))
        gameDisplay.blit(submit, (865, 910))

        #Render ships
        gameDisplay.blit(cargo, (350, 405))
        gameDisplay.blit(galley, (350, 604))
        gameDisplay.blit(schooner, (350, 270))

        pygame.display.update()