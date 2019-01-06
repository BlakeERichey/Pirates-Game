##This is a testing page for debugging code and testing methods 
import pygame
import Play, common, StateClass
import components

from   Play       import Play
from   MainMenu   import main_menu
from   StateClass import State
from   common     import coordToPixel, isInt, isAdjacent, Node

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