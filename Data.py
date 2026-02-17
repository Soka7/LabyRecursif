from pyray import *

SpritesData : dict = {
    "Button" : 
    {
        "Base" : Rectangle(0, 0, 61, 18),
        "Hover" : Rectangle(0, 18, 62, 20),
        "Pressed" : Rectangle(0, 38, 62, 20)
    },
    "InputBox" :
    {
        "Base" : Rectangle(62, 0, 62, 23)
    }
}

UiData : dict = {
    "MainMenu" : 
    {
        "StartButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "Position" : Rectangle(550, 400, 120, 40), 
            "Text" : "Start",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "QuitButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "Position" : Rectangle(550, 670, 120, 40),
            "Text" : "Quit",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "SettingsButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "Position" : Rectangle(1070, 5, 120, 40),
            "Text" : "Options",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "CreditsButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "Position" : Rectangle(5, 670, 120, 40),
            "Text" : "Credits",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "CreationButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "Position" : Rectangle(550, 500, 120, 40),
            "Text" : "Create",
            "TextSize" : 24,
            "TextColor" : BLACK
        }
    },
    "SettingsMenu" :
    {
        "ApplyButton":
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "Position" : Rectangle(445, 300, 150, 50),
            "Text" : "Apply",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "BackButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "Position" : Rectangle(445, 600, 150, 50),
            "Text" : "Back",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "WidthInputBox" :
        {
            "Type" : "InputBox",
            "RefTexture" : "InputBox",
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
            "Type" : "InputBox",
            "RefTexture" : "InputBox",
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