from pyray import *

from Ui.Buttons import Button
from Ui.InputBox import InputBox
from Ui.Label import Label
from Ui.CheckBox import CheckBox

class Menu:
    def __init__(self, Buttons : int, InputBoxes : int, CheckBoxes : int, Labels : int) -> None:
        """
        Create a Menu object with a specified amount of buttons.

        :param Buttons: The amount of buttons in the menu
        :type Buttons: int
        :param InputBoxes: The amount of input boxes in the menu
        :type InputBoxes: int
        :param CheckBoxes: The amount of chck boxes in the menu
        :type CheckBoxes: int
        :param Labels: The amount of Labels in the menu
        :type Labels: int
        :return: None

        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity). \n
        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        self.Buttons : list = []                                    # List holding all the buttons and input boxes
        for _ in range(Buttons):                                    # Create the buttons        
            self.Buttons.append(Button())

        for _ in range(InputBoxes):                                 # Create the input boxes
            self.Buttons.append(InputBox())

        for _ in range(CheckBoxes):                                 # Create the checkboxes
            self.Buttons.append(CheckBox())

        for _ in range(Labels):                                     # Create the labels
            self.Buttons.append(Label())

        # Buttons texture
        self.BaseButtonTexture : Rectangle = Rectangle(0, 0, 0, 0)     # Where the base button texture is located in the Atlas
        self.HoverButtonTexture : Rectangle = Rectangle(0, 0, 0, 0)    # Where the hover button texture is located in the Atlas
        self.PressedButtonTexture : Rectangle = Rectangle(0, 0, 0, 0)  # Where the pressed button texture is located in the Atlas
        return None
    
    def Update(self) -> None:
        """
        Call the update method of each elements.

        :return: None
        """
        for button in self.Buttons:
            if type(button) == Label:
                continue
            button.Update()
        return None

    def Draw(self, Atlas : Texture) -> None:
        """
        Call the Draw method of each button and input boxes.

        :param Atlas: The texture holding all the game sprite.
        :type Atlas: Texture
        :return: None

        Extras: - Texture is a structure of raylib holding an image. \n
        Extras: - In this project, Atlas is Sprites.png
        """
        for button in self.Buttons:
            button.Draw(Atlas)
        return None
    
    def Prepare(self, Source : dict, MenuName : str, SpriteSource : dict) -> None:
        """
        Call the prepare method of each element.

        :param Source: The dictionarry containing all Data.
        :type Source: dict
        :param MenuName: The name of the menu inside Data.py
        :type MenuName: str
        :param SpriteSource: The dictionarry containing all the sprites location
        :type SpriteSource: dict
        :return: None

        Extras: - Source and SpriteSource refers to Data.py
        """
        Counter : int = 0
        Info : dict = Source[MenuName]
        for ButtonName in Source[MenuName].keys():
            if Info[ButtonName]["Type"] == "Label":
                self.Buttons[Counter].Prepare(Source, MenuName, ButtonName)
            else:
                self.Buttons[Counter].Prepare(Source, MenuName, ButtonName, SpriteSource)
            Counter += 1
        return None
    
    def ScaleMenu(self, ScreenSize : Vector2) -> None:
        """
        Call the scale method of each element of the menu to adapt to the given screen size.
        
        :param ScreenSize: The size of the screen
        :type ScreenSize: Vector2
        :return: None
        
        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        for element in self.Buttons:
            element.Scale(ScreenSize)
        return None
    
    def BindAll(self, *args) -> None:
        """
        Define which functions the buttons should call when clicked.

        :param *args: The function called by each button
        :type *args: function
        :return: None

        Extras: - Each function must be argumentless and must return None
        """
        for i in range(len(args)):
            if type(self.Buttons[i]) != Button:
                continue
            self.Buttons[i].Bind(args[i])
        return None
    
    def GetInputBoxesContent(self) -> list:
        """
        Return the content of all the input boxes as a list of strings.
        
        :return: A list of strings with all the content
        :rtype: list

        Extras: - The list is ordered the same way you created the input boxes.
        """
        Content : list = []
        for inputbox in self.Buttons:
            if type(inputbox) != InputBox:
                continue
            Content.append(inputbox.GetInput())
        return Content
