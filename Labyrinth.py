from pyray import *
from threading import Thread
class Labyrinth:

    def __init__(self):
        self.LabyrinthArray: list = []
        self.Entry: Vector2 = (-1, -1)
        self.SideLenght: int = 10
        self.OffsetX: int = 100
        self.OffsetY: int = 100
        self.PathCounter: int = 0
        self.PathStorage: list = []
        self.PathFound: bool = False
        self.GroundColor: Color = (20, 220, 20, 255)
        self.WallColor: Color = (220, 20, 20, 255)
        self.ExitColor: Color = (20, 220, 220, 255)
        self.EntryColor: Color = (132, 10, 225, 255)
        self.ErrorColor: Color = (0, 0, 0, 255)
        self.AlrdColor: Color = (50, 50, 50, 255)
        self.RightPathColor : Color = (255, 45, 69, 255)
        self.coos = None

    def LoadLabyrinth(self, Filepath: str) -> None:
        self.LabyrinthArray.clear()
        with open(Filepath, "r") as f:
            LabyrinthString = f.read()
        for line in LabyrinthString.splitlines():
            self.LabyrinthArray.append(list(line))

    def FindEntry(self) -> None:
        for line in range(len(self.LabyrinthArray)):
            for column in range(len(self.LabyrinthArray[line])):
                if self.LabyrinthArray[line][column] == 'E':
                    self.Entry = (column, line)
                    self.coos = self.Entry
                    return

    def FindState(self, x, y):
        if y < 0 or y >= len(self.LabyrinthArray):
            return 'X'
        if x < 0 or x >= len(self.LabyrinthArray[y]):
            return 'X'
        return self.LabyrinthArray[y][x]

    def Solve(self, COOS, LISTE):
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

    def Draw(self):
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
                draw_rectangle_rec((
                    self.OffsetX + self.SideLenght * column,
                    self.OffsetY + self.SideLenght * LineCount,
                    self.SideLenght, self.SideLenght
                ), Current)
            LineCount += 1