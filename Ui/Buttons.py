from pyray import *

class Button:
    def __init__(self) -> None:
        """
        Create a button object. \n
        All attributes are defaulted to 0 or null.

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height. \n
        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity).
        """
        self.function = None                        # Function called by the button when its clicked
        self.Dimensions = Rectangle(0, 0, 0, 0)     # Rectangle being the button's dimmensions
        self.Text : str = ""                        # Text displayed by the button
        self.TextSize : int = 0                     # Size of the text with default font
        self.TextColor : Color = (0, 0, 0, 0)       # Color of the text (Red, Green, Blue, Alpha(Opacity))

        # Textures
        self.CurrentTexture : Rectangle = Rectangle(0, 0, 0, 0)  # The location of the texture to use for drawing
        self.BaseTexture : Rectangle = Rectangle(0, 0, 0, 0)     # Location of the base button's texture in the Atlas
        self.HoverTexture : Rectangle = Rectangle(0, 0, 0, 0)    # Location of the hover button's texture in the Atlas
        self.PressedTexture : Rectangle = Rectangle(0, 0, 0, 0)  # Location of the pressed button's texture in the Atlas
        return None
        
    def IsHovered(self) -> bool:
        """
        Check if the mouse is hovering the button.
        
        :return: True if the mouse is hovering it, False otherwise.
        :rtype: bool

        Extras: - check_collision_point_rec() is a raylib function checking if a point is inside a rectangle. \n
        Extras: - get_mouse_position() is a raylib function returning a Vector2 holding the x and y position of the mouse.
        """
        if check_collision_point_rec(get_mouse_position(), (self.Dimensions.x, self.Dimensions.y, self.Dimensions.width, self.Dimensions.height)):
            return True
        return False

    def EditPos(self, Dimensions : Rectangle) -> None:
        """
        Edit the button's position and size.
        
        :param Dimensions: The x and y position of the button and its width and height.
        :type Dimensions: Rectangle
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        self.Dimensions = Dimensions
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

        Extras: - Using default font. \n
        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity).
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

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height. \n
        Extras: - In this project the Atlas is Sprites.png
        """
        self.BaseTexture = Base
        self.HoverTexture = Hover
        self.PressedTexture = Pressed
        return None
    
    def Bind(self, function) -> None:
        """
        Give a function to the button that will be called when it is clicked.
        
        :param function: A function to call
        :type function: function
        :return: None

        Extras: - Function must be argumentless and return None.
        """
        self.function = function
        return None
    
    def DrawText(self) -> None:
        """
        Draw the text of the button at its center.
        
        :return: None

        Extras: - measure_text() is a raylib function returning the width of the text with the default font. \n
        Extras: - draw_text() is a raylib function to draw text.
        """
        TextWidth : int = measure_text(self.Text, self.TextSize)
        # Find where the text should be to be centered.
        TextPosition : Vector2 = Vector2(self.Dimensions.x + (self.Dimensions.width - TextWidth) / 2,
                                         self.Dimensions.y + (self.Dimensions.height - self.TextSize) / 2)
        draw_text(self.Text, int(TextPosition.x), int(TextPosition.y), self.TextSize, self.TextColor)
        return None
    
    def IsClicked(self) -> bool:
        """
        Check if the left mouse button is clicked.

        :return: True if the buton is clicked False otherwise
        :rtype: bool

        Extras: - is_mouse_button_pressed() is a raylib function checking if a button of the mouse has been pressed. \n
        Extras: - MouseButton.MOUSE_BUTTON_LEFT is a raylib data that refers to the left mouse button
        """
        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            return True
        return False

    def Update(self) -> None:
        """
        Check if the mouse clicked the button and call the function it holds.
        
        :return: None

        Extras: - is_mouse_button_down() is a raylib function checking if a button of the mouse is being held. \n
        Extras: - MouseButton.MOUSE_BUTTON_LEFT is a raylib data that refers to the left mouse button
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

        # Reset the texture 
        if self.CurrentTexture != self.BaseTexture:
            self.CurrentTexture = self.BaseTexture
        return None
    
    def Draw(self, Atlas : Texture) -> None:
        """
        Draw the button with the adequate texture.

        :param Atlas: The texture holding all the sprites of the game.
        :type Atlas: Texture
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position.
        Extras: - draw_texture_pro() is a raylib method to draw a texture with more flexibility.
        """
        Origin : Vector2 = Vector2(0, 0) # Origin of the button (top left corner)
        Rotation : int = 0 # Rotation of the button's texture (0)

        # Take a region of Atlas, being TextureLocation, to draw the button
        # Draw it at its hitbox place with a WHITE tint (default)
        draw_texture_pro(Atlas, self.CurrentTexture, self.Dimensions, Origin, Rotation, WHITE)
        self.DrawText()
        return None
    
