from pyray import *
from Labyrinth import *
from Menus import *

class Game :
    def __init__(self):
        self.Maze : Labyrinth = Labyrinth()
        self.MainMenu : MainMenu = MainMenu()

        self.Atlas : Texture = None
        self.ButtonLocation : Rectangle = Rectangle(0, 0, 61, 18)

        self.CurrentMenu : list = []

    def Prepare(self) -> None:
        self.MainMenu.EditPosAll()
        self.MainMenu.EditTextAll()
        self.MainMenu.EditHoverAll()
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
        if self.CurrentMenu == []:
            self.CurrentMenu.append("MainMenu")
        return None
    
    def Draw(self) -> None:
        """
        Draw the ui and the labyrinth.
        
        :return:
        :rtype: None
        """
        self.Maze.Draw()
        self.MainMenu.Draw(self.Atlas, self.ButtonLocation)
        return None
    
    def PrepareToQuit(self) -> None:
        unload_texture(self.Atlas)
        return None
