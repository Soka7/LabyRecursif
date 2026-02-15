from pyray import *
from Labyrinth import *
from Ui.Menus import Menu

class Game :
    def __init__(self):
        self.Atlas : Texture = None                                     # The texture holding all the sprites
        self.BaseButtonLocation : Rectangle = Rectangle(0, 0, 61, 18)   # Where the button sprite is in the Atlas
        self.HoverButtonLocation : Rectangle = Rectangle(0, 18, 62, 20) # Where the hover button sprite is in the Atlas
        self.PressedButtonLocation : Rectangle = Rectangle(0, 38, 62, 20) # Where the pressed button sprite is in the Atlas

        self.Maze : Labyrinth = Labyrinth()                         
        self.MainMenu : Menu = Menu(5, self.BaseButtonLocation, self.HoverButtonLocation, self.PressedButtonLocation)

        self.CurrentMenu : list = []                                    # Stack to know which menu you are in
        self.ShouldClose : bool = False
        self.InMenus : bool = True                                      # If the player is inside menus or not

    def Prepare(self) -> None:
        self.LoadMaze("dedales.txt")
        self.Maze.FindEntry()
        self.LoadTextures("Textures/Sprites.png")

        self.MainMenu.EditPosAll(Rectangle(550, 400, 120, 40), Rectangle(550, 670, 120, 40),
                                 Rectangle(5, 670, 120, 40), Rectangle(1070, 5, 120, 40),
                                 Rectangle(550, 500, 120, 40))
        self.MainMenu.EditTextAll("Start", "Quit", "Credits", "Settings", "Creation")
        self.MainMenu.EditTexturesAll()
        self.MainMenu.BindAll(self.PrepareMaze, self.PrepareToQuit, None, None, None)

        return None

    def PrepareMaze(self) -> None:
        """
        Prepare the change to the maze. By loading the maze and quitting the menu.

        :return: None
        """
        self.InMenus = False
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
        self.MainMenu.Update()
        if self.CurrentMenu == []:
            self.CurrentMenu.append("MainMenu")
        return None
    
    def Draw(self) -> None:
        """
        Draw the adequate menu or elements.
        
        :rtype: None
        """
        if self.InMenus:
            self.MainMenu.Draw(self.Atlas)
        else:
            self.Maze.Draw()
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
