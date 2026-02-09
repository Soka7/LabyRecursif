from pyray import *

class Labyrinth:
    def __init__(self):
        self.LabyrinthArray : list = []
        self.SideLenght : int = 10
        self.OffsetX : int = 100
        self.OffsetY : int = 100

        self.Ground : Color = (20, 220, 20, 255)
        self.Wall : Color = (220, 20, 20, 255)
        self.Exit : Color = (20, 220, 220, 255)
        self.Entry : Color = (20, 20, 220, 255)
        self.Error : Color = (0, 0, 0, 255)

    def LoadLabyrinth(self, Filepath : str):
        """
        Open, read and transform into an array the txt file used for the labyrinth. \n
        :param MazePath: The path to the txt file.
        :type MazePath: str
        :return:
        :rtype: None
        """
        LabyrinthString = open(Filepath, "r")
        LabyrinthString = LabyrinthString.read()
        for line in LabyrinthString.splitlines():
            self.LabyrinthArray.append(list(line))

    def Solve(self):
        pass
    
    def Draw(self):
        """
        Draw the labyrinth with the defined colors.\n
        Loops through the array and draw each rectangle.
        """
        Current : Color = self.Error
        LineCount : int = 0
        for line in self.LabyrinthArray:
            for column in range(0, len(line)):
                match line[column]:
                    case 'X':
                        Current = self.Wall
                    case ' ':
                        Current = self.Ground
                    case 'E':
                        Current = self.Entry
                    case 'S':
                        Current = self.Exit
                draw_rectangle_rec((self.OffsetX + self.SideLenght * column,
                                    self.OffsetY + self.SideLenght * LineCount,
                                    self.SideLenght, self.SideLenght), Current)
            LineCount += 1
