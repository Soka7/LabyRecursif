from pyray import *
from Labyrinth import *
from Menus import *

class Game :
    def __init__(self):
        self.Atlas : Texture = None                                     # The texture holding all the sprites
        self.BaseButtonLocation : Rectangle = Rectangle(0, 0, 61, 18)   # Where the button sprite is in the Atlas
        self.HoverButtonLocation : Rectangle = Rectangle(0, 18, 62, 20) # Where the hover button sprite is in the Atlas
        self.PressedButtonLocation : Rectangle = Rectangle(0, 38, 62, 20) # Where the pressed button sprite is in the Atlas

        self.Maze : Labyrinth = Labyrinth()                         
        self.MainMenu : MainMenu = MainMenu(self.BaseButtonLocation, self.HoverButtonLocation, self.PressedButtonLocation)

        self.CurrentMenu : list = []                                    # Stack to know which menu you are in
        self.ShouldClose : bool = False
        self.InMenus : bool = True                                      # If the player is inside menus or not

    def Prepare(self) -> None:
        self.LoadMaze("dedales.txt")
        self.Maze.FindEntry()
        self.LoadTextures("Textures/Sprites.png")
        self.MainMenu.EditPosAll()
        self.MainMenu.EditTextAll()
        self.MainMenu.EditTexturesAll()
        self.MainMenu.BindAll(self.PrepareGame, self.PrepareToQuit, None, None, None)
        return None

    def PrepareGame(self) -> None:
        self.InMenus = False
        self.LoadMaze("dedales.txt")
        return None

    def LoadMaze(self, MazePath : str) -> None:
        """
        Load a maze based of a txt file. \n
        :param MazePath: The relative path to the txt file.
        :type MazePath: str
        :return:
        :rtype: None
        """
        self.Maze.LoadLabyrinth(MazePath)
        return None

    def LoadTextures(self, FilePath : str) -> None:
        """
        Load the file containing all the sprites.
        
        :param FilePath: The relative path to the file, likely png.
        :type FilePath: str
        :return: None
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
        Draw the ui and the labyrinth.
        
        :return:
        :rtype: None
        """
        if self.InMenus:
            self.MainMenu.Draw(self.Atlas)
        else:
            self.Maze.Draw()
        return None
    
    def PrepareToQuit(self) -> None:
        unload_texture(self.Atlas)
        self.ShouldClose = True
        return None
