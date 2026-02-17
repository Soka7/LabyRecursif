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


# Set-up : pip3 install raylib==5.5.0.3 --break-system-packages
# Sources : https://electronstudio.github.io/raylib-python-cffi/README.html

# Optional fixes (if you don't know what to do ) :
# - Make the user able to hold space to delete characters (input box)
# - PressedHover Texture for the button (button)
# - Make the warning appear when the user tries to type more than the max character (input box)
# - Check doctsrings (potential mistakes / extra informations)
# - Make the apply button usable with enter (settings menu)
# - Rename the position argument (containing x,y,width,height) to one same thing across all classes
# - Make the possibility to have custom fonts (Label)
# - Make the fps drawing an actual function and make it clearer