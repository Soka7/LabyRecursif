from pyray import *
from Game import Game
import os
import subprocess
import sys

Background : Color = (128, 128, 128, 255)
ScreenWidth : int = 1200
ScreenHeight : int = 720
Title : str = "A based maze solver !"

game : Game = Game()

init_window(ScreenWidth, ScreenHeight, Title) # Create the window

game.LoadMaze("dedales.txt")
game.LoadTextures("Textures/Sprites.png")
game.Prepare()                  
game.Maze.FindEntry()

while not window_should_close():
    begin_drawing()
    clear_background(Background)
    game.Draw()                                                     # Game drawing looping
    end_drawing()
    
game.PrepareToQuit()
close_window()

if os.name == "nt":  # Windows
    subprocess.Popen(f'start cmd /k python -c "for stuff in {game.Maze.LabyrinthArray}: print(stuff)"', shell=True)

# Set-up : pip3 install raylib==5.5.0.3 --break-system-packages
# Sources : https://electronstudio.github.io/raylib-python-cffi/README.html