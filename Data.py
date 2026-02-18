from pyray import *

SpritesData : dict = {
    "Button" : 
    {
        "Base" : Rectangle(0, 0, 62, 18),
        "Hover" : Rectangle(0, 18, 63, 20),
        "Pressed" : Rectangle(0, 38, 62, 20)
    },
    "InputBox" :
    {
        "Base" : Rectangle(62, 0, 62, 23)
    },
    "CheckBox" :
    {
        "Base" : Rectangle(186, 0, 30, 30),
        "Hover" : Rectangle(216, 0, 32, 32),
        "Checked" : Rectangle(186, 30, 30, 30),
        "CheckedHover" : Rectangle(216, 32, 32, 32)
    },
    "Background" :
    {
        "SettingsMenu" : Rectangle(124, 0, 62, 62)
    }
}

UiData : dict = {
    "MainMenu" : 
    {
        "Background" :
        {
            "RefTexture" : "Background",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "HasBackground" : False,
            "Position" : Rectangle(0, 0, 0, 0),
        },
        "StartButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(550, 400, 120, 40), 
            "Text" : "Start",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "QuitButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(550, 670, 120, 40),
            "Text" : "Quit",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "SettingsButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(1070, 5, 120, 40),
            "Text" : "Options",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "CreditsButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(5, 670, 120, 40),
            "Text" : "Credits",
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "CreationButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(550, 500, 120, 40),
            "Text" : "Create",
            "TextSize" : 24,
            "TextColor" : BLACK
        }
    },
    "SettingsMenu" :
    {
        "Background" :
        {
            "RefTexture" : "Background",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "HasBackground" : True,
            "Position" : Rectangle(300, 60, 600, 600),
        },
        "ApplyButton":
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(460, 320, 150, 50),
            "Text" : "Apply",
            "TextSize" : 24,
            "TextColor" : Color(141, 220, 220, 255)
        },
        "BackButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(525, 580, 150, 50),
            "Text" : "Back",
            "TextSize" : 24,
            "TextColor" : Color(141, 220, 220, 255)
        },
        "WidthInputBox" :
        {
            "Type" : "InputBox",
            "RefTexture" : "InputBox",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(550, 125, 210, 70),
            "WelcomeText" : "1200",
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
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(550, 225, 210, 70),
            "WelcomeText" : "720",
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
        "FPSCheckBox" :
        {
            "Type" : "CheckBox",
            "RefTexture" : "CheckBox",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Rectangle(570, 395, 39, 39)
        },
        "WindowSizeLabel" :
        {
            "Type" : "Label",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Vector2(360, 80),
            "Text" : "Window settings :",
            "TextSize" : 26,
            "TextColor" : Color(141, 220, 220, 255),
            "Rotation" : 0,
            "Origin" : Vector2(0, 0),
            "CharacterSpacing" : 2,
            "Underline" : True,
            "LineColor" : Color(141, 220, 220, 255),
            "LineSpacing" : 2,
            "LineThickness" : 1,
            "Overline" : False,
            "OverlineColor" : Color(0, 0, 0, 0)
        },
        "WidthLabel" :
        {
            "Type" : "Label",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Vector2(430, 150),
            "Text" : "Width :",
            "TextSize" : 24,
            "TextColor" : Color(226, 114, 91, 255),
            "Rotation" : 0,
            "Origin" : Vector2(0, 0),
            "CharacterSpacing" : 2,
            "Underline" : True,
            "LineColor" : Color(226, 114, 91, 255),
            "LineSpacing" : 2,
            "LineThickness" : 1,
            "Overline" : False,
            "OverlineColor" : Color(0, 0, 0, 0)
        },
        "HeightLabel" :
        {
            "Type" : "Label",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Vector2(430, 250),
            "Text" : "Height :",
            "TextSize" : 24,
            "TextColor" : Color(226, 114, 91, 255),
            "Rotation" : 0,
            "Origin" : Vector2(0, 0),
            "CharacterSpacing" : 2,
            "Underline" : True,
            "LineColor" : Color(226, 114, 91, 255),
            "LineSpacing" : 2,
            "LineThickness" : 1,
            "Overline" : False,
            "OverlineColor" : Color(0, 0, 0, 0)
        },
        "FPSLabel" : 
        {
            "Type" : "Label",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Vector2(430, 400),
            "Text" : "Draw FPS :",
            "TextSize" : 24,
            "TextColor" : Color(226, 114, 91, 255),
            "Rotation" : 0,
            "Origin" : Vector2(0, 0),
            "CharacterSpacing" : 2,
            "Underline" : True,
            "LineColor" : Color(226, 114, 91, 255),
            "LineSpacing" : 2,
            "LineThickness" : 1,
            "Overline" : False,
            "OverlineColor" : Color(0, 0, 0, 0)
        }
    }
}