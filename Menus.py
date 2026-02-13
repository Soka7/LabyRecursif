from pyray import *
from Button import Button

class MainMenu:
    def __init__(self, ButtonBase : Rectangle, ButtonHover : Rectangle, ButtonPressed : Rectangle) -> None:
        # Main menu Buttons
        self.StartButton : Button = Button()
        self.QuitButton : Button = Button()
        self.CreditsButton : Button = Button()
        self.SettingsButton : Button = Button()
        self.CreationButton : Button = Button()

        self.TextSize : int = 24
        self.TextColor : Color = (0, 0, 0, 255)
        self.BaseButtonTexture : Rectangle = ButtonBase
        self.HoverButtonTexture : Rectangle = ButtonHover
        self.PressedButtonTexture : Rectangle = ButtonPressed
        return None
    
    def Update(self) -> None:
        self.StartButton.Update()
        self.QuitButton.Update()
        self.CreditsButton.Update()
        self.SettingsButton.Update()
        self.CreationButton.Update()
        return None

    def Draw(self, Atlas : Texture) -> None:
        self.StartButton.Draw(Atlas)
        self.QuitButton.Draw(Atlas)
        self.CreditsButton.Draw(Atlas)
        self.SettingsButton.Draw(Atlas)
        self.CreationButton.Draw(Atlas)
        return None

    def EditPosAll(self) -> None:
        self.StartButton.EditPos(Vector2(550, 400), Vector2(120, 40))
        self.QuitButton.EditPos(Vector2(550, 680), Vector2(120, 40))
        self.CreditsButton.EditPos(Vector2(5, 680), Vector2(120, 40))
        self.SettingsButton.EditPos(Vector2(1055, 10), Vector2(120, 35))
        self.CreationButton.EditPos(Vector2(550, 480), Vector2(120, 40))
        return None
    
    def EditTextAll(self) -> None:
        self.StartButton.EditText("Start", self.TextSize, self.TextColor)
        self.QuitButton.EditText("Quit", self.TextSize, self.TextColor)
        self.CreditsButton.EditText("Credits", self.TextSize, self.TextColor)
        self.SettingsButton.EditText("Settings", self.TextSize, self.TextColor)
        self.CreationButton.EditText("Create", self.TextSize, self.TextColor)
        return None
    
    def EditTexturesAll(self) -> None:
        # Make a small hover effect on the button.
        self.StartButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        self.QuitButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        self.CreditsButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        self.SettingsButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        self.CreationButton.EditTextures(self.BaseButtonTexture, self.HoverButtonTexture, self.PressedButtonTexture)
        return None
    
    def BindAll(self, StartFunction, QuitFunction, CreditsFunction, SettingsFunction, CreationFunction) -> None:
        self.StartButton.Bind(StartFunction)
        self.QuitButton.Bind(QuitFunction)
        self.CreditsButton.Bind(CreditsFunction)
        self.SettingsButton.Bind(SettingsFunction)
        self.CreationButton.Bind(CreationFunction)
        return None
