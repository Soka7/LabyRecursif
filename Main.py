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
    if game.ShouldClose:
        break
    begin_drawing()
    clear_background(Background)
    game.Draw()
    end_drawing()

if not game.ShouldClose:
    game.PrepareToQuit()
close_window()


# - Set-up : pip3 install raylib==5.5.0.3 --break-system-packages
# - Sources : https://electronstudio.github.io/raylib-python-cffi/README.html
# - Camera2D overview : https://youtu.be/zkjDU3zmk40
# - Camera Code example and additional details : https://www.raylib.com/examples/core/loader.html?name=core_2d_camera
# - Software for pixel art : PixiEditor
# - Help for the saving system : https://www.w3schools.com/python/python_file_write.asp

# On the work (You better do it) :
# - Importing a maze
# - Add a back ground image

# Optional fixes (if you don't know what to do ) :
# - Make the user able to hold space to delete characters (input box)
# - Check doctsrings (potential mistakes / extra informations)
# - Make the apply button usable with enter (settings menu)
# - Make the possibility to have custom fonts (Label)
# - Make the fps drawing an actual function and make it clearer
# - Make the camera not center when you right click (editor screen)                             # REALLY IMPORTANT #
# - Better ui information (show what you have selected) (editor screen)
# - Add a way to hold ctrl z and ctrl y (editor screen)
# - Add a way to hold the mouse to place (editor screen)
# - Add a warning when the open button is pressed to tell the user than there is no maze or whatever
# - Music ?
# - Make underlining multiple lines of text possible (label)
