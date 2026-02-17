from pyray import *

class Label:
    def __init__(self) -> None:
        """
        Create a Label object, all parameters are default to 0, except character space which is 2.

        :return: None
        
        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity). \n
        Extras: - Font is a raylib structure holding a font file. \n
        Extras: - get_font_default() is a raylib method to get the font used by default by raylib.
        """
        self.Position : Vector2 = Vector2(0, 0)          # Position of the text

        self.Text : str = ""                             # Text to display
        self.TextSize : int = 0                          # Size of the text
        self.TextColor : Color = Color(0, 0, 0, 0)       # Color of the text

        self.Rotation : float = 0                        # Rotation of the text
        self.Origin : Vector2 = Vector2(0, 0)            # Origin point of the text
        self.CharacterSpacing : float = 2                # Space between each character
        self.Font : Font = get_font_default()            # Font to use

        self.UnderLine : bool = False                    # If the text should be underlined
        self.LineColor : Color = Color(0, 0, 0, 0)       # Color of the underline
        self.LineSpacing : float = 0                     # Space between the line and the text on the y axis
        self.LineThickness : float = 0                   # Thickness of the line
        self.LineBegin : Vector2 = Vector2(0, 0)         # Begin point of the underline
        self.LineEnd : Vector2 = Vector2(0, 0)           # End point of the underline
        self.TextDimensions : Vector2 = Vector2(0, 0)    # Width and height of the text.

        self.OverLine = False                            # If the text should be overlined
        self.OverLineColor : Color = Color(0, 0, 0, 0)   # Color of the overline

        self.BaseSize : Vector2 = Vector2(0, 0)     # The screen size it was made on.

        return None
    
    def Prepare(self, Source : dict, MenuName : str, ButtonName : str) -> None:
        """
        Does the calculations for the under line and overline placement. \n
        Load all the info needed for the label.
        
        :param Source: The dictionarry containing all Data.
        :type Source: dict
        :param MenuName: The name of the menu inside Data.py
        :type MenuName: str
        :param ButtonName: The name of the button inside Data.py
        :type ButtonName: str
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - Source refers to Data.py
        """
        Info : dict = Source[MenuName][ButtonName]

        self.Position = Info["Position"]
        self.BaseSize = Info["OriginalScreenSize"]
        self.Text = Info["Text"]
        self.TextSize = Info["TextSize"]
        self.TextColor = Info["TextColor"]
        self.Font = Info["Font"]
        self.Rotation = Info["Rotation"]
        self.Origin = Info["Origin"]
        self.CharacterSpacing = Info["CharacterSpacing"]
        self.Underline = Info["Underline"]
        self.LineColor = Info["LineColor"]
        self.LineSpacing = Info["LineSpacing"]
        self.LineThickness = Info["LineThickness"]
        self.Overline = Info["Overline"]
        self.OverlineColor = Info["OverlineColor"]

        if self.Overline or self.Underline:
            self.TextDimensions : Vector2 = measure_text_ex(self.Font, self.Text, self.TextSize, self.CharacterSpacing)
        if self.Underline:
            self.LineBegin : Vector2 = Vector2(self.Position.x, self.Position.y + self.TextDimensions.y + self.LineSpacing)
            self.LineEnd : Vector2 = Vector2(self.LineBegin.x + self.TextDimensions.x, self.LineBegin.y)
        return None
    
    def Scale(self, ScreenSize : Vector2) -> None:
        """
        Scale the label to the given screen size.
        
        :param ScreenSize: The size of the screen
        :type ScreenSize: Vector2
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        XFactor : float = ScreenSize.x / self.BaseSize.x
        YFactor : float = ScreenSize.y / self.BaseSize.y

        self.Position = Vector2(self.Position.x * XFactor,
                                self.Position.y * YFactor)
        self.TextDimensions = Vector2(self.TextDimensions.x * XFactor,
                                      self.TextDimensions.y * YFactor)
        self.BaseSize = ScreenSize
        self.TextSize = int(self.TextSize * YFactor)
        return None
    
    def Draw(self) -> None:
        """
        Draw the label and its overline and underline if needed.
        
        :return: None

        Extras: - draw_text_pro() is a raylib function to draw text with additionnal parameters. \n
        Extras: - draw_line_ex() is a raylib function to draw a line with additional parameters. \n
        Extras: - draw_rectangle() is a raylib function to draw a rectangle. \n
        Extras: - 1 is added to the dimensions to avoid rounding imperfection.
        """
        draw_text_pro(self.Font, self.Text, self.Position, self.Origin, self.Rotation, self.TextSize, self.CharacterSpacing, self.TextColor)
        if self.Underline:
            draw_line_ex(self.LineBegin, self.LineEnd, self.LineThickness, self.LineColor)
        if self.Overline:
            draw_rectangle(int(self.Position.x), int(self.Position.y), int(self.TextDimensions.x) + 1, int(self.TextDimensions.y) + 1, self.OverlineColor)
        return None
