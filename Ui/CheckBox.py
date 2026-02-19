from pyray import *

class CheckBox:
    def __init__(self) -> None:
        """
        Create a CheckBox object. All attributes are defaulted to 0.
        
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        self.Position : Rectangle = Rectangle(0, 0, 0, 0)               # Dimensions of the Check Box
        self.IsChecked : bool = False                                   # If the Check Box is checked
        self.function = None                                            # Function to call when checked

        self.BaseTexture : Rectangle = Rectangle(0, 0, 0, 0)            # Location of the base Check Box texture in the Atlas
        self.HoverTexture : Rectangle = Rectangle(0, 0, 0, 0)           # Location of the hover Check Box texture in the Atlas
        self.CheckedTexture : Rectangle = Rectangle(0, 0, 0, 0)         # Location of the checked Check Box texture in the Atlas
        self.CheckedHoverTexture : Rectangle = Rectangle(0, 0, 0, 0)    # Location of the hoverchecked Check Box texture in the Atlas
        self.CurrentTexture : Rectangle = Rectangle(0, 0, 0, 0)         # Location of the current texture to use in the Atlas

        self.BaseSize : Vector2 = Vector2(0, 0)                         # The screen size it was made on.
        return None
    
    def GetChecked(self) -> bool:
        """
        Return True if the box is checked and False otherwise.
        
        :return: If the box is checked or not.
        :rtype: bool
        """
        return self.IsChecked
    
    def Bind(self, function) -> None:
        """
        Give a function to the checkbox that will be called when it is checked.
        
        :param function: A function to call
        :type function: function
        :return: None

        Extras: - Function must be argumentless and return None. \n
        Extras: - Since it's a check box, function should be switching a boolean on and off.
        """
        self.function = function
        return None
    
    def IsHovered(self) -> bool:
        """
        Check if the mouse is hovering the check box.
        
        :return: True if the mouse hover the check box, False otherwise.
        :rtype: bool

        Extras: - check_collision_point_rec() is a raylib function checking if a point is inside a rectangle. \n
        Extras: - get_mouse_position() is a raylib function returning a Vector2 holding the x and y position of the mouse.
        """
        if check_collision_point_rec(get_mouse_position(), Rectangle(self.Position.x, self.Position.y, self.Position.width, self.Position.height)):
            return True
        return False
    
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
    
    def Prepare(self, Source : dict, MenuName : str, ButtonName : str, SpriteSource : dict) -> None:
        """
        Load everything the button needs to work.
        
        :param Source: The dictionarry containing all Data.
        :type Source: dict
        :param MenuName: The name of the menu inside Data.py
        :type MenuName: str
        :param ButtonName: The name of the button inside Data.py
        :type ButtonName: str
        :param SpriteSource: The dictionarry containing all the sprites location
        :type SpriteSource: dict
        :return: None

        Extras: - Source and SpriteSource refers to Data.py
        """

        Info : dict = Source[MenuName][ButtonName]
        SpriteInfo : dict = SpriteSource[Info["RefTexture"]]

        self.Position = Info["Position"]
        self.BaseSize = Info["OriginalScreenSize"]
        self.BaseTexture = SpriteInfo["Base"]
        self.HoverTexture = SpriteInfo["Hover"]
        self.CheckedTexture = SpriteInfo["Checked"]
        self.CheckedHoverTexture = SpriteInfo["CheckedHover"]

        return None
    
    def Draw(self, Atlas : Texture) -> None:
        """
        Draw the text box with the right texture.
        
        :param Atlas: The texture containing all the game's sprites.
        :type Atlas: Texture
        :return: None

        Extras: - Texture is a raylib structure used to hold images. \n
        Extras: - In this project, Atlas is Sprites.png
        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        Origin : Vector2 = Vector2(0, 0)
        Rotation : int = 0
        draw_texture_pro(Atlas, self.CurrentTexture, self.Position, Origin, Rotation, WHITE)
        return None
    
    def Scale(self, ScreenSize : Vector2) -> None:
        """
        Scale the check box to the given screen size.
        
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
        return None
    
    def Update(self) -> None:
        """
        Handle the different state changes of the check box.
        
        :return: None
        """
        if self.IsHovered() and self.IsClicked():
            self.CurrentTexture = self.CheckedHoverTexture
            self.IsChecked = not self.IsChecked
            self.function()
        elif self.IsChecked and self.IsHovered():
            self.CurrentTexture = self.CheckedHoverTexture
        elif self.IsClicked() and not self.IsChecked:
            self.CurrentTexture = self.BaseTexture
        elif self.IsHovered():
            self.CurrentTexture = self.HoverTexture
        elif self.IsChecked:
            self.CurrentTexture = self.CheckedTexture
        else:
            self.CurrentTexture = self.BaseTexture
        return None
