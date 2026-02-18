from pyray import *

class Labyrinth:
    def __init__(self):
        self.LabyrinthArray : list = []                 # The labyrinth 
        self.Entry : Vector2 = (-1 ,-1)                 # Spawn point of the labyrinth
        self.SideLenght : int = 10                      # Size of each cell of the labyrinth
        self.OffsetX : int = 100                        
        self.OffsetY : int = 100

        self.PathCounter : int = 0                      # The current path used 
        self.PathStorage : list = []                    # The numbers used to displayed the paths
        self.PathFound : bool = False                   # If a path to the exit has been found

        # Color of the different tiles
        self.GroundColor : Color = (20, 220, 20, 255)      
        self.WallColor : Color = (220, 20, 20, 255)
        self.ExitColor : Color = (20, 220, 220, 255)
        self.EntryColor : Color = (20, 20, 220, 255)
        self.ErrorColor : Color = (0, 0, 0, 255)
        

    def LoadLabyrinth(self, Filepath : str) -> None:
        """
        Open, read and transform into an array the txt file used for the labyrinth. \n
        :param MazePath: The path to the txt file.
        :type MazePath: str
        :return:
        :rtype: None
        """
        self.LabyrinthArray.clear()                 # Reset the previous labyrinth to avoid duplication
        LabyrinthString = open(Filepath, "r")
        LabyrinthString = LabyrinthString.read()
        for line in LabyrinthString.splitlines():
            self.LabyrinthArray.append(list(line))
        return None

    def FindEntry(self) -> None:
        for line in range(0, len(self.LabyrinthArray)):
            for column in range(0, len(self.LabyrinthArray[line])):
                if self.LabyrinthArray[line][column] == 'E':
                    self.Entry = (line, column)
                    return None
        return None

    def Solve(self):
        pass
    
    def Draw(self):
        """
        Draw the labyrinth with the defined colors.\n
        Loops through the array and draw each rectangle.
        """
        Current : Color = self.ErrorColor
        LineCount : int = 0
        for line in self.LabyrinthArray:
            for column in range(0, len(line)):
                match line[column]:
                    case 'X':
                        Current = self.WallColor
                    case ' ':
                        Current = self.GroundColor
                    case 'E':
                        Current = self.EntryColor
                    case 'S':
                        Current = self.ExitColor
                draw_rectangle_rec((self.OffsetX + self.SideLenght * column,
                                    self.OffsetY + self.SideLenght * LineCount,
                                    self.SideLenght, self.SideLenght), Current)
            LineCount += 1