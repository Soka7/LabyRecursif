from pyray import *

SpritesData : dict = {
    "Button" : 
    {
        "Base" : Rectangle(1, 0, 62, 18),
        "Hover" : Rectangle(0, 18, 64, 20),
        "Pressed" : Rectangle(0, 38, 62, 18),
        "HoverPressed" : Rectangle(0, 57, 64, 20)
    },
    "InputBox" :
    {
        "Base" : Rectangle(63, 0, 62, 23)
    },
    "CheckBox" :
    {
        "Base" : Rectangle(187, 0, 30, 30),
        "Hover" : Rectangle(217, 0, 32, 32),
        "Checked" : Rectangle(187, 30, 30, 30),
        "CheckedHover" : Rectangle(217, 32, 32, 32)
    },
    "IconButton" :
    {
        "Base" : Rectangle(187, 64, 28, 28),
        "Hover" : Rectangle(215, 64, 30, 30),
        "Pressed" : Rectangle(187, 92, 28, 28),
        "HoverPressed" : Rectangle(215, 94, 30, 30)
    },
    "Background" :
    {
        "SettingsMenu" : Rectangle(125, 0, 62, 62),
        "CreationPopUp" : Rectangle(125, 0, 62, 62)
    },
    "Tiles" : 
    {
        "Wall" : Rectangle(0, 240, 16, 16),
        "Ground" : Rectangle(16, 240, 16, 16),
        "Entry" : Rectangle(32, 240, 16, 16),
        "Exit" : Rectangle(48, 240, 16, 16)
    },
    "Icons" :
    {
        "Cross" : Rectangle(238, 238, 18, 18),
        "Entry" : Rectangle(226, 240, 12, 16),
        "Exit" : Rectangle(214, 241, 12, 15),
        "Ground" : Rectangle(198, 240, 16, 16),
        "Wall" : Rectangle(182, 240, 16, 16)
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
            "Position" : Rectangle(460, 330, 150, 50),
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
            "Position" : Rectangle(550, 140, 210, 70),
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
            "Position" : Rectangle(550, 250, 210, 70),
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
            "Position" : Rectangle(570, 490, 39, 39)
        },
        "WindowSizeLabel" :
        {
            "Type" : "Label",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Vector2(365, 80),
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
            "Position" : Vector2(430, 165),
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
            "Position" : Vector2(430, 275),
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
            "Position" : Vector2(430, 500),
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
        },
        "MiscLabel" :
        {
            "Type" : "Label",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Vector2(365, 415),
            "Text" : "Miscellaneous :",
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
        }
    },
    "CreationPopUp" :
    {
        "Background" :
        {
            "RefTexture" : "Background",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "HasBackground" : True,
            "Position" : Rectangle(350, 200, 500, 320),
        },
        "ApplyButton" :
        {
            "Type" : "Button",
            "RefTexture" : "Button",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(535, 460, 150, 50),
            "Text" : "Apply",
            "TextSize" : 24,
            "TextColor" : Color(141, 220, 220, 255)
        },
        "BackButton" :
        {
            "Type" : "IconButton",
            "RefTexture" : "IconButton",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(780, 210, 42, 42),
            "IconScaleFactor" : Vector2(0.5, 0.5),
            "RefIconTexture" : "Cross"
        },
        "LenghtInputBox" :
        {
            "Type" : "InputBox",
            "RefTexture" : "InputBox",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(520, 275, 180, 60),
            "WelcomeText" : "10",
            "WarningText" : "Limit reached !",
            "WarningSize" : 16,
            "WarningColor" : RED,
            "MaxCharacters" : 3,
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
            "Position" : Rectangle(520, 365, 180, 60),
            "WelcomeText" : "10",
            "WarningText" : "Limit reached !",
            "WarningSize" : 16,
            "WarningColor" : RED,
            "MaxCharacters" : 3,
            "CharacterRange" : (48, 57),
            "LineOffset" : Vector2(5, 0),
            "LineCooldown" : 0.5,
            "LineColor" : BLACK,
            "TextSize" : 24,
            "TextColor" : BLACK
        },
        "CreationLabel" :
        {
            "Type" : "Label",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Vector2(535, 215),
            "Text" : "Parameters",
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
        "LenghtLabel" :
        {
            "Type" : "Label",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Vector2(400, 290),
            "Text" : "Lenght :",
            "TextSize" : 24,
            "TextColor" : Color(226, 114, 91, 255),
            "Rotation" : 0,
            "Origin" : Vector2(0, 0),
            "CharacterSpacing" : 2,
            "Underline" : True,
            "LineColor" : Color(226, 114, 91, 255),
            "LineSpacing" : 1,
            "LineThickness" : 1,
            "Overline" : False,
            "OverlineColor" : Color(0, 0, 0, 0)
        },
        "HeightLabel" : 
        {
            "Type" : "Label",
            "OriginalScreenSize" : Vector2(1200, 720),
            "Position" : Vector2(400, 380),
            "Text" : "Height :",
            "TextSize" : 24,
            "TextColor" : Color(226, 114, 91, 255),
            "Rotation" : 0,
            "Origin" : Vector2(0, 0),
            "CharacterSpacing" : 2,
            "Underline" : True,
            "LineColor" : Color(226, 114, 91, 255),
            "LineSpacing" : 1,
            "LineThickness" : 1,
            "Overline" : False,
            "OverlineColor" : Color(0, 0, 0, 0)
        }
    },
    "EditorHUDMenu" :
    {
        "Background" :
        {
            "RefTexture" : "Background",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "HasBackground" : False,
            "Position" : Rectangle(0, 0, 0, 0),
        },
        "WallPlacerButton" :
        {
            "Type" : "IconButton",
            "RefTexture" : "IconButton",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(1065, 70, 60, 60),
            "IconScaleFactor" : Vector2(0.5, 0.5),
            "RefIconTexture" : "Wall"
        },
        "EntryPlacerButton" :
        {
            "Type" : "IconButton",
            "RefTexture" : "IconButton",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(1135, 5, 60, 60),
            "IconScaleFactor" : Vector2(0.5, 0.5),
            "RefIconTexture" : "Entry"
        },
        "ExitPlacerButton" :
        {
            "Type" : "IconButton",
            "RefTexture" : "IconButton",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(1135, 70, 60, 60),
            "IconScaleFactor" : Vector2(0.5, 0.5),
            "RefIconTexture" : "Exit"
        },
        "GroundPlacerButton" :
        {
            "Type" : "IconButton",
            "RefTexture" : "IconButton",
            "OriginalScreenSize" : Vector2(1200, 720), 
            "Position" : Rectangle(1065, 5, 60, 60),
            "IconScaleFactor" : Vector2(0.5, 0.5),
            "RefIconTexture" : "Ground"
        },
    }
}