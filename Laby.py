from pyray import *

class Labyrinth:
    def __init__(self):
        LabyrinthString : str = ""
        Labyrinth : list = []
    def LoadLabyrinth(self, Filepath : str):
        LabyrinthString = str(open(Filepath, "r"))
    def Solve(self):
        pass
    def TransformToArray(self):
        Labyrinth = [list(ligne) for ligne in laby.splitlines()]