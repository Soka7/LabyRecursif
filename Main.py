from pyray import *
from Game import Game

Background : Color = (128, 128, 128, 255)
ScreenWidth : int = 1200
ScreenHeight : int = 720
Title : str = "A based maze solver !"

game : Game = Game()

init_window(ScreenWidth, ScreenHeight, Title) # Create the window

game.Prepare()

while not window_should_close():
    game.Update()
    begin_drawing()
    clear_background(Background)
    game.Draw()                                                     # Game drawing loop
    end_drawing()
    if game.ShouldClose:
        break

if not game.ShouldClose:
    game.PrepareToQuit()
close_window()


# Set-up : pip3 install raylib==5.5.0.3 --break-system-packages
# Sources : https://electronstudio.github.io/raylib-python-cffi/README.html

# NOTE : ADD PYRAY FUNCTIONS TO DOCSTRINGS

# On the work :, Fix the bug when quitting, finish settings menu, also fix input box to show the warning when a character is typed at the limit