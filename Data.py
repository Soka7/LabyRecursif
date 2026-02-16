from pyray import *

UiData : dict = {
    "MainMenu" : {
        "StartButton" :
        {
            "Position" : Rectangle(550, 400, 120, 40), 
            "Text" : "Start"
        },
        "QuitButton" :
        {
            "Position" : Rectangle(550, 670, 120, 40),
            "Text" : "Quit"
        },
        "SettingsButton" :
        {
            "Position" : Rectangle(1070, 5, 120, 40),
            "Text" : "Options"
        },
        "CreditsButton" :
        {
            "Position" : Rectangle(5, 670, 120, 40),
            "Text" : "Credits"
        },
        "CreationButton" :
        {
            "Position" : Rectangle(550, 500, 120, 40),
            "Text" : "Create"
        }
    },
    "SettingsMenu" :
    {
        "ApplyButton":
        {
            "Position" : Rectangle(445, 300, 150, 50),
            "Text" : "Apply"
        },
        "BackButton" :
        {
            "Position" : Rectangle(445, 600, 150, 50),
            "Text" : "Back"
        },
        "WidthInputBox" :
        {
            "Position" : Rectangle(300, 200, 210, 70),
            "WelcomeText" : "Width :",
            "WarningText" : "Limit reached !",
            "WarningSize" : 16,
            "WarningColor" : RED,
            "MaxCharacters" : 4,
            "CharacterRange" : (48, 57),
            "LineOffset" : Vector2(5, 0),
            "LineCooldown" : 0.5,
            "LineColor" : BLACK,
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "HeightInputBox" :
        {
            "Position" : Rectangle(520, 200, 210, 70),
            "WelcomeText" : "Height :",
            "WarningText" : "Limit reached !",
            "WarningSize" : 16,
            "WarningColor" : RED,
            "MaxCharacters" : 4,
            "CharacterRange" : (48, 57),
            "LineOffset" : Vector2(5, 0),
            "LineCooldown" : 0.5,
            "LineColor" : BLACK,
            "TextSize" : 24,
            "TextColor" : BLACK
        }

    }
}