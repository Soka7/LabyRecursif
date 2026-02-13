from pyray import *
from Button import Button

class MainMenu:
    def __init__(self, ButtonBase : Rectangle, ButtonHover : Rectangle, ButtonPressed : Rectangle) -> None:
        """
        Create the class with each button and default text size & colors.

        :param ButtonBase: The location of the base button texture in the Atlas.
        :type ButtonBase: Rectangle
        :param ButtonHover: The location of the hover button texture in the Atlas.
        :type ButtonHover: Rectangle
        :param ButtonPressed: The location of the pressed button texture in the Atlas.
        :type ButtonPressed: Rectangle
        :return: None

        Extras: - Color is raylib structure with 4 values, a Red, Green, Blue tint and alpha (opacity).
        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        # Buttons of the menu
        self.StartButton : Button = Button()
        self.QuitButton : Button = Button()
        self.CreditsButton : Button = Button()
        self.SettingsButton : Button = Button()
        self.CreationButton : Button = Button()

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
        self.StartButton.Update()
        self.QuitButton.Update()
        self.CreditsButton.Update()
        self.SettingsButton.Update()
        self.CreationButton.Update()
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
        self.StartButton.Draw(Atlas)
        self.QuitButton.Draw(Atlas)
        self.CreditsButton.Draw(Atlas)
        self.SettingsButton.Draw(Atlas)
        self.CreationButton.Draw(Atlas)
        return None

    def EditPosAll(self) -> None:
        """
        Place all the buttons, positions and sizes are hardcoded here.

        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height.
        """
        self.StartButton.EditPos(Rectangle(550, 400, 120, 40))
        self.QuitButton.EditPos(Rectangle(550, 680, 120, 40))
        self.CreditsButton.EditPos(Rectangle(5, 680, 120, 40))
        self.SettingsButton.EditPos(Rectangle(1055, 10, 120, 40))
        self.CreationButton.EditPos(Rectangle(550, 480, 120, 40))
        return None
    
    def EditTextAll(self) -> None:
        """
        Give the text parameters to all buttons of the menu. Size and Color are using default parameters.

        :return: None

        Extras: - Using default font
        """
        self.StartButton.EditText("Start", self.TextSize, self.TextColor)
        self.QuitButton.EditText("Quit", self.TextSize, self.TextColor)
        self.CreditsButton.EditText("Credits", self.TextSize, self.TextColor)
        self.SettingsButton.EditText("Settings", self.TextSize, self.TextColor)
        self.CreationButton.EditText("Create", self.TextSize, self.TextColor)
        return None
    
    def EditTexturesAll(self) -> None:
        """
        Give all the textures location the button need.

        :return: None
        """
        self.StartButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        self.QuitButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        self.CreditsButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        self.SettingsButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        self.CreationButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        return None
    
    def BindAll(self, StartFunction, QuitFunction, CreditsFunction, SettingsFunction, CreationFunction) -> None:
        """
        Define which functions the buttons should call when clicked.

        :param StartFunction: The function for the start button.
        :type StartFunction: function
        :param QuitFunction: The function for the quit button.
        :type QuitFunction: function
        :param CreditsFunction: The function for the credits button.
        :type CreditsFunction: function
        :param SettingsFunction: The function for the settings button.
        :type SettingsFunction: function
        :param CreationFunction: The function for the creation button.
        :type CreationFunction: function
        :return: None

        Extras: - Each function must be argumentless and must return None
        """
        self.StartButton.Bind(StartFunction)
        self.QuitButton.Bind(QuitFunction)
        self.CreditsButton.Bind(CreditsFunction)
        self.SettingsButton.Bind(SettingsFunction)
        self.CreationButton.Bind(CreationFunction)
        return None
