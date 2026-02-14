from pyray import *

Background : Color = (128, 128, 128, 255)

init_window(1200, 720, "Testing text box")

class TextBox:
    def __init__(self) -> None:
        """
        Generate a TextBox object, all attributes are defauletd to None or 0
        
        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity).
        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        self.WrittenCharacters : str = ""                   # Characters displayed by the box   
        self.ButtonLoc = Rectangle(400, 200, 400, 100)      # Location of the the box

        self.LastUpdateTime : float = 0                     # Time since the last time the line changed state
        self.LineCooldown : float = 0.5                     # Cooldown between each state switch of the line
        self.ShowLine : bool = False                        # If the line should appear
        self.HasBeenClicked : bool = False                  # If the text box has been clicked 

        self.TextSize : int = 24                            # Size of the displayed text
        self.TextPos : Vector2 = Vector2(0, 0)              # Position of the text
        self.TextColor : Color = (0, 0, 0, 255)             # Color of the text (Black)

        self.LineBegin : Vector2 = Vector2(0, 0)            # Starting position of the line
        self.LineEnd : Vector2 = Vector2(0, 0)              # Ending position of the line
        self.LineOffset : Vector2 = Vector2(10, 10)         # Small off set to the line
        self.LineColor : Color = (0, 0, 0, 255)             # Color of the line (Black)
        return None
    
    def IsReady(self, Cooldown : float) -> bool:
        """
        Check if a timer is finished or not.
        
        :param Cooldown: The timer's coolwon in seconds
        :type Cooldown: float
        :return: If the timer is over or not
        :rtype: bool

        Extras: - get_time() is a raylib function returning the time in seconds since the window is open.
        """
        CurrentTime : float = get_time()
        if CurrentTime > self.LastUpdateTime + Cooldown:
            self.LastUpdateTime = CurrentTime
            return True
        return False
    
    def IsHovered(self) -> bool:
        """
        Check if the mouse is on the button.
        
        :return: If the mouse is on the button or not
        :rtype: bool

        Extras: - check_collision_point_rec() is a raylib function checking if a point is inside a rectangle. \n
        Extras: - get_mouse_position() is a raylib function returning a Vector2 holding the x and y position of the mouse.
        """
        if check_collision_point_rec(get_mouse_position(), (self.ButtonLoc.x, self.ButtonLoc.y,
                                                            self.ButtonLoc.width, self.ButtonLoc.height)):
            return True
        return False
    
    def IsClicked(self) -> bool:
        """
        Check if the left mouse button has been clicked.
        
        :return: If the left mouse button has been clicked.
        :rtype: bool

        Extras: - is_mouse_button_pressed() is a raylib function checking if a button of the mouse has been pressed. \n
        Extras: - MouseButton.MOUSE_BUTTON_LEFT is a raylib data that refers to the left mouse button
        """
        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            return True
        return False

    def CenterText(self) -> None:
        """
        Center the text in the text box.
        
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - measure_text() is a raylib function returning the width of the text with the default font.
        """
        TextWidth : float = measure_text(self.WrittenCharacters, self.TextSize)
        self.TextPos = Vector2(self.ButtonLoc.x + (self.ButtonLoc.width - TextWidth) / 2,
                               self.ButtonLoc.y + (self.ButtonLoc.height - self.TextSize) / 2)
        return None
        
    def UpdateLinePlace(self) -> None:
        """
        Place the line right after the last written character.
        
        :return: None

        Extras: - measure_text() is a raylib function returning the width of the text with the default font.
        """
        TextWidth = measure_text(self.WrittenCharacters, self.TextSize)
        self.LineBegin.x = self.ButtonLoc.x + (self.ButtonLoc.width / 2) + TextWidth / 2 + self.LineOffset.x
        self.LineEnd.x = self.ButtonLoc.x + (self.ButtonLoc.width / 2) + TextWidth / 2 + self.LineOffset.x
        self.LineBegin.y = self.ButtonLoc.y + self.LineOffset.y
        self.LineEnd.y = self.ButtonLoc.y + self.ButtonLoc.height - self.LineOffset.y
        return None
    
    def GetPlayerInput(self) -> None:
        """
        Get the character pressed by the player.
        
        :return: None

        Extras: - is_key_pressed() is a raylib function that check if a keyboard key has been pressed. \n
        Extras: - KEY_BACKSPACE refers to the key to delete characters. \n
        Extras: - get_char_pressed() returns the unicode of the character pressed on the keyboard.
        """
        if not self.HasBeenClicked:
            return None

        # Handle character deletion
        if is_key_pressed(KEY_BACKSPACE):
            self.WrittenCharacters = self.WrittenCharacters[:-1]
            return None

        UnicodeCharacter : int = get_char_pressed()

        # get_char_pressed() returns 0 if nothing is pressed
        if UnicodeCharacter == 0:
            return None

        self.WrittenCharacters += chr(UnicodeCharacter)
        return None

    def Update(self) -> None:
        """
        Update the differents state of the textbox.
        
        :return: None
        """
        if self.IsHovered() and self.IsClicked():
            self.HasBeenClicked = True
        elif self.IsClicked() and not self.IsHovered():
            self.HasBeenClicked = False
        
        if self.HasBeenClicked and self.IsReady(self.LineCooldown):
            self.ShowLine = not self.ShowLine

        self.GetPlayerInput()
        return None
    
    def DrawContent(self) -> None:
        """
        Draw the text of the text box.
        
        :return: None

        Extras: - draw_text() is a raylib function to draw text.
        """
        self.CenterText()
        draw_text(self.WrittenCharacters, int(self.TextPos.x), int(self.TextPos.y), self.TextSize, self.TextColor)
        return None

    def Draw(self) -> None:
        """
        Draw the text box and all its content.

        :return: None

        Extras: draw_line_ex() is a raylib function to draw a line.
        """
        draw_rectangle_rec(self.ButtonLoc, WHITE)
        self.DrawContent()

        if not self.HasBeenClicked:
            return None
        
        self.UpdateLinePlace()
        if self.ShowLine:
            draw_line_ex(self.LineBegin, self.LineEnd, 1, self.LineColor) # 1 stands for line thickness
        return None
        

text : TextBox = TextBox()

while not window_should_close():
    text.Update()
    begin_drawing() 
    text.Draw()
    clear_background(Background)
    end_drawing()
close_window()
