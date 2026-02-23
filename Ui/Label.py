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
        self.TextWidth : int = 0                         # The maximum width of one line of text
        self.TextSpacing : int = 0                       # The space in pixels between each line of text
        self.SplittedText : list = []                    # A list storing each line of text

        self.Rotation : float = 0                        # Rotation of the text
        self.Origin : Vector2 = Vector2(0, 0)            # Origin point of the text
        self.CharacterSpacing : float = 2                # Space between each character
        self.Font : Font = get_font_default()            # Font to use

        self.Underline : bool = False                    # If the text should be underlined
        self.LineColor : Color = Color(0, 0, 0, 0)       # Color of the underline
        self.LineSpacing : float = 0                     # Space between the line and the text on the y axis
        self.LineThickness : float = 0                   # Thickness of the line
        self.LineBegin : Vector2 = Vector2(0, 0)         # Begin point of the underline
        self.LineEnd : Vector2 = Vector2(0, 0)           # End point of the underline
        self.TextDimensions : list = []                  # List of the dimensions of each line of text

        self.Overline = False                            # If the text should be overlined
        self.OverLineColor : Color = Color(0, 0, 0, 0)   # Color of the overline

        self.BaseSize : Vector2 = Vector2(0, 0)          # The screen size it was made on.

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
        Extras: - get_font_default() is a raylib method to get the font used by default by raylib. \n
        Extras: - Source refers to Data.py
        """
        Info : dict = Source[MenuName][ButtonName]

        self.Position = Info["Position"]
        self.BaseSize = Info["OriginalScreenSize"]
        self.Text = Info["Text"]
        self.TextSize = Info["TextSize"]
        self.TextColor = Info["TextColor"]
        self.TextWidth = Info["TextWidth"]
        self.TextSpacing = Info["TextSpacing"]
        self.Font = get_font_default()
        self.Rotation = Info["Rotation"]
        self.Origin = Info["Origin"]
        self.CharacterSpacing = Info["CharacterSpacing"]
        self.Underline = Info["Underline"]
        self.LineColor = Info["LineColor"]
        self.LineSpacing = Info["LineSpacing"]
        self.LineThickness = Info["LineThickness"]
        self.Overline = Info["Overline"]
        self.OverlineColor = Info["OverlineColor"]

        self.UpdateText()
        return None
    
    def UpdateText(self) -> None:
        """
        Resize the parameters for over and under line accordingly to the screen size, and update the lines of the text.
        
        :return: None

        Extras: - measure_text_ex() is a raylib function to measure a text dimensions with a special font.
        """
        self.SpliText()
        if self.Overline or self.Underline:
            for line in self.SplittedText:
                LineDimension : Vector2 = measure_text_ex(self.Font, line, self.TextSize, self.CharacterSpacing)
                self.TextDimensions.append(LineDimension)
        if self.Underline:
            self.LineBegin = Vector2(self.Position.x, self.Position.y + self.TextDimensions[0].y + self.LineSpacing)
            self.LineEnd = Vector2(self.LineBegin.x + self.TextDimensions[0].x, self.LineBegin.y)
        return None
    
    def SpliText(self) -> None:
        """
        Split the text accros multiple lines.

        :return: None

        Extras: - measure_text() is a raylib function to measure the width of a text.
        """
        line : str = ""
        self.SplittedText.clear()
        for letter in self.Text:
            line += letter
            if(measure_text(line, self.TextSize) > self.TextWidth):
                AdditionalLetter : str = line[-1]
                line = line[:-1]
                self.SplittedText.append(line)
                line = AdditionalLetter

        if line != "":
            self.SplittedText.append(line)
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
        for line in range(len(self.TextDimensions)):
            self.TextDimensions[line] = Vector2(self.TextDimensions[line].x * XFactor,
                                                self.TextDimensions[line].y * YFactor)
        self.BaseSize = ScreenSize
        self.TextSize = int(self.TextSize * YFactor)

        self.UpdateLinePos()
        return None
    
    def Draw(self) -> None:
        """
        Draw the label and its overline and underline if needed.
        
        :return: None

        Extras: - draw_text_pro() is a raylib function to draw text with additionnal parameters. \n
        Extras: - draw_line_ex() is a raylib function to draw a line with additional parameters. \n
        Extras: - draw_rectangle() is a raylib function to draw a rectangle. \n
        Extras: - 1 is added to the dimensions to avoid rounding imperfection. \n
        Extras: - Vector2 is a raylib structure holding a x and a y position.

        :BUG: Drawing multiples lines of text with an under line will not work, though, overline does work.
        """
        UnderLineBegin : Vector2 = self.LineBegin
        UnderLineEnd : Vector2 = self.LineEnd

        for line in range(len(self.SplittedText)):
            TextPos : Vector2 = Vector2(self.Position.x, self.Position.y + (self.TextSpacing + self.TextSize) * line)
            draw_text_pro(self.Font, self.SplittedText[line], TextPos, self.Origin, self.Rotation, self.TextSize, self.CharacterSpacing, self.TextColor)
            if self.Underline:
                UnderLineBegin.y += self.TextSpacing * line
                UnderLineEnd.y += self.TextSpacing * line
                draw_line_ex(UnderLineBegin, UnderLineEnd, self.LineThickness, self.LineColor)
            if self.Overline:
                draw_rectangle(int(TextPos.x), int(TextPos.y), int(self.TextDimensions[line].x) + 1, int(self.TextDimensions[line].y) + 1, self.OverlineColor)
        return None