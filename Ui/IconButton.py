from pyray import *

class IconButton:
    def __init__(self) -> None:
        """
        Create a icon button object. \n
        All attributes are defaulted to 0 or null.

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height. \n
        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity).
        """
        self.function = None                        # Function called by the button when its clicked
        self.Position = Rectangle(0, 0, 0, 0)       # Rectangle being the button's dimmensions
        self.IconPosition = Rectangle(0, 0, 0, 0)   # Rectangle being the icon's dimensions

        self.IconScaleFactor : Vector2 = Vector2(0, 0) # % of the width and height of the button that the icon will have

        self.BaseSize : Vector2 = Vector2(0, 0)     # The screen size it was made on.

        # Textures
        self.CurrentTexture : Rectangle = Rectangle(0, 0, 0, 0)  # The location of the texture to use for drawing
        self.BaseTexture : Rectangle = Rectangle(0, 0, 0, 0)     # Location of the base button's texture in the Atlas
        self.HoverTexture : Rectangle = Rectangle(0, 0, 0, 0)    # Location of the hover button's texture in the Atlas
        self.PressedTexture : Rectangle = Rectangle(0, 0, 0, 0)  # Location of the pressed button's texture in the Atlas
        self.HoverPressedTexture : Rectangle = Rectangle(0, 0, 0, 0) # Location of the hover pressed button's texture in the Atlas
        self.IconTexture : Rectangle = Rectangle(0, 0, 0, 0)     # Location of the icon texture displayed by the button in the Atlas
        return None
    
    def Prepare(self, Source : dict, MenuName : str, ButtonName : str, SpriteSource : dict) -> None:
        """
        Load everything the icon button need to work.

        :param Source: The dictionary containing all Data.
        :type Source: dict
        :param MenuName: The name of the menu inside Data.py
        :type MenuName: str
        :param ButtonName: The name of the button inside Data.py
        :type ButtonName: str
        :param SpriteSource: The dictionary containing all the sprites location
        :type SpriteSource: dict
        :return: None

        Extras: - Source and SpriteSource refers to Data.py
        """
        Info = Source[MenuName][ButtonName]
        SpriteInfo = SpriteSource[Info["RefTexture"]]

        self.Position = Info["Position"]
        self.IconScaleFactor = Info["IconScaleFactor"]
        self.BaseSize = Info["OriginalScreenSize"]

        self.BaseTexture = SpriteInfo["Base"]
        self.HoverTexture = SpriteInfo["Hover"]
        self.PressedTexture = SpriteInfo["Pressed"]
        self.HoverPressedTexture = SpriteInfo["HoverPressed"]
        self.IconTexture = SpriteSource["Icons"][Info["RefIconTexture"]]

        self.IconPosition.width = self.Position.width * self.IconScaleFactor.x
        self.IconPosition.height = self.Position.height * self.IconScaleFactor.y
        self.CenterIcon()
        return None
    
    def CenterIcon(self) -> None:
        """
        Center the icon at the center of the button.

        :return: None
        """
        self.IconPosition.x = self.Position.x + (self.Position.width - self.IconPosition.width) / 2
        self.IconPosition.y = self.Position.y + (self.Position.height - self.IconPosition.height) / 2
        return None
        
    def IsHovered(self) -> bool:
        """
        Check if the mouse is hovering the button.
        
        :return: True if the mouse is hovering it, False otherwise.
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
        
        self.IconPosition = Rectangle(self.IconPosition.x * XFactor,
                                      self.IconPosition.y * YFactor,
                                      self.IconPosition.width * XFactor,
                                      self.IconPosition.height * YFactor)
        self.CenterIcon()
        self.BaseSize = ScreenSize
        return None
    
    def Draw(self, Atlas : Texture) -> None:
        """
        Draw the button with the adequate texture.

        :param Atlas: The texture holding all the sprites of the game.
        :type Atlas: Texture
        :param ScreenSize: The current size of the screen
        :type ScreenSize: Vector2
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position.
        Extras: - draw_texture_pro() is a raylib method to draw a texture with more flexibility.
        """

        Origin : Vector2 = Vector2(0, 0) # Origin of the button (top left corner)
        Rotation : int = 0 # Rotation of the button's texture (0)

        # Take a region of Atlas, being TextureLocation, to draw the button
        # Draw it at its hitbox place with a WHITE tint (default)
        draw_texture_pro(Atlas, self.CurrentTexture, self.Position, Origin, Rotation, WHITE)
        draw_texture_pro(Atlas, self.IconTexture, self.IconPosition, Origin, Rotation, WHITE)
        return None
