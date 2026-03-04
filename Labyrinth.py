from pyray import *
from threading import Thread, Lock
from time import perf_counter

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
        self.Lock: Lock = Lock()                             # Lock pour eviter les race conditions

        # Colors used to draw the maze
        self.GroundColor: Color = (20, 220, 20, 255)         
        self.WallColor: Color = (220, 20, 20, 255)
        self.ExitColor: Color = (20, 220, 220, 255)
        self.EntryColor: Color = (132, 10, 225, 255)
        self.ErrorColor: Color = (0, 0, 0, 255)
        self.AlrdColor: Color = (50, 50, 50, 255)
        self.RightPathColor : Color = (255, 45, 69, 255)

        self.ExecutionTime : float = 0
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

    def ShowExecutionTime(self) -> None:
        """
        Show the time to solve the maze inside the terminal.

        :return: None

        Extras: - We lacked some time to make it in a proper element of the user interface.
        """
        print("===========================================================\n")
        print("THE MAZE WAS SOLVED IN : ", self.ExecutionTime, " seconds. \n")
        print("===========================================================\n")
        return None

    def Threaded(self, element, LISTE):
        """The code used to solve the labyrinth and gettin processed in threads

        Args:
            element (tuple): The coordonates of the current position
            LISTE (list): The list of coordonates

        Returns:
            bool: True
        """
        if self.PathFound:                                          # Inutile de continuer si la sortie est deja trouvee
            return
        state = self.FindState(element[0], element[1])
        if state == 'S':                                            # Sortie trouvee
            with self.Lock:                                         # On prend le verrou pour eviter les race conditions
                if not self.PathFound:                              # Double verification apres acquisition du verrou
                    self.PathFound = True
                    self.PathStorage = LISTE
                    
                    # On trace le chemin le plus court et redessine l'entree une fois que la sortie est trouvee
                    for coors in self.PathStorage:
                        self.LabyrinthArray[coors[1]][coors[0]] = 'z'
                    self.LabyrinthArray[self.Entry[1]][self.Entry[0]] = 'E'
            self.ExecutionTime = perf_counter() - self.ExecutionTime
            self.ShowExecutionTime()
            return True
        elif state == ' ':
            self.Solve(element, LISTE)                              # Appel récursif, LISTE deja copiee dans Solve()

    def Solve(self, COOS : tuple, LISTE : list) -> None:
        """
        Recursively solves the labyrinth.

        :param COOS: The coordinates to explore
        :type COOS: 2-uplet
        :param LISTE:  A list to store visited coordinates
        :param LISTE: list
        :return: None
        """
        if self.ExecutionTime == 0:
            self.ExecutionTime = perf_counter()
        if self.PathFound == True:
            return True
        else:
            X1, Y1 = COOS
            
            LISTE.append(COOS)

            if self.LabyrinthArray[Y1][X1] == ' ':
                with self.Lock:                                                 # On prend le verrou pour eviter les race conditions
                    if self.PathFound == False:                                 # Double verification apres acquisition du verrou
                        self.LabyrinthArray[Y1][X1] = "."                      # On marque la case courante comme visitée

            droite = (X1 + 1, Y1)
            gauche = (X1 - 1, Y1)
            haut = (X1, Y1 - 1)
            bas = (X1, Y1 + 1)
            ListeDir = [droite, bas, gauche, haut]

            for element in ListeDir:
                th = Thread(target=self.Threaded, args=(element, LISTE.copy()))  # Chaque thread a sa propre copie de LISTE
                th.start()                                                       # On utilise des threads pour explorer chaque direction
                                                                                 # simultanement, afin d'accelerer la resolution en parcourant
                                                                                 # plusieurs chemins en parallele
            return None

