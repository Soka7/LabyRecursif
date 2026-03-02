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
        self.Position = Rectangle(0, 0, 0, 0)       # Rectangle being the button's dimmensions
        self.Text : str = ""                        # Text displayed by the button
        self.TextSize : int = 0                     # Size of the text with default font
        self.TextColor : Color = (0, 0, 0, 0)       # Color of the text 

        self.BaseSize : Vector2 = Vector2(0, 0)     # The screen size it was made on.

        # Textures
        self.CurrentTexture : Rectangle = Rectangle(0, 0, 0, 0)      # The location of the texture to use for drawing
        self.BaseTexture : Rectangle = Rectangle(0, 0, 0, 0)         # Location of the base button's texture in the Atlas
        self.HoverTexture : Rectangle = Rectangle(0, 0, 0, 0)        # Location of the hover button's texture in the Atlas
        self.PressedTexture : Rectangle = Rectangle(0, 0, 0, 0)      # Location of the pressed button's texture in the Atlas
        self.HoverPressedTexture : Rectangle = Rectangle(0, 0, 0, 0) # Location of the hover pressed button's texture in the Atlas
        return None
    
    def Prepare(self, Source : dict, MenuName : str, ButtonName : str, SpriteSource : dict) -> None:
        """
        Load everything the button need to work.

        :param Source: The dictionary containing the data for the button
        :type Source: dict
        :param MenuName: The name of the menu inside Data.py
        :type MenuName: str
        :param ButtonName: The name of the button inside Data.py
        :type ButtonName: str
        :param SpriteSource: The dictionary containing all the sprites location in Sprites.png
        :type SpriteSource: dict
        :return: None

        Extras: - Source and SpriteSource refers to Data.py
        """
        Info = Source[MenuName][ButtonName]
        SpriteInfo = SpriteSource[Info["RefTexture"]]

        self.Position = Info["Position"]
        self.BaseSize = Info["OriginalScreenSize"]
        self.Text = Info["Text"]
        self.TextSize = Info["TextSize"]
        self.TextColor = Info["TextColor"]

        self.BaseTexture = SpriteInfo["Base"]
        self.HoverTexture = SpriteInfo["Hover"]
        self.PressedTexture = SpriteInfo["Pressed"]
        self.HoverPressedTexture = SpriteInfo["HoverPressed"]

        return None
        
    def IsHovered(self) -> bool:
        """
        Check if the mouse is hovering the button.
        
        :return: True if the mouse is hovering it, False otherwise
        :rtype: bool

        Extras: - check_collision_point_rec() is a raylib function checking if a point is inside a rectangle. \n
        Extras: - get_mouse_position() is a raylib function returning a Vector2 holding the x and y position of the mouse.
        """
        if check_collision_point_rec(get_mouse_position(), (self.Position.x, self.Position.y, self.Position.width, self.Position.height)):
            return True
        return False
    
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
        Extras: - draw_text() is a raylib function to draw text. \n
        Extras: - Vector2 is a raylib structure storing 2 floats, being x and y coordinates.
        """
        TextWidth : int = measure_text(self.Text, self.TextSize)
        # Center the text inside the button
        TextPosition : Vector2 = Vector2(self.Position.x + (self.Position.width - TextWidth) / 2,
                                         self.Position.y + (self.Position.height - self.TextSize) / 2)
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

        # Reset the texture back to the normal one
        if self.CurrentTexture != self.BaseTexture:
            self.CurrentTexture = self.BaseTexture
        return None
    
    def Scale(self, ScreenSize : Vector2) -> None:
        """
        Scale the button to the given screen size.
        
        :param ScreenSize: The size of the screen
        :type ScreenSize: Vector2
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height. \n
        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        XFactor : float = ScreenSize.x / self.BaseSize.x
        YFactor : float = ScreenSize.y / self.BaseSize.y

        self.Position = Rectangle(self.Position.x * XFactor,
                                  self.Position.y * YFactor,
                                  self.Position.width * XFactor,
                                  self.Position.height * YFactor)
        self.BaseSize = ScreenSize
        self.TextSize = int(self.TextSize * YFactor)
        return None
    
    def Draw(self, Atlas : Texture) -> None:
        """
        Draw the button with the adequate texture.

        :param Atlas: The texture holding all the sprites of the game.
        :type Atlas: Texture
        :param ScreenSize: The current size of the screen
        :type ScreenSize: Vector2
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - draw_texture_pro() is a raylib method to draw a texture with more flexibility. \n
        Extras: - Texture is a raylib data storing an image.
        """

        Origin : Vector2 = Vector2(0, 0)
        Rotation : int = 0

        draw_texture_pro(Atlas, self.CurrentTexture, self.Position, Origin, Rotation, WHITE)
        self.DrawText()
        return None
