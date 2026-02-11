from pyray import *
from Game import Game
from Menus import MainMenu

Background : Color = (255, 255, 255, 255)
ScreenWidth : int = 1200
ScreenHeight : int = 720
Title : str = "A based maze solver !"

game : Game = Game()
moi = MainMenu()
moi.EditHoverAll()
moi.EditPosAll()
moi.EditTextAll()

init_window(ScreenWidth, ScreenHeight, Title)

game.LoadMaze("dedales.txt")
game.Maze.FindEntry()

while not window_should_close():
    begin_drawing()
    clear_background(Background)
    game.Draw()
    moi.Draw()
    end_drawing()

close_window()

# Set-up : pip3 install raylib==5.5.0.3 --break-system-packages
# Sources : https://electronstudio.github.io/raylib-python-cffi/README.html