from pyray import *

Background : Color = (128, 128, 128, 255)

init_window(1200, 720, "Testing text box")

class TextBox:
    def __init__(self):
        self.WrittenCharacters : str = ""
        self.LastUpdateTime : float = 0
        self.ShowLine : bool = False
        self.textsize = 24
        self.textPos = Vector2(0, 0)
        self.ButtonRec = Rectangle(400, 200, 400, 100)
        self.LinePos : Vector2 = Vector2(0, 0)
        self.LineEndPos : Vector2 = Vector2(0, 0)
        self.LineXOffset = 10
    
    def IsReady(self, Time : float):
        CurrentTime : float = get_time()
        if CurrentTime > self.LastUpdateTime + Time:
            self.ShowLine = not self.ShowLine
            self.LastUpdateTime = CurrentTime
        return None
    
    def ComputeCenterText(self):
        Textwidth = measure_text(self.WrittenCharacters, self.textsize)
        self.textPos = Vector2(self.ButtonRec.x + (self.ButtonRec.width - Textwidth) / 2,
                               self.ButtonRec.y + (self.ButtonRec.height - self.textsize) / 2)
        
    def ComputeLinePlace(self):
        Textwidth = measure_text(self.WrittenCharacters, self.textsize)
        self.LinePos.x = self.ButtonRec.x + (self.ButtonRec.width / 2) + Textwidth / 2 + self.LineXOffset
        self.LineEndPos.x = self.ButtonRec.x + (self.ButtonRec.width / 2) + Textwidth / 2 + self.LineXOffset
        self.LinePos.y = self.ButtonRec.y + 10
        self.LineEndPos.y = self.ButtonRec.y + self.ButtonRec.height - 10

    def Draw(self):
        draw_rectangle_rec(self.ButtonRec, WHITE)
        self.ComputeCenterText()
        self.ComputeLinePlace()
        draw_text(self.WrittenCharacters, int(self.textPos.x), int(self.textPos.y), self.textsize, BLACK)
        self.IsReady(0.5)
        if self.ShowLine:
            draw_line(int(self.LinePos.x), int(self.LinePos.y), int(self.LineEndPos.x), int(self.LineEndPos.y), BLACK)

moi : TextBox = TextBox()

while not window_should_close():
    begin_drawing() 
    moi.Draw()
    clear_background(Background)
    end_drawing()
close_window()