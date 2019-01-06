##This is a testing page for debugging code and testing methods 
import pygame
import components.Play, components.common, components.StateClass

from   components.Play       import Play
from   components.StateClass import State
from   components.MainMenu   import main_menu
from   components.common     import coordToPixel, isInt, isAdjacent, Node

def run_game():
  root = State()
  pygame.init()

  #Check for events
  while True:
    if root.page == "Play":
      Play(root)
    elif root.page == "Menu":
      main_menu(root)

run_game()