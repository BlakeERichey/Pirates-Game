##This is the primary executable for the game. 
import pygame
import components.Play, components.common, components.StateClass

from   components.Play       import Play
from   components.Setup      import Setup
from   components.StateClass import State
from   components.MainMenu   import main_menu
from   components.GameOver   import GameOver
from   components.common     import coordToPixel, isInt, isAdjacent, Node

def run_game():
  root = State()
  pygame.init()
  # root.page = "GameOver"

  #Determine which page to display
  while True:
    if root.page == "Play":
      Play(root)
    elif root.page == "Setup":
      Setup(root)
    elif root.page == "Menu":
      main_menu(root)
    elif root.page == "GameOver":
      GameOver(root)

run_game()