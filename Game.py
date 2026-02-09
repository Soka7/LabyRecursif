from pyray import *
from Labyrinth import *

class Game :
    def __init__(self):
        self.Maze : Labyrinth = Labyrinth()

    def LoadMaze(self, MazePath : str) -> None:
        """
        Load a maze based of a txt file. \n
        :param MazePath: The path to the txt file.
        :type MazePath: str
        :return:
        :rtype: None
        """
        self.Maze.LoadLabyrinth(MazePath)
        return None

    def Update(self):
        pass
    
    def Draw(self) -> None:
        """
        Draw the ui and the labyrinth.
        
        :return:
        :rtype: None
        """
        self.Maze.Draw()
