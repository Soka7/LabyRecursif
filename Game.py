from pyray import *

class Game :
    def __init__(self):
        pass
    def Launch(self):
        init_window(800, 450, "Hello")
    def Update(self):
        while not window_should_close():
            begin_drawing()
            clear_background(WHITE)
            draw_text("Hello world", 190, 200, 20, VIOLET)
            end_drawing()
        close_window()