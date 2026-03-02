from pyray import *
from threading import Thread

class Labyrinth:

    def __init__(self):
        """
        Create a labyrinth object, everything is set in the constructor.

        :return: None

        Extras: - Vector2 is a raylib data storing 2 floats, being x and y coordinates. \n
        Extras: - Color is a raylib data storing 4 floats, being a RGBA code (Red, Green, Blue, Alpha(opacity)).
        """
        self.LabyrinthArray : list = []                      # The labyrinth stored as a list of list
        self.Entry : Vector2 = (-1, -1)                      # Position of the labyrinth's entry
        self.SideLenght : int = 10                           # Size of each cell of the labyrinth

        self.OffsetX: int = 100                              # Offset on the x axis to the cells
        self.OffsetY: int = 100                              # Offset on the y axis to the cells

        self.PathStorage: list = []                          # Stores all the path taken
        self.PathFound: bool = False                         # If a path to the exit has been found

        # Colors used to draw the maze
        self.GroundColor: Color = (20, 220, 20, 255)         
        self.WallColor: Color = (220, 20, 20, 255)
        self.ExitColor: Color = (20, 220, 220, 255)
        self.EntryColor: Color = (132, 10, 225, 255)
        self.ErrorColor: Color = (0, 0, 0, 255)
        self.AlrdColor: Color = (50, 50, 50, 255)
        self.RightPathColor : Color = (255, 45, 69, 255)
        return None

    def LoadLabyrinth(self, Filepath: str) -> None:
        """
        Load a maze from a txt file. Also clear the previous loaded maze.

        :param Filepath: the relative path to the txt file
        :type Filepath: str

        :return: None
        """
        self.LabyrinthArray.clear()
        with open(Filepath, "r") as f:
            LabyrinthString = f.read()
        for line in LabyrinthString.splitlines():
            self.LabyrinthArray.append(list(line))
        return None

    def FindEntry(self) -> None:
        """
        Find the entry of the maze.

        :return: None
        """
        for line in range(len(self.LabyrinthArray)):
            for column in range(len(self.LabyrinthArray[line])):
                if self.LabyrinthArray[line][column] == 'E':
                    self.Entry = (column, line)
                    return None
        return None

    def FindState(self, x : int, y : int) -> str:
        """
        Get the state of cell of the labyrinth.

        :param x: The x coordinate of the maze
        :type x: int
        :param y: The y coordinate of the maze
        :type y: int
        :return: The state of the cell, 'X' if it is out of bounds.
        :rtype: str
        """
        if y < 0 or y >= len(self.LabyrinthArray):
            return 'X'
        if x < 0 or x >= len(self.LabyrinthArray[y]):
            return 'X'
        return self.LabyrinthArray[y][x]

    def Solve(self, COOS : tuple, LISTE : list) -> None:
        """
        Recursively solves the labyrinth.

        :param COOS: The coordinates to explore
        :type COOS: 2-uplet
        :param LISTE:  A list to store visited coordinates
        :param LISTE: list
        :return: None
        """
        X1, Y1 = COOS
        
        LISTE.append(COOS)

        if self.LabyrinthArray[Y1][X1] == ' ':
            self.LabyrinthArray[Y1][X1] = "."

        droite = (X1 + 1, Y1)
        gauche = (X1 - 1, Y1)
        haut = (X1, Y1 - 1)
        bas = (X1, Y1 + 1)
        ListeDir = [droite, bas, gauche, haut]

        for element in ListeDir:
            def Threaded(element):
                state = self.FindState(element[0], element[1])
                if state == 'S':
                    self.PathFound = True
                    self.PathStorage = LISTE
                    for coors in self.PathStorage:
                        self.LabyrinthArray[coors[1]][coors[0]] = 'z'
                    self.LabyrinthArray[self.Entry[1]][self.Entry[0]] = 'E'
                    return True
                elif state == ' ':
                    self.Solve(element, LISTE.copy())
            th = Thread(target = Threaded, args=(element,))
            th.start()
        return None

    def Draw(self) -> None:
        """
        Draw the maze with the color defined in the constructor.

        :return: None

        Extras: - Color is a raylib data storing 4 floats, being a RGBA code (Red, Green, Blue, Alpha(opacity)). \n
        Extras: - draw_rectangle_rec() is a raylib function to draw a rectangle using a rectangle argument. \n
        Extras: - Rectangle is a raylib data storing 4 floats, being x and y coordinates and width and height.
        """
        Current: Color = self.ErrorColor
        LineCount: int = 0
        for line in self.LabyrinthArray:
            for column in range(len(line)):
                match line[column]:
                    case 'X':
                        Current = self.WallColor
                    case ' ':
                        Current = self.GroundColor
                    case 'E':
                        Current = self.EntryColor
                    case 'S':
                        Current = self.ExitColor
                    case '.':
                        Current = self.AlrdColor
                    case 'z':
                        Current = self.RightPathColor
                DestRec : Rectangle = Rectangle(self.OffsetX + self.SideLenght * column, self.OffsetY + self.SideLenght * LineCount,
                                                self.SideLenght, self.SideLenght)
                draw_rectangle_rec(DestRec, Current)
            LineCount += 1
        return None