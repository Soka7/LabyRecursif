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

        return None
    
    def Prepare(self) -> None:
        """
        Does the calculations for the under line and overline placement.
        
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - Must be called once after setting everything up
        """
        if self.OverLine or self.UnderLine:
            self.TextDimensions : float = measure_text_ex(self.Font, self.Text, self.TextSize, self.CharacterSpacing)
        if self.UnderLine:
            self.LineBegin : Vector2 = Vector2(self.Position.x, self.Position.y + self.TextDimensions.y + self.LineSpacing)
            self.LineEnd : Vector2 = Vector2(self.LineBegin.x + self.TextDimensions.x, self.LineBegin.y)
        return None
    
    def SetUnderLine(self, LineColor : Color, LineSpacing : float, LineThickness : float) -> None:
        """
        Set the parameters for the line under the text.
        
        :param LineColor: Color of the line
        :type LineColor: Color
        :param LineSpacing: Space between the line and the text on the y axis
        :type LineSpacing: float
        :param LineThickness: Thickness of the line in pixels
        :type LineThickness: float
        :return: None

        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity).
        """
        self.UnderLine = True
        self.LineColor = LineColor
        self.LineSpacing = LineSpacing
        self.LineThickness = LineThickness
        return None
    
    def SetOverLine(self, OverLineColor : Color) -> None:
        """
        Set the parameters for the rectangle on the text.
        
        :param OverLineColor: Color of the rectangle
        :type OverLineColor: Color
        :return: None

        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity).
        """
        self.OverLine = True
        self.OverLineColor = OverLineColor
        return None
    
    def EditPos(self, Position : Vector2) -> None:
        """
        Edit the position of the text upper left corner.
        
        :param Position: The position of the upper left corner of the text
        :type Position: Vector2
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        self.Position = Position
        return None
    
    def EditText(self, Text : str, TextSize : int, TextColor : Color) -> None:
        """
        Edit the text displayed by the label.
        
        :param Text: The text to display
        :type Text: str
        :param TextSize: The size of the text
        :type TextSize: int
        :param TextColor: The color of the text
        :type TextColor: Color
        :return: None

        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity).
        """
        self.Text = Text
        self.TextSize = TextSize
        self.TextColor = TextColor
        return None
    
    def EditAdvancedText(self, Font : Font, Rotation : float, Origin : Vector2, Spacing : float) -> None:
        """
        Give advanced parameters to the text.
        
        :param Font: The font to use
        :type Font: Font
        :param Rotation: The rotation in degrees of the text
        :type Rotation: float
        :param Origin: The origin of the text
        :type Origin: Vector2
        :param Spacing: The space between each character
        :type Spacing: float
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - Font is a raylib structure holding a font file. \n
        Extras: - The rotation must be in degrees. \n
        Extras: - Rotated text can't be underlined or overlined.
        """
        self.Font = Font
        self.Rotation = Rotation
        self.Origin = Origin
        self.CharacterSpacing = Spacing
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
        if self.UnderLine:
            draw_line_ex(self.LineBegin, self.LineEnd, self.LineThickness, self.LineColor)
        if self.OverLine:
            draw_rectangle(int(self.Position.x), int(self.Position.y), int(self.TextDimensions.x) + 1, int(self.TextDimensions.y) + 1, self.OverLineColor)
        return None
