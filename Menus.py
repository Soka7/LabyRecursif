from pyray import *
from Button import Button

class MainMenu:
    def __init__(self) -> None:
        self.StartButton = Button()
        self.QuitButton = Button()
        self.CreditsButton = Button()
        self.SettingsButton = Button()
        self.CreationButton = Button()

        self.TextSize = 24
        self.TextColor = (0, 0, 0, 255)
        self.HoverSize = 5
        self.HoverColor = (0, 0, 255, 255)
        return None
    
    def Draw(self) -> None:
        self.StartButton.Draw()
        self.QuitButton.Draw()
        self.CreditsButton.Draw()
        self.SettingsButton.Draw()
        self.CreationButton.Draw()
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
    
    def EditHoverAll(self) -> None:
        self.StartButton.EditHover(self.HoverSize, self.HoverColor)
        self.QuitButton.EditHover(self.HoverSize, self.HoverColor)
        self.CreditsButton.EditHover(self.HoverSize, self.HoverColor)
        self.SettingsButton.EditHover(self.HoverSize, self.HoverColor)
        self.CreationButton.EditHover(self.HoverSize, self.HoverColor)
        return None
