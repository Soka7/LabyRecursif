from pyray import *
from Ui.Buttons import Button
from Ui.InputBox import InputBox

class Menu:
    def __init__(self, Buttons : tuple, ButtonBase : Rectangle, ButtonHover : Rectangle, ButtonPressed : Rectangle,
                 InputBoxTexture : Rectangle = Rectangle(0, 0, 0, 0)) -> None:
        """
        Create a Menu object with a specified amount of buttons.

        :param Buttons: A tuple of 2 elements containing the amount of buttons and input boxes.
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

        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity). \n
        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        self.Buttons : list = []                                    # List holding all the buttons and input boxes
        for _ in range(Buttons[0]):                                 # Create the buttons        
            self.Buttons.append(Button())

        for _ in range(Buttons[1]):                                 # Create the input boxes
            self.Buttons.append(InputBox(InputBoxTexture))

        self.TextSize : int = 24                                    # Default text size of the buttons
        self.TextColor : Color = (0, 0, 0, 255)                     # Default text color of the buttons

        # Buttons texture
        self.BaseButtonTexture : Rectangle = ButtonBase             # Where the base button texture is located in the Atlas
        self.HoverButtonTexture : Rectangle = ButtonHover           # Where the hover button texture is located in the Atlas
        self.PressedButtonTexture : Rectangle = ButtonPressed       # Where the pressed button texture is located in the Atlas
        return None
    
    def Update(self) -> None:
        """
        Call the update method of each button and input boxes.

        :return: None
        """
        for button in self.Buttons:
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
    
    def Prepare(self) -> None:
        """
        Call the prepare method of the input boxes.
        
        :return: None
        """
        for inputbox in self.Buttons:
            if type(inputbox) != InputBox:
                continue
            inputbox.Prepare()
        return None
    
    def EditInputBoxMessages(self, *args : tuple) -> None:
        """
        Edit the warning and welcome message of the input box
        
        :param args: A 4-uplet
        :type args: tuple
        :return: None

        Extras: - There is 1 4-uplet for each input box \n
        Extras: - The 4-uplet must contains : WelcomeText(str), WarningText(str), WarningSize(int), WarningColor(Color) in this order.\n
        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity)
        """
        Counter : int = 0
        for inputbox in self.Buttons:
            if type(inputbox) != InputBox:
                continue
            inputbox.EditWelcome(args[Counter][0])
            inputbox.EditWarning(args[Counter][1], args[Counter][2], args[Counter][3])
            Counter += 1
        return None
    
    def EditInputBoxContent(self, *args : tuple) -> None:
        """
        Edit the line, characters and text of the input box
        
        :param args: A 7-uplet
        :type args: tuple
        :return: None

        Extras: - There is one 7-uplet for each Input Box. \n
        Extras: - Each 7-uplet must have: MaxDisplayableCharacters(int), UnicodeRange(2-uplet), \n
        LineOffset(Vector2), LineCooldown(float), LineColor(Color), TextSize(int), TextColor(Color) in this order. \n
        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity) \n
        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - The UnicodeRange has 2 values being the start and end character's unicode, such as start < end.
        """
        Counter : int = 0
        for inputbox in self.Buttons:
            if type(inputbox) != InputBox:
                continue
            inputbox.EditCharacters(args[Counter][0], args[Counter][1])
            inputbox.EditLine(args[Counter][2], args[Counter][3], args[Counter][4])
            inputbox.EditText(args[Counter][5], args[Counter][6])
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

        Extras: - The list is ordered the same way you created the input boxes.
        """
        Content : list = []
        for inputbox in self.Buttons:
            if type(inputbox) != InputBox:
                continue
            Content.append(inputbox.GetInput())
        return Content
