from pyray import *
from Ui.Buttons import Button
from Ui.InputBox import InputBox

class Menu:
    def __init__(self, Buttons : tuple, ButtonBase : Rectangle, ButtonHover : Rectangle, ButtonPressed : Rectangle,
                 InputBoxTexture : Rectangle = Rectangle(0, 0, 0, 0)) -> None:
        """
        Create the class with a specified amount of buttons.

        :param Buttons: A tuple of 2 elements containing the amount of buttons and input box.
        :type Buttons: tuple
        :param ButtonBase: The location of the base button texture in the Atlas.
        :type ButtonBase: Rectangle
        :param ButtonHover: The location of the hover button texture in the Atlas.
        :type ButtonHover: Rectangle
        :param ButtonPressed: The location of the pressed button texture in the Atlas.
        :type ButtonPressed: Rectangle
        :param InputBoxTexture: The location of the texture of the input box in the Atlas.
        :type InputBoxTexture: Rectangle
        :return: None

        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity).
        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        # Buttons of the menu
        self.Buttons : list = []
        for _ in range(Buttons[0]):
            self.Buttons.append(Button())

        for _ in range(Buttons[1]):
            self.Buttons.append(InputBox(InputBoxTexture))

        # Default parameters for buttons
        self.TextSize : int = 24
        self.TextColor : Color = (0, 0, 0, 255)

        # Buttons texture
        self.BaseButtonTexture : Rectangle = ButtonBase
        self.HoverButtonTexture : Rectangle = ButtonHover
        self.PressedButtonTexture : Rectangle = ButtonPressed
        return None
    
    def Update(self) -> None:
        """
        Call the update method of each button.

        :return: None
        """
        for button in self.Buttons:
            button.Update()
        return None

    def Draw(self, Atlas : Texture) -> None:
        """
        Call the Draw method of each button.

        :param Atlas: The texture holding all the game sprite.
        :type Atlas: Texture
        :return: None

        Extras: - Texture is a structure of raylib holding an image. \n
        Extras: - In this project, Atlas is Sprites.png
        """
        for button in self.Buttons:
            button.Draw(Atlas)
        return None
    
    def Prepare(self) -> None:
        """
        Call the prepare methdo of the input boxes.
        
        :return: None
        """
        for inputbox in self.Buttons:
            if type(inputbox) != InputBox:
                continue
            inputbox.EditCharacters()
            inputbox.EditLine()
            inputbox.EditText()
            inputbox.EditWarning()
            inputbox.EditWelcome()
            inputbox.Prepare()
        return None

    def EditPosAll(self, *args : Rectangle) -> None:
        """
        Place all the buttons.

        :param *args: A Rectangle for each button
        :type *args: Rectangle
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        for i in range(len(args)):
            self.Buttons[i].EditPos(args[i])
        return None
    
    def EditTextAll(self, *args : str) -> None:
        """
        Give the text parameters to all buttons of the menu. Size and Color are using default parameters.

        :param *args: The text for each buttons.
        :type *args: str
        :return: None

        Extras: - Using default font
        """
        for i in range(len(args)):
            if type(self.Buttons[i]) == Button:
                self.Buttons[i].EditText(args[i], self.TextSize, self.TextColor)
            else:
                self.Buttons[i].EditText(self.TextSize, self.TextColor)
        return None
    
    def EditTexturesAll(self) -> None:
        """
        Give all the textures location the button need.

        :return: None
        """
        for button in self.Buttons:
            if type(button) != Button:
                continue
            button.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
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

        Extras: - The list is ordered the same way you created them.
        """
        Content : list = []
        for inputbox in self.Buttons:
            if type(inputbox) != InputBox:
                continue
            Content.append(inputbox.GetInput())
        return Content