#def Solve(self, COOS: tuple, LISTE: list) -> list:
#    X1, Y1 = COOS
#    state = self.FindState(X1, Y1)
#
#    if state == 'S':
#        self.PathFound = True
#        self.PathStorage = LISTE
#        for coors in self.PathStorage:
#            self.LabyrinthArray[coors[1]][coors[0]] = 'z'
#        self.LabyrinthArray[self.Entry[1]][self.Entry[0]] = 'E'
#        return LISTE
#
#    if state not in (' ', 'E'):
#        return []
#
#    self.LabyrinthArray[Y1][X1] = '.'
#
#    for element in [(X1+1, Y1), (X1, Y1+1), (X1-1, Y1), (X1, Y1-1)]:
#        result = self.Solve(element, LISTE + [COOS])
#        if result:
#            return result
#
#    return []
##########################################Pour avoir que le meilleur chemin il suffit de remonter la longueur des chemins et de tous les comparer

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
    
############
    def BenchmarkComplexity(self) -> None:
            """
            Compare la complexité temporelle et spatiale des deux versions de Solve
            sur le labyrinthe déjà chargé. À appeler après la résolution.

            :return: None
            """
            import copy
            import tracemalloc
            import matplotlib.pyplot as plt
            from time import perf_counter
            from threading import Thread, Lock

            original_maze = copy.deepcopy(self.LabyrinthArray)

            # ── Version Threaded ──────────────────────────────────────────────────
            def run_threaded():
                self.LabyrinthArray = copy.deepcopy(original_maze)
                self.PathFound = False
                self.PathStorage = []
                self.Lock = Lock()
                self.FindEntry()
                x, y = self.Entry
                self.LabyrinthArray[y][x] = ' '
                threads = []
                for element in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                    th = Thread(target=self.Threaded, args=(element, [(x,y)]))
                    th.start()
                    threads.append(th)
                for th in threads:
                    th.join(timeout=10)

            # ── Version Récursive ─────────────────────────────────────────────────
            def solve_recursive(COOS, LISTE):
                import sys; sys.setrecursionlimit(100000)
                X1, Y1 = COOS
                state = self.FindState(X1, Y1)
                if state == 'S':
                    return LISTE
                if state not in (' ', 'E'):
                    return []
                self.LabyrinthArray[Y1][X1] = '.'
                for element in [(X1+1,Y1),(X1,Y1+1),(X1-1,Y1),(X1,Y1-1)]:
                    result = solve_recursive(element, LISTE + [COOS])
                    if result:
                        return result
                return []

            def run_recursive():
                self.LabyrinthArray = copy.deepcopy(original_maze)
                self.FindEntry()
                solve_recursive(self.Entry, [])

            # ── Mesure ────────────────────────────────────────────────────────────
            def measure(fn):
                tracemalloc.start()
                t0 = perf_counter()
                fn()
                elapsed = (perf_counter() - t0) * 1000
                _, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                return elapsed, peak / 1024

            REPEATS = 5
            times_t, mems_t = zip(*[measure(run_threaded)  for _ in range(REPEATS)])
            times_r, mems_r = zip(*[measure(run_recursive) for _ in range(REPEATS)])

            # Restore le labyrinthe original
            self.LabyrinthArray = copy.deepcopy(original_maze)

            runs = list(range(1, REPEATS + 1))

            # ── Tracé ─────────────────────────────────────────────────────────────
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
            fig.suptitle("Complexité : Threaded vs Récursif", fontsize=13, fontweight="bold")

            ax1.plot(runs, times_t, 'o-',  color="crimson",    label="Threaded")
            ax1.plot(runs, times_r, 's--', color="royalblue",  label="Récursif")
            ax1.set_title("Temps d'exécution")
            ax1.set_xlabel("Exécution n°")
            ax1.set_ylabel("Temps (ms)")
            ax1.legend(); ax1.grid(True, linestyle=":")

            ax2.plot(runs, mems_t, 'o-',  color="crimson",    label="Threaded")
            ax2.plot(runs, mems_r, 's--', color="royalblue",  label="Récursif")
            ax2.set_title("Mémoire utilisée")
            ax2.set_xlabel("Exécution n°")
            ax2.set_ylabel("Mémoire (KB)")
            ax2.legend(); ax2.grid(True, linestyle=":")

            plt.tight_layout()
            import os
            plt.tight_layout()
            plt.savefig("benchmark.png", dpi=150, bbox_inches="tight")
            plt.close()
            os.system("xdg-open benchmark.png")  # Linux
            # os.system("open benchmark.png")    # macOS
            # os.startfile("benchmark.png")      # Windows
            return None
############ Claude