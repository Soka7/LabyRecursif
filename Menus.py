from pyray import *
from Button import Button

class MainMenu:
    def __init__(self) -> None:
        # Main menu Buttons
        self.StartButton : Button = Button()
        self.QuitButton : Button = Button()
        self.CreditsButton : Button = Button()
        self.SettingsButton : Button = Button()
        self.CreationButton : Button = Button()

        # Default Parameters for the buttons
        self.TextSize : int = 24
        self.TextColor : Color = (0, 0, 0, 255)
        self.HoverSize : int = 5
        self.HoverColor : Color = (0, 0, 255, 255)
        return None
    
    def Draw(self, Atlas : Texture, TextureLocation : Rectangle) -> None:
        self.StartButton.Draw(Atlas, TextureLocation)
        self.QuitButton.Draw(Atlas, TextureLocation)
        self.CreditsButton.Draw(Atlas, TextureLocation)
        self.SettingsButton.Draw(Atlas, TextureLocation)
        self.CreationButton.Draw(Atlas, TextureLocation)
        return None

    def EditPosAll(self) -> None:
        # Place all the buttons on the screen (give them a size as well).
        self.StartButton.EditPos(Vector2(550, 400), Vector2(120, 40))
        self.QuitButton.EditPos(Vector2(550, 680), Vector2(120, 40))
        self.CreditsButton.EditPos(Vector2(5, 680), Vector2(120, 40))
        self.SettingsButton.EditPos(Vector2(1055, 10), Vector2(120, 35))
        self.CreationButton.EditPos(Vector2(550, 480), Vector2(120, 40))
        return None
    
    def EditTextAll(self) -> None:
        # Edit the text with the default parameters and a specific text
        self.StartButton.EditText("Start", self.TextSize, self.TextColor)
        self.QuitButton.EditText("Quit", self.TextSize, self.TextColor)
        self.CreditsButton.EditText("Credits", self.TextSize, self.TextColor)
        self.SettingsButton.EditText("Settings", self.TextSize, self.TextColor)
        self.CreationButton.EditText("Create", self.TextSize, self.TextColor)
        return None
    
    def EditHoverAll(self) -> None:
        # Make a small hover effeft on the button.
        self.StartButton.EditHover(self.HoverSize, self.HoverColor)
        self.QuitButton.EditHover(self.HoverSize, self.HoverColor)
        self.CreditsButton.EditHover(self.HoverSize, self.HoverColor)
        self.SettingsButton.EditHover(self.HoverSize, self.HoverColor)
        self.CreationButton.EditHover(self.HoverSize, self.HoverColor)
        return None
