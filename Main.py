from pyray import *
from Game import *
from Button import *

Background : Color = (255, 255, 255, 255)
ScreenWidth : int = 800
ScreenHeight : int = 450
Title : str = "A based maze solver !"

game : Game = Game()

init_window(ScreenWidth, ScreenHeight, Title)

bouton = Button()
bouton.EditPos(Vector2(0, 0), Vector2(100, 100))
bouton.EditText("Moi", 28, (255, 255, 255, 255))
bouton.EditHover(10, (255, 0, 0, 255))

game.LoadMaze("dedales.txt")
game.Maze.FindEntry()

while not window_should_close():
    begin_drawing()
    clear_background(Background)
    if bouton.IsClicked():
        print("moi")
    game.Draw()
    bouton.Draw()
    end_drawing()

close_window()

# Set-up : pip3 install raylib==5.5.0.3 --break-system-packages