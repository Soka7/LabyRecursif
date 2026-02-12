from pyray import *

class Button:
    def __init__(self) -> None:
        """
        Create a button object. \n
        All attributes are defaulted to 0 or null.
        """
        self.function = None                        # Function Called by the button when its clicked
        self.Position : Vector2 = Vector2(0, 0)     # Position (x and y)
        self.Size : Vector2 = Vector2(0, 0)         # Size (width, lenght)
        self.Text : str = ""                        # Text displayed
        self.TextSize : int = 0                     # Size of the text with default font
        self.TextColor : Color = (0, 0, 0, 0)       # Color of the text (Red, Green, Blue, Alpha(Opacity))
        self.HoverSize : int = 0                    # Size of the hover effect (line thickness)
        self.HoverColor : Color = (0, 0, 0, 0)      # Color of those lines
        return None
        
    def IsHovered(self) -> bool:
        """
        Check if the mouse is hovering the button.
        
        :return: True if the mouse is hovering it, False otherwise.
        :rtype: bool
        """
        # Check if the mouse cursor is inside the button's hitbox
        if check_collision_point_rec(get_mouse_position(), (self.Position.x, self.Position.y, self.Size.x, self.Size.y)):
            return True
        return False

    def EditPos(self, Position : Vector2, Size : Vector2) -> None:
        """
        Edit the button position and size.
        
        :param Position: The x and y position of the button.
        :type Position: Vector2
        :param Size: The width and lenght of the button.
        :type Size: Vector2
        :return: None
        """
        self.Position = Position
        self.Size = Size
        return None
    
    def EditText(self, Text : str, TextSize : int, TextColor : Color) -> None:
        """
        Edit the text, size of the text and color of the text displayed by the button.
        
        :param Text: The text to display.
        :type Text: str
        :param TextSize: The fontsize of the text. 
        :type TextSize: int
        :param TextColor: The color of the text. (RGBA)
        :type TextColor: Color
        :return: None
        """
        self.Text = Text
        self.TextSize = TextSize
        self.TextColor = TextColor
        return None

    def EditHover(self, HoverSize : int, HoverColor : Color) -> None:
        """
        Edit the hover effect of the button. \n
        The effect is simply a rectangular border.
        
        :param HoverSize: The size of the border in pixels.
        :type HoverSize: int
        :param HoverColor: The color of the border (RGBA).
        :type HoverColor: Color
        :return: None
        """
        self.HoverSize = HoverSize
        self.HoverColor = HoverColor
        return None
    
    def Bind(self, function) -> None:
        """
        Give a function to the button that will be called when it is clicked.
        
        :param function: A function, must return None and have no parameters.
        :return: None
        """
        # Define which function to call when the button is pressed
        self.function = function
        return None
    
    def DrawText(self) -> None:
        """
        Draw the text of the button at its center.
        
        :return: None
        """
        TextWidth : int = measure_text(self.Text, self.TextSize) # Measure the width in pixels of the text
        # Find where the text should be to be centered.
        TextPosition : Vector2 = Vector2(self.Position.x + (self.Size.x - TextWidth) / 2,
                                         self.Position.y + (self.Size.y - self.TextSize) / 2)
        draw_text(self.Text, int(TextPosition.x), int(TextPosition.y), self.TextSize, self.TextColor)
        return None

    def HoverEffect(self) -> None:
        """
        Apply the hover effect to the button if it is hovered.
        
        :return: None
        """
        # If the button is hovered apply a a small effect (lines of self.hoversize thicknexss and self.HoverCOlor color)
        if self.IsHovered():
            Object : Rectangle = (self.Position.x, self.Position.y, self.Size.x, self.Size.y)
            draw_rectangle_lines_ex(Object, self.HoverSize, self.HoverColor)
        return None

    def Update(self) -> None:
        """
        Check if the mouse clicked the button and call the function it has.
        
        :return: None
        """
        # Check if the button is hovered by the mouse and if the left click of the mouse is pressed, call the function if it is the case
        if self.IsHovered() and is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            self.function()
        return None
    
    def Draw(self, Atlas : Texture, TextureLocation : Rectangle) -> None:
        """
        Draw a rectangle being the button at the given coordinates with the given size. \n
        Also Draw its text and apply a hover effect if needed. \n
        :param Atlas: The texture containing all the sprites.
        :type Atlas: Texture
        :param TextureLocation: The rectangle containing the position of the texture in the atlas.
        :type TextureLocation: Rectangle
        :return: None
        """
        Origin : Vector2 = Vector2(0, 0) # Origin of the button (top left corner)
        DestinationRec : Rectangle = Rectangle(self.Position.x, self.Position.y, self.Size.x, self.Size.y) # Button hitbox
        Rotation : int = 0 # Rotation of the button's texture (0)
        # Take a region of Atlas, being TextureLocation, to draw the button
        # Draw it at its hitbox place with a WHITE tint (default)
        draw_texture_pro(Atlas, TextureLocation, DestinationRec, Origin, Rotation, WHITE)
        self.DrawText()
        self.HoverEffect()
        return None
    
