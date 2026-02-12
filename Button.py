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

        self.CurrentTexture : Rectangle = Rectangle(0, 0, 0, 0) # The location of the texture to use for drawing.
        self.BaseTexture : Rectangle = Rectangle(0, 0, 0, 0)    # Location of the base button texture in the Atlas
        self.HoverTexture : Rectangle = Rectangle(0, 0, 0, 0)   # Location of the hover button texture in the Atlas
        self.PressedTexture : Rectangle = Rectangle(0, 0, 0, 0) # Location of the pressed button texture in the Atlas
        return None
        
    def IsHovered(self) -> bool:
        """
        Check if the mouse is hovering the button.
        
        :return: True if the mouse is hovering it, False otherwise.
        :rtype: bool
        """
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
    
    def EditTextures(self, Base : Rectangle, Hover : Rectangle, Pressed : Rectangle) -> None:
        """
        Give the textures of the buttons
        
        :param Base: The location of the base texture in the Atlas
        :type Base: Rectangle
        :param Hover: The location of the hover texture in the Atlas
        :type Hover: Rectangle
        :param Pressed: The location of the pressed texture in the Atlas.
        :type Pressed: Rectangle
        :return: None
        """
        self.BaseTexture = Base
        self.HoverTexture = Hover
        self.PressedTexture = Pressed
        return None
    
    def Bind(self, function) -> None:
        """
        Give a function to the button that will be called when it is clicked.
        
        :param function: A function, must return None and have no parameters.
        :return: None
        """
        self.function = function
        return None
    
    def DrawText(self) -> None:
        """
        Draw the text of the button at its center.
        
        :return: None
        """
        TextWidth : int = measure_text(self.Text, self.TextSize)
        # Find where the text should be to be centered.
        TextPosition : Vector2 = Vector2(self.Position.x + (self.Size.x - TextWidth) / 2,
                                         self.Position.y + (self.Size.y - self.TextSize) / 2)
        draw_text(self.Text, int(TextPosition.x), int(TextPosition.y), self.TextSize, self.TextColor)
        return None
    
    def IsClicked(self) -> bool:
        """
        Check if the left mouse button is clicked.

        :return: If the buton is clicked
        :rtype: bool
        """
        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            return True
        return False

    def Update(self) -> None:
        """
        Check if the mouse clicked the button and call the function it has.
        
        :return: None
        """
        # Check if the button is hovered by the mouse and if the left click of the mouse is pressed, call the function if it is the case
        if self.IsHovered():
            self.CurrentTexture = self.HoverTexture
            if self.IsClicked():
                self.function()
                self.CurrentTexture = self.PressedTexture
            elif is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT):
                self.CurrentTexture = self.PressedTexture
            return None
        if self.CurrentTexture != self.BaseTexture:
            self.CurrentTexture = self.BaseTexture
        return None
    
    def Draw(self, Atlas : Texture) -> None:
        """
        Draw a rectangle being the button at the given coordinates with the given size. \n
        Also Draw its text and apply a hover effect if needed. \n
        :param Atlas: The texture containing all the sprites.
        :type Atlas: Texture
        :return: None
        """
        Origin : Vector2 = Vector2(0, 0) # Origin of the button (top left corner)
        DestinationRec : Rectangle = Rectangle(self.Position.x, self.Position.y, self.Size.x, self.Size.y) # Button hitbox
        Rotation : int = 0 # Rotation of the button's texture (0)

        # Take a region of Atlas, being TextureLocation, to draw the button
        # Draw it at its hitbox place with a WHITE tint (default)
        draw_texture_pro(Atlas, self.CurrentTexture, DestinationRec, Origin, Rotation, WHITE)
        self.DrawText()
        return None
    
