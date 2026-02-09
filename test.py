from pyray import *
dedale = open("dedales.txt", "r")
laby = str(dedale.read())
print(laby[0:9])
init_window(800, 450, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world", 190, 200, 20, VIOLET)
    end_drawing()
close_window()

# Set-up : pip3 install raylib==5.5.0.3 --break-system-packages