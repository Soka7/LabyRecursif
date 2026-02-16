from pyray import *
from Labyrinth import *
from Ui.Menus import Menu

class Game :
    def __init__(self):
        self.Atlas : Texture = None                                     # The texture holding all the sprites
        self.BaseButtonLocation : Rectangle = Rectangle(0, 0, 61, 18)   # Where the button sprite is in the Atlas
        self.HoverButtonLocation : Rectangle = Rectangle(0, 18, 62, 20) # Where the hover button sprite is in the Atlas
        self.PressedButtonLocation : Rectangle = Rectangle(0, 38, 62, 20) # Where the pressed button sprite is in the Atlas
        self.InputBoxLocation : Rectangle = Rectangle(62, 0, 62, 23)    # Where the input box sprite is in the Atlas

        self.Maze : Labyrinth = Labyrinth()                         
        self.MainMenu : Menu = Menu((5, 0), self.BaseButtonLocation, self.HoverButtonLocation, self.PressedButtonLocation)
        self.SettingsMenu : Menu = Menu((1, 2), self.BaseButtonLocation, self.HoverButtonLocation,
                                                self.PressedButtonLocation, self.InputBoxLocation)

        self.CurrentMenu : list = ["MainMenu"]                          # Stack to know which menu you are in
        self.ShouldClose : bool = False

    def Prepare(self) -> None:
        self.LoadMaze("dedales.txt")
        self.Maze.FindEntry()
        self.LoadTextures("Textures/Sprites.png")

        self.MainMenu.EditPosAll(Rectangle(550, 400, 120, 40), Rectangle(550, 670, 120, 40),
                                 Rectangle(5, 670, 120, 40), Rectangle(1070, 5, 120, 40),
                                 Rectangle(550, 500, 120, 40))
        self.MainMenu.EditTextAll("Start", "Quit", "Credits", "Settings", "Creation")
        self.MainMenu.EditTexturesAll()
        self.MainMenu.BindAll(self.PrepareMaze, self.PrepareToQuit, None, self.ShowSettings, None)
        self.MainMenu.Prepare()

        self.SettingsMenu.EditPosAll(Rectangle(445, 300, 150, 50), Rectangle(300, 200, 210, 70),
                                     Rectangle(520, 200, 210, 70))
        self.SettingsMenu.EditTexturesAll()
        self.SettingsMenu.EditTextAll("Apply")
        self.SettingsMenu.BindAll(self.ApplySizeChanges)
        self.SettingsMenu.Prepare()

        return None

    def PrepareMaze(self) -> None:
        """
        Prepare the change to the maze. By loading the maze and quitting the menu.

        :return: None
        """
        self.CurrentMenu.append("Maze")
        self.LoadMaze("dedales.txt")
        return None

    def LoadMaze(self, MazePath : str) -> None:
        """
        Load a maze based of a txt file. \n
        :param MazePath: The relative path to the txt file.
        :type MazePath: str
        :rtype: None

        Extras: - In this project the MazePath is dedales.txt
        """
        self.Maze.LoadLabyrinth(MazePath)
        return None

    def LoadTextures(self, FilePath : str) -> None:
        """
        Load the file containing all the sprites.
        
        :param FilePath: The relative path to the file, likely png.
        :type FilePath: str
        :return: None

        Extras: - In this project, the FilePath is Textures/Sprites.png
        """
        self.Atlas = load_texture(FilePath)
        return None

    def Update(self) -> None:
        if self.CurrentMenu[-1] == "MainMenu":
            self.MainMenu.Update()
        elif self.CurrentMenu[-1] == "SettingsMenu":
            self.SettingsMenu.Update()
        return None
    
    def Draw(self) -> None:
        """
        Draw the adequate menu or elements.
        
        :rtype: None
        """
        if self.CurrentMenu[-1] == "MainMenu":
            self.MainMenu.Draw(self.Atlas)
        elif self.CurrentMenu[-1] == "SettingsMenu":
            self.SettingsMenu.Draw(self.Atlas)
        elif self.CurrentMenu[-1] == "Maze":
            self.Maze.Draw()
        else:
            self.MainMenu.Draw(self.Atlas)
        return None
    
    def PrepareToQuit(self) -> None:
        """
        Prepare raylib for quitting by unloading all textures.

        :return: None

        Extras: - unload_texture() is a raylib function to remove a texture from the memory.
        """
        unload_texture(self.Atlas)
        self.ShouldClose = True
        return None
    
    def ShowSettings(self) -> None:
        self.CurrentMenu.append("SettingsMenu")
        return None
    
    def ApplySizeChanges(self) -> None:
        """
        Get the player input in the settings menu and changes the size of the window accordingly.

        :return: None
        
        Extras: - set_window_size() is a raylib function to change the size of the window.
        """
        Content : list = self.SettingsMenu.GetInputBoxesContent()
        if Content[0] == '' or Content[1] == '':
            return None
        width : int = int(Content[0])
        height : int = int(Content[1])
        set_window_size(width, height)
        return None