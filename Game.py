from pyray import *
from Labyrinth import *
from Ui.Menus import Menu
from Data import UiData

class Game :
    def __init__(self):
        self.Atlas : Texture = None                                     # The texture holding all the sprites
        self.BaseButtonLocation : Rectangle = Rectangle(0, 0, 61, 18)   # Where the button sprite is in the Atlas
        self.HoverButtonLocation : Rectangle = Rectangle(0, 18, 62, 20) # Where the hover button sprite is in the Atlas
        self.PressedButtonLocation : Rectangle = Rectangle(0, 38, 62, 20) # Where the pressed button sprite is in the Atlas
        self.InputBoxLocation : Rectangle = Rectangle(62, 0, 62, 23)    # Where the input box sprite is in the Atlas

        self.Maze : Labyrinth = Labyrinth()                         
        self.MainMenu : Menu = Menu((5, 0), self.BaseButtonLocation, self.HoverButtonLocation, self.PressedButtonLocation)
        self.SettingsMenu : Menu = Menu((2, 2), self.BaseButtonLocation, self.HoverButtonLocation,
                                                self.PressedButtonLocation, self.InputBoxLocation)

        self.CurrentMenu : list = ["MainMenu"]                          # Stack to know which menu you are in
        self.ShouldClose : bool = False

    def Prepare(self) -> None:
        self.LoadMaze("dedales.txt")
        self.Maze.FindEntry()
        self.LoadTextures("Textures/Sprites.png")

        self.MainMenu.EditPosAll(UiData["MainMenu"]["StartButton"]["Position"],
                                 UiData["MainMenu"]["QuitButton"]["Position"],
                                 UiData["MainMenu"]["CreditsButton"]["Position"],
                                 UiData["MainMenu"]["SettingsButton"]["Position"],
                                 UiData["MainMenu"]["CreationButton"]["Position"])
        
        self.MainMenu.EditTextAll(UiData["MainMenu"]["StartButton"]["Text"],
                                  UiData["MainMenu"]["QuitButton"]["Text"],
                                  UiData["MainMenu"]["CreditsButton"]["Text"],
                                  UiData["MainMenu"]["SettingsButton"]["Text"],
                                  UiData["MainMenu"]["CreationButton"]["Text"])
        
        self.MainMenu.EditTexturesAll()
        self.MainMenu.BindAll(self.PrepareMaze, self.PrepareToQuit, None, self.ShowSettings, None)
        self.MainMenu.Prepare()

        self.SettingsMenu.EditPosAll(Rectangle(445, 300, 150, 50), Rectangle(445, 600, 150, 50),
                                     Rectangle(300, 200, 210, 70), Rectangle(520, 200, 210, 70))
        self.SettingsMenu.EditTexturesAll()
        self.SettingsMenu.EditTextAll("Apply", "Back")
        self.SettingsMenu.BindAll(self.ApplySizeChanges, self.GoBack)
        self.SettingsMenu.EditInputBoxMessages(("Width : ", "Limit reached !", 16, RED),
                                               ("Height : ", "Limit reahced !", 16, RED))
        self.SettingsMenu.EditInputBoxContent((4, (48, 57), Vector2(5, 0), 0.5, BLACK, 24, BLACK),
                                              (4, (48, 57), Vector2(5, 0), 0.5, BLACK, 24, BLACK))
        self.SettingsMenu.Prepare()

        return None

    def PrepareMaze(self) -> None:
        """
        Prepare the change to the maze. By loading the maze and quitting the menu.

        :return: None
        """
        self.CurrentMenu.append("Maze")
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
        """
        Call the update method of the current menu.
        
        :return: None
        """
        if self.CurrentMenu[-1] == "MainMenu":
            self.MainMenu.Update()
        elif self.CurrentMenu[-1] == "SettingsMenu":
            self.SettingsMenu.Update()
        return None
    
    def Draw(self) -> None:
        """
        Draw the adequate menu or elements depending on the current menu.
        Draw the main menu if nothing can be drawn.
        
        :return: None
        """
        if self.CurrentMenu[-1] == "MainMenu":
            self.MainMenu.Draw(self.Atlas)
        elif self.CurrentMenu[-1] == "SettingsMenu":
            self.SettingsMenu.Draw(self.Atlas)
        elif self.CurrentMenu[-1] == "Maze":
            self.Maze.Draw()
        else:
            self.MainMenu.Draw(self.Atlas)
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
    
    def ShowSettings(self) -> None:
        """
        Add the SettingsMenu to the stack to draw and update it.
        
        :return: None
        """
        self.CurrentMenu.append("SettingsMenu")
        return None
    
    def GoBack(self) -> None:
        """
        Remove the last element from the stack to go back one menu.
        
        :return: None
        """
        self.CurrentMenu.pop(-1)
        return None
    
    def ApplySizeChanges(self) -> None:
        """
        Get the player input in the settings menu and changes the size of the window accordingly.

        :return: None
        
        Extras: - set_window_size() is a raylib function to change the size of the window. \n
        Extras: - get_current_monitor() is a raylib function to get on which monitor the window is. \n
        Extras: - get_monitor_width() is a raylib function to get the current monitor width. \n
        Extras: - get_monitor_height() is a raylib function to get the current monitor height \n
        Extras: - set_window_position() is a raylib function to change the position of the window on the screen.
        """
        Content : list = self.SettingsMenu.GetInputBoxesContent()

        if Content[0] == '' or Content[1] == '':
            return None

        width : int = int(Content[0])
        height : int = int(Content[1])

        set_window_size(width, height)

        # Center window on the screen
        CurrentMonitor : int = get_current_monitor()

        MonitorWidth : int = get_monitor_width(CurrentMonitor)
        MonitorHeight : int = get_monitor_height(CurrentMonitor)

        WindowX : int = int((MonitorWidth - width) / 2)
        WindowY : int = int((MonitorHeight - height) / 2)

        set_window_position(WindowX, WindowY)
        return None