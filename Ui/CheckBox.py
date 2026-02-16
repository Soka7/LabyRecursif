from pyray import *

class CheckBox:
    def __init__(self) -> None:
        """
        Create a CheckBox object. All attributes are defaulted to 0.
        
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        self.CheckBoxLoc : Rectangle = Rectangle(0, 0, 0, 0)
        self.IsChecked : bool = False

        self.BaseTexture : Rectangle = Rectangle(0, 0, 0, 0)
        self.HoverTexture : Rectangle = Rectangle(0, 0, 0, 0)
        self.CheckedTexture : Rectangle = Rectangle(0, 0, 0, 0)
        self.CheckedHoverTexture : Rectangle = Rectangle(0, 0, 0, 0)
        self.CurrentTexture : Rectangle = Rectangle(0, 0, 0, 0)
        return None
    
    def GetChecked(self) -> bool:
        """
        Return True if the box is checked and False otherwise.
        
        :return: If the box is checked or not.
        :rtype: bool
        """
        return self.IsChecked
    
    def EditTextures(self, Base : Rectangle, Hover : Rectangle, Checked : Rectangle, HoverChecked : Rectangle) -> None:
        """
        Edit the different textures of the check box.
        
        :param Base: Location of the base texture in the Atlas.
        :type Base: Rectangle
        :param Hover: Location of the hover texture in the Atlas.
        :type Hover: Rectangle
        :param Checked: Location of the checked texture in the Atlas.
        :type Checked: Rectangle
        :param HoverChecked: Location of the hoverchecked texture in the Atlas.
        :type HoverChecked: Rectangle
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        self.BaseTexture = Base
        self.HoverTexture = Hover
        self.CheckedTexture = Checked
        self.CheckedHoverTexture = HoverChecked
        return None
    
    def EditPos(self, Dimensions : Rectangle) -> None:
        """
        Edit the position and dimensions of the check box.
        
        :param Dimensions: The x and y position and the width and height of the check box.
        :type Dimensions: Rectangle
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        self.CheckBoxLoc = Dimensions
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
        draw_texture_pro(Atlas, self.CurrentTexture, self.CheckBoxLoc, Origin, Rotation, WHITE)
        return None

    def IsHovered(self) -> bool:
        """
        Check if the mouse is hovering the check box.
        
        :return: True if the mouse hover the check box, False otherwise.
        :rtype: bool

        Extras: - check_collision_point_rec() is a raylib function checking if a point is inside a rectangle. \n
        Extras: - get_mouse_position() is a raylib function returning a Vector2 holding the x and y position of the mouse.
        """
        if check_collision_point_rec(get_mouse_position(), Rectangle(self.CheckBoxLoc.x, self.CheckBoxLoc.y, self.CheckBoxLoc.width, self.CheckBoxLoc.height)):
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
    
    def Update(self) -> None:
        """
        Handle the different state changes of the check box.
        
        :return: None
        """
        if self.IsHovered() and self.IsClicked():
            self.CurrentTexture = self.CheckedHoverTexture
            self.IsChecked = not self.IsChecked
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
