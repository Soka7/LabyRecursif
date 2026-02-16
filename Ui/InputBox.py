from pyray import *

class InputBox:
    def __init__(self, BaseTexture : Rectangle) -> None:
        """
        Generate a InputBox object, all attributes are defauletd to None or 0

        :param BaseTexture: The location of the texture in the Atlas
        :type BaseTexture: Rectangle
        :return: None
        
        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height. \n
        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity). \n
        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        self.WrittenCharacters : str = ""                   # Characters displayed by the box
        self.MaxCharacters : int = 0                        # The Maximum amount of characters on the Input Box
        self.CharacterRange : tuple = (0, 0)                # The unicode character range that can be displayed
        self.ButtonLoc = Rectangle(0, 0, 0, 0)              # Location of the the box

        self.LastUpdateTime : float = 0                     # Time since the last time the line changed state
        self.ShowLine : bool = False                        # If the line should appear
        self.HasBeenClicked : bool = False                  # If the Input Box has been clicked 

        self.TextSize : int = 0                             # Size of the displayed text
        self.TextPos : Vector2 = Vector2(0, 0)              # Position of the text
        self.TextColor : Color = (0, 0, 0, 0)               # Color of the text (Black)

        self.LineBegin : Vector2 = Vector2(0, 0)            # Starting position of the line
        self.LineEnd : Vector2 = Vector2(0, 0)              # Ending position of the line
        self.LineOffset : Vector2 = Vector2(0, 0)           # Small off set to the line
        self.LineColor : Color = (0, 0, 0, 0)               # Color of the line (Black)
        self.LineCooldown : float = 0                       # Cooldown between each state switch of the line

        self.WelcomeText : str = ""                         # Text displayed when no characters are written.
        self.ShowWelcomeText : bool = True                  # If the welcome text should be displayed

        self.MaxCharacterWarning : bool = False             # If the max character warning should be displayed
        self.WarningPos : Vector2 = Vector2(0, 0)           # Position of the warning
        self.WarningText : str = ""                         # Message displayed by the warning
        self.WarningTextSize : int = 0                      # Font size of the warning text using default font
        self.WarningColor : Color = (0, 0, 0, 0)            # Color of the warning message

        self.BaseTexture : Rectangle = BaseTexture          # The location of the texture to use in the Atlas
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

    def CenterText(self, Text : str) -> None:
        """
        Center the text in the Input Box.
        
        :param Text: The text to cenetr inside the Input Box.
        :type Text: str
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - measure_text() is a raylib function returning the width of the text with the default font.
        """
        TextWidth : int = measure_text(Text, self.TextSize)
        self.TextPos = Vector2(self.ButtonLoc.x + (self.ButtonLoc.width - TextWidth) / 2,
                               self.ButtonLoc.y + (self.ButtonLoc.height - self.TextSize) / 2)
        return None
    
    def CenterWarning(self) -> None:
        """
        Center the warning text under the Input Box.
        
        :return: None

        Extras: - measure_text() is a raylib function returning the width of the text with the default font.
        """
        TextWidth : int = measure_text(self.WarningText, self.WarningTextSize)
        self.WarningPos.x = self.ButtonLoc.x + (self.ButtonLoc.width - TextWidth) / 2
        self.WarningPos.y = self.ButtonLoc.y + self.ButtonLoc.height
        return None

    def UpdateLinePlace(self) -> None:
        """
        Place the line right after the last written character.
        
        :return: None

        Extras: - measure_text() is a raylib function returning the width of the text with the default font.
        Extras: - The texture is 23 pixels height and 11 of them are for the text, so 9 will be used to draw text on it.
        """
        LineLenght : int = int(self.ButtonLoc.height * (9 / 23))
        TextWidth = measure_text(self.WrittenCharacters, self.TextSize)
        self.LineBegin.x = self.ButtonLoc.x + (self.ButtonLoc.width / 2) + TextWidth / 2 + self.LineOffset.x
        self.LineEnd.x = self.LineBegin.x

        self.LineBegin.y = self.ButtonLoc.y + self.LineOffset.y + (self.ButtonLoc.height - LineLenght) / 2
        self.LineEnd.y = self.LineBegin.y + LineLenght
        return None
    
    def IsCharacterValid(self, Character : int) -> bool:
        """
        Check if a character should be displayed.
        
        :param Character: The unicode of the character
        :type Character: int
        :return: If the character can be displayed or not
        :rtype: bool

        Extras: - Number corresponds to "!" from "~" in the unicode table.
        """
        if self.CharacterRange[0] <= Character and Character <= self.CharacterRange[1]:
            return True
        return False
    
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
        elif is_key_pressed(KEY_ENTER):
            self.HasBeenClicked = False
            return None

        UnicodeCharacter : int = get_char_pressed()

        # get_char_pressed() returns 0 if nothing is pressed
        if UnicodeCharacter == 0 or len(self.WrittenCharacters) == self.MaxCharacters:
            return None
        elif not self.IsCharacterValid(UnicodeCharacter):
            return None

        self.WrittenCharacters += chr(UnicodeCharacter)
        return None

    def Update(self) -> None:
        """
        Update the differents state of the Input box.
        
        :return: None
        """
        if self.IsHovered() and self.IsClicked():
            self.HasBeenClicked = True
        elif self.IsClicked() and not self.IsHovered():
            self.HasBeenClicked = False
        
        if self.HasBeenClicked and self.IsReady(self.LineCooldown):
            self.ShowLine = not self.ShowLine

        if len(self.WrittenCharacters) == 0:
            self.ShowWelcomeText = True
            self.CenterText(self.WelcomeText)
        else:
            self.ShowWelcomeText = False

        if len(self.WrittenCharacters) == self.MaxCharacters:
            self.MaxCharacterWarning = True
        else:
            self.MaxCharacterWarning = False

        self.GetPlayerInput()
        return None
    
    def DrawContent(self) -> None:
        """
        Draw the text of the Input Box.
        
        :return: None

        Extras: - draw_text() is a raylib function to draw text.
        """
        if self.ShowWelcomeText:
            draw_text(self.WelcomeText, int(self.TextPos.x), int(self.TextPos.y), self.TextSize, self.TextColor)
            return None
        
        self.CenterText(self.WrittenCharacters)
        draw_text(self.WrittenCharacters, int(self.TextPos.x), int(self.TextPos.y), self.TextSize, self.TextColor)

        if self.MaxCharacterWarning:
            draw_text(self.WarningText, int(self.WarningPos.x), int(self.WarningPos.y), self.WarningTextSize, self.WarningColor)
        return None

    def Draw(self, Atlas : Texture) -> None:
        """
        Draw the Input Box and all its content.

        :param Atlas: The texture holding all the game's sprites.
        :type Atlas: Texture
        :return: None

        Extras: - draw_line_ex() is a raylib function to draw a line. \n
        Extras: - In this project Atlas refers to Sprites.png \n
        Extras: - Texture is a raylib structure being an image loaded in memory. \n
        Extras: - draw_texture_pro() is a raylib method to draw a texture with more flexibility.
        """
        Origin : Vector2 = Vector2(0, 0)
        Rotation : int = 0
        draw_texture_pro(Atlas, self.BaseTexture, self.ButtonLoc, Origin, Rotation, WHITE)
        self.DrawContent()

        if not self.HasBeenClicked:
            return None
        
        self.UpdateLinePlace()
        if self.ShowLine:
            draw_line_ex(self.LineBegin, self.LineEnd, 1, self.LineColor) # 1 stands for line thickness
        return None
    
    def Prepare(self) -> None:
        """
        Call the function that should be called once after creating the object.
        
        :return: None
        """
        self.CenterWarning()
        self.CenterText(self.WelcomeText)
        return None
    
    def EditCharacters(self, MaxAmount : int = 9, Range : tuple = (33, 126)) -> None:
        """
        Edit the maximum amount of characters in the Input Box and their unicode range.
        
        :param MaxAmount: Maximum amount of characters displayable
        :type MaxAmount: int
        :param Range: Start and end of the available unicode.
        :type Range: tuple
        :return: None

        Extras: - The Range argument must be a tuple(a, b) where a < b.
        """
        self.MaxCharacters = MaxAmount
        self.CharacterRange = Range
        return None
    
    def EditPos(self, Dimensions : Rectangle) -> None:
        """
        Edit the button x and y and width and height.
        
        :param Dimensions: The x and y position of the button and width and height.
        :type Dimensions: Rectangle
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        self.ButtonLoc = Dimensions
        return None
    
    def EditText(self, TextSize : int = 24, TextColor : Color = BLACK) -> None:
        """
        Edit the size and color of the displayed text.
        
        :param TextSize: The size of the text
        :type TextSize: int
        :param TextColor: The color of the text
        :type TextColor: Color
        :return: None

        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity). \n
        Extras: - Using default font.
        """
        self.TextSize = TextSize
        self.TextColor = TextColor
        return None
    
    def EditLine(self, LineOffset : Vector2 = Vector2(5, 0), LineCooldown : float = 0.5, LineColor : Color = BLACK) -> None:
        """
        Edit line offset, switch cooldown and color.
        
        :param LineOffset: Special offset used after centering the line
        :type LineOffset: Vector2
        :param LineCooldown: Time between the line goes from visible to invisible (in seconds)
        :type LineCooldown: float
        :param LineColor: Color of the line
        :type LineColor: Color
        :return: None

        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity). \n
        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        self.LineOffset = LineOffset
        self.LineCooldown = LineCooldown
        self.LineColor = LineColor
        return None
    
    def EditWelcome(self, WelcomeText : str = "Enter Text : ") -> None:
        """
        Edit the welcome message of the Input Box.
        
        :param WelcomeText: Welcome message displayed when nothing is written
        :type WelcomeText: str
        :return: None
        """
        self.WelcomeText = WelcomeText
        return None
    
    def EditWarning(self, WarningText : str = "Limit Reached !", TextSize : int = 16, WarningColor : Color = RED) -> None:
        """
        Edit the text, size, and color of the warning.
        
        :param WarningText: The text displayed by the warning
        :type WarningText: str
        :param TextSize: The size of the warning text
        :type TextSize: int
        :param WarningColor: The color of the warning text
        :type WarningColor: Color
        :return: None

        Extras: - Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity). \n
        Extras: - Using default font.
        """
        self.WarningText = WarningText
        self.WarningTextSize = TextSize
        self.WarningColor = WarningColor
        return None
    
    def GetInput(self) -> str:
        """
        Return what was written inside the Input Box.
        
        :return: The characters written inside the Input Box
        :rtype: str
        """
        return self.WrittenCharacters