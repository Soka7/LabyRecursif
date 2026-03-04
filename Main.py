from pyray import *
from Game import Game

BackgroundColor : Color = (128, 128, 128, 255) # RGBA code
ScreenWidth : int = 1200
ScreenHeight : int = 720
Title : str = "A based maze solver !"

game : Game = Game()

init_window(ScreenWidth, ScreenHeight, Title) # Create the window

game.Prepare() # Prepare all the game's elements

# game loop
###### Si le chemin observe ne semble pas etre le meilleur il est conseille de relancer la resolution du labyrinthe
while not window_should_close():
    game.Update()
    if game.ShouldClose:
        break
    # draw loop
    begin_drawing()
    clear_background(BackgroundColor)
    game.Draw()
    end_drawing()

if not game.ShouldClose:
    game.PrepareToQuit()
close_window()