def Pirates():   
    ##GUI Main Game
    import pygame, time, sys
    import ShipClass
    from   ShipClass import Ship
    
    gamePadCoordinate = ""

    def run_game():
        pygame.init()

        #background = (51, 70, 242)
        battlefieldBackground=pygame.image.load('./resources/images/background-battlefield.jpg')

        #Sprites Resources
        galleySprite = pygame.image.load('./resources//images/Icon_Galley.png')
        schSprite    = pygame.image.load('./resources//images/Icon_Schooner.png')

        display_width = 1920
        display_height = 1080

        #Load and Fill Background
        gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
        pygame.display.set_caption('Pirates PC!')
        clock = pygame.time.Clock()
        #gameDisplay.fill(background)
        gameDisplay.blit(battlefieldBackground, (0,0))

        #Set Player Ships
        x = Ship("Schooner")
        x.pos=(3,3)
        Player1Ships = [x]    
        
        #Load Sprites
        for ship in Player1Ships:
          if(ship.type == "Galley"):
              gameDisplay.blit(galleySprite, ship.getPosition())
          if(ship.type == "Schooner"):
              gameDisplay.blit(schSprite, ship.getPosition())

        pygame.display.update()

        #Check for events
        while True:
        
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
              #get position of mouse and save it ss mx and my
              mx, my = pygame.mouse.get_pos()
            
              for x in Player1Ships:
                print((x.pos[0] - 1)*64)
                print(mx)
                if (x.pos[0] - 1)*64<mx and x.pos[0]*64>mx:
                  print("You hit!")
              
            if event.type == pygame.MOUSEBUTTONUP:
              print("key lifted")
              newMx, newMy = pygame.mouse.get_pos()
              
              Player1Ships[0].setPosition((newMx, newMy))
              print(Player1Ships[0].pos)

          #Load and Fill Background
          gameDisplay.blit(battlefieldBackground, (0,0))

          #Load Sprites
          for ship in Player1Ships:
            if(ship.type == "Galley"):
                gameDisplay.blit(galleySprite, ship.getPosition())
            if(ship.type == "Schooner"):
                gameDisplay.blit(schSprite, ship.getPosition())
          
          #Rerender
          pygame.display.update()

          time.sleep(0.03)
    run_game()

Pirates()
