from pyray import *
from Game import *

Background : Color = (255, 255, 255, 255)
ScreenWidth : int = 800
ScreenHeight : int = 450
Title : str = "A based maze solver !"

game : Game = Game()

init_window(ScreenWidth, ScreenHeight, Title)

game.LoadMaze("dedales.txt")
game.Maze.FindEntry()

while not window_should_close():
    begin_drawing()
    clear_background(Background)
    game.Draw()
    end_drawing()

close_window()

# Set-up : pip3 install raylib==5.5.0.3 --break-system-packages