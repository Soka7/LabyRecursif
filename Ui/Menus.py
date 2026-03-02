from pyray import *

from Ui.Buttons import Button
from Ui.IconButton import IconButton
from Ui.InputBox import InputBox
from Ui.Label import Label
from Ui.CheckBox import CheckBox

class Menu:
    def __init__(self, Buttons : int, IconButtons : int, InputBoxes : int, CheckBoxes : int, Labels : int) -> None:
        """
        Create a Menu object with a specified amount of buttons.

        :param Buttons: The amount of buttons in the menu
        :type Buttons: int
        :param IconButtons: The amount of icon buttons in the menu
        :type IconButtons: int
        :param InputBoxes: The amount of input boxes in the menu
        :type InputBoxes: int
        :param CheckBoxes: The amount of chck boxes in the menu
        :type CheckBoxes: int
        :param Labels: The amount of Labels in the menu
        :type Labels: int
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height. \n
        Extras: - Vector2 is a raylib structure holding 2 floats, being x and y coordinates.
        """
        self.Buttons : list = []                                    # List holding all the buttons and input boxes
        for _ in range(Buttons):                                    # Create the buttons        
            self.Buttons.append(Button())

        for _ in range(IconButtons):                                # Create the icon buttons
            self.Buttons.append(IconButton())

        for _ in range(InputBoxes):                                 # Create the input boxes
            self.Buttons.append(InputBox())

        for _ in range(CheckBoxes):                                 # Create the checkboxes
            self.Buttons.append(CheckBox())

        for _ in range(Labels):                                     # Create the labels
            self.Buttons.append(Label())

        self.HasBackground : bool = False                           # If a background texture should be displayed
        self.BackgroundPos : Rectangle = Rectangle(0, 0, 0, 0)      # Position of the back ground
        self.BackgroundTexture : Rectangle = Rectangle(0, 0, 0, 0)  # Position of the texture in the Atlas
        self.BaseSize : Vector2 = Vector2(0, 0)                     # The original size the menu was meant to be on
        return None
    
    def Update(self) -> None:
        """
        Call the update method of each element.

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
        Extras: - In this project, Atlas is Sprites.png \n
        Extras: - Vector2 is a raylib structure holding 2 floats, being x and y coordinates. \n
        Extras: - draw_texture_pro() is a raylib funcion to draw only a part of texture.
        """
        if self.HasBackground:
            Origin : Vector2 = Vector2(0, 0)
            Rotation : float = 0
            draw_texture_pro(Atlas, self.BackgroundTexture, self.BackgroundPos, Origin, Rotation, WHITE)
        for button in self.Buttons:
            if type(button) == Label:
                button.Draw()
                continue
            button.Draw(Atlas)
        return None
    
    def Prepare(self, Source : dict, MenuName : str, SpriteSource : dict) -> None:
        """
        Call the prepare method of each element.

        :param Source: The dictionary containing all Data.
        :type Source: dict
        :param MenuName: The name of the menu inside Data.py
        :type MenuName: str
        :param SpriteSource: The dictionary containing all the sprites location
        :type SpriteSource: dict
        :return: None

        Extras: - Source and SpriteSource refers to Data.py
        """
        Counter : int = 0
        Info : dict = Source[MenuName]
        for ButtonName in Source[MenuName].keys():
            if ButtonName == "Background":
                continue
            if Info[ButtonName]["Type"] == "Label":
                self.Buttons[Counter].Prepare(Source, MenuName, ButtonName)
            else:
                self.Buttons[Counter].Prepare(Source, MenuName, ButtonName, SpriteSource)
            Counter += 1

        self.HasBackground = Info["Background"]["HasBackground"]
        if self.HasBackground:
            self.BackgroundPos = Info["Background"]["Position"]
            self.BackgroundTexture = SpriteSource["Background"][MenuName]
            self.BaseSize = Info["Background"]["OriginalScreenSize"]
        return None
    
    def ScaleMenu(self, ScreenSize : Vector2) -> None:
        """
        Call the scale method of each element of the menu to adapt to the given screen size. \n
        Also scale the menu background if it has one.
        
        :param ScreenSize: The size of the screen
        :type ScreenSize: Vector2
        :return: None
        
        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        for element in self.Buttons:
            element.Scale(ScreenSize)

        if self.HasBackground:
            XFactor : float = ScreenSize.x / self.BaseSize.x
            YFactor : float = ScreenSize.y / self.BaseSize.y
            self.BackgroundPos = Rectangle(self.BackgroundPos.x * XFactor,
                                           self.BackgroundPos.y * YFactor,
                                           self.BackgroundPos.width * XFactor,
                                           self.BackgroundPos.height * YFactor)
            self.BaseSize = ScreenSize
        return None
    
    def BindAll(self, *args) -> None:
        """
        Define which functions the buttons should call when clicked.

        :param *args: The function called by each button
        :type *args: function
        :return: None

        Extras: - Each function must be argumentless and must return None. \n
        Extras: - You must put the function in the same order you made the buttons in Data.py
        """
        Counter : int = 0
        FuncCounter : int = 0
        while Counter < len(self.Buttons):
            if type(self.Buttons[Counter]) != Button and type(self.Buttons[Counter]) != CheckBox and type(self.Buttons[Counter]) != IconButton:
                Counter += 1
                continue
            self.Buttons[Counter].Bind(args[FuncCounter])
            Counter += 1
            FuncCounter += 1

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
