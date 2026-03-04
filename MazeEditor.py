from pyray import *

from Ui.Menus import Menu

class EditorScreen:
    def __init__(self) -> None:
        """
        Create an EditorScreen object, all values are defaulted to 0 or None.

        :return: None

        Extras: - Camera2D is a raylib struct to have a 2D camera (viewport). \n
        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        self.Camera : Camera2D = Camera2D()                                 # Camera used to show the maze
        self.CameraZoomFactor : float = 1.08                                # The camera factor / divisor applied when zooming in and out
        self.CurrentObject : str = " "                                      # The current object held by the user
        self.MazeArray : list = []                                          # The array containing the maze

        self.WallObject : str = "X"                                         # Character used to represents wall
        self.EntryObject : str = "E"                                        # Character used to represents entry
        self.ExitObject : str = "S"                                         # Character used to represents exit
        self.GroundObject : str = " "                                       # Character used to represents Ground

        self.WallTexture : Rectangle = Rectangle(0, 0, 0, 0)                # Location of the wall texture in the Atlas
        self.EntryTexture : Rectangle = Rectangle(0, 0, 0, 0)               # Location of the entry texture in the Atlas
        self.ExitTexture : Rectangle = Rectangle(0, 0, 0, 0)                # Location of the exit texture in the Atlas
        self.GroundTexture : Rectangle = Rectangle(0, 0, 0, 0)              # Location of the ground texture in the Atlas

        self.GridLenght : int = 0                                           # The number of cells on one line of the maze
        self.GridHeight : int = 0                                           # The number of cells on one column of the maze
        self.MazeLenght : int = 0                                           # The lenght of the maze in pixels
        self.MazeHeight : int = 0                                           # The height of the maze in pixels
        self.CellSize : Vector2 = Vector2(32, 32)                           # The size of each cell

        self.HUD : Menu = Menu(1, 10, 0, 0, 0)                              # The user interface, 1 button and 10 icon buttons

        self.WarningTestPopUp : Menu = Menu(0, 1, 0, 0, 2)                  # The pop up that appears after testing the maze, 1 icon button and 2 label
        self.ShowWarningTestPopUp : bool = False                            # If the warning Pop Up should be shown or not
        self.ValidationTestPopUp : Menu = Menu(0, 1, 0, 0, 2)               # The pop up that appears after testing the maze, 1 icon button and 2 label
        self.ShowValidationTestPopUp : bool = False                         # if the validation Pop Up should be shown or not
        self.OpenFilePopUp : Menu = Menu(1, 1, 1, 0, 1)                     # The pop up that appears when trying to open a file
        self.ShowOpenFilePopUp : bool = False
        
        self.BaseScreenSize : Vector2 = Vector2(1200, 720)                  # The screen size at which the editor screen was made

        self.MousePosition : Vector2 = Vector2(0, 0)                        # Mouse position when the user right clicked
        self.MouseSensitivity : float = 1                                   # Mouse sensitivity when dragging the camera
        self.MouseSensitivityIncrement : float = 0.1                        # By how much the sensitivity increment / decrement when changed

        self.CurrentAction : str = ""                                       # The action the user is going to do
        self.CanPlace : bool = False                                        # Make sure only action is placed each frame
        self.InputStack : list = []                                         # A stack to store all the input of the user
        self.ReversedInputStack : list = []                                 # A stack to store all the input the user reversed

        self.BackFunction = None                                            # The function for the exit button
        return None
    
    def RegisterMousePosition(self) -> None:
        """
        Store the the current mouse position.
        
        :return: None

        Extras: - get_mouse_position() is a raylib function returning a Vector2 holding the x and y position of the mouse.
        """
        self.MousePosition = get_mouse_position()
        return None
    
    def GetCamera(self) -> Camera2D:
        """
        :return: The camera used by the editor.
        :rtype: Camera2D

        Extras: - Camera2D is a raylib struct to have a 2D camera (viewport).
        """
        return self.Camera
    
    def GetCellClicked(self) -> Vector2:
        """
        Get the cell clicked by the mouse.

        :return: The x and y coordinates of the cell
        :rtype: Vector2

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n   
        Extras: - get_screen_to_world_2d() is a raylib function to convert a position on the screen to a position on the world. \n
        Extras: - get_mouse_position() is a raylib function to get the coordinates of the mouse.  
        """
        WorldCoordinates : Vector2 = get_screen_to_world_2d(get_mouse_position(), self.Camera)

        if not self.IsMouseInsideMaze(WorldCoordinates):
            return Vector2(-1, -1)
        
        Cell : Vector2 = Vector2(WorldCoordinates.x // self.CellSize.x, WorldCoordinates.y // self.CellSize.y)
        return Cell
    
    def SetCell(self, Coordinates : Vector2, Object : str) -> None:
        """
        Set a cell of the maze to be the a wanted object.

        :param Coordinates: The x and y indices of the cell
        :type Coordinates: Vector2
        :param Object: The object to place
        :type Object: str
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        self.MazeArray[int(Coordinates.x)][int(Coordinates.y)] = Object
        return None

    def IsMouseInsideMaze(self, MousePosition : Vector2) -> bool:
        """
        Check if the mouse is inside the maze.

        :param MousePosition: The mouse position in the world
        :type MousePosition: Vector2
        :return: True if it is, False otherwise
        :rtype: bool

        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        if MousePosition.x < 0 or MousePosition.x >= self.MazeLenght:
            return False
        if MousePosition.y < 0 or MousePosition.y >= self.MazeHeight:
            return False
        
        return True

    def CreateMazeArray(self) -> None:
        """
        Create an array of self.Lenght by self.Height to be the maze.

        :return: None
        """
        self.MazeArray.clear()
        for i in range(self.GridHeight):
            line : list = []
            for j in range(self.GridLenght):
                line.append(" ")
            self.MazeArray.append(line)
        return None
    
    def ComputeMazeDimensions(self) -> None:
        """
        Calculate the lenght and height in pixels of the maze.

        :return: None
        """
        self.MazeLenght = self.GridLenght * self.CellSize.x
        self.MazeHeight = self.GridHeight * self.CellSize.y
        return None
    
    def SetMazeGridSize(self, Lenght : int, Height : int) -> None:
        """
        Set the size of the grid to edit the maze.
        
        :param lenght: The lenght of the maze in cells
        :type lenght: int
        :param height: The height of the maze in cells
        :type lenght: int
        :return: None
        """
        self.GridLenght = Lenght
        self.GridHeight = Height
        return None
    
    def TakeWallObject(self) -> None:
        """
        Take the wall object (X) as the current object.

        :return: None
        """
        if self.CurrentObject == self.WallObject:
            self.CurrentObject = self.GroundObject
        else:
            self.CurrentObject = self.WallObject
        self.CanPlace = False
        return None

    def TakeEntryObject(self) -> None:
        """
        Take the entry object (E) as the current object.

        :return: None
        """
        if self.CurrentObject == self.EntryObject:
            self.CurrentObject = self.GroundObject
        else:
            self.CurrentObject = self.EntryObject
        self.CanPlace = False
        return None

    def TakeExitObject(self) -> None:
        """
        Take the exit object (S) as the current object.

        :return: None
        """
        if self.CurrentObject == self.ExitObject:
            self.CurrentObject = self.GroundObject
        else:
            self.CurrentObject = self.ExitObject
        self.CanPlace = False
        return None

    def TakeGroundObject(self) -> None:
        """
        Take the Ground object ( ) as the current object.

        :return: None
        """
        self.CurrentObject = self.GroundObject
        self.CanPlace = False
        return None
    
    def SetReplaceAll(self) -> None:
        """
        Prepare the replace all action.

        :return: None
        """
        if self.CurrentAction == "ReplaceAll":
            self.CurrentAction = ""
        else:
            self.CurrentAction = "ReplaceAll"
        self.CanPlace = False
        return None
    
    def Save(self) -> None:
        """
        Save the maze in a txt file.

        :return: None
        """
        File = open("Mazes/dedales.txt", "w")
        for column in self.MazeArray:
            FileLine : str = ""
            for line in column:
                FileLine += line
            FileLine += "\n"
            File.write(FileLine)
        self.CanPlace = False
        File.close()
        return None
    
    def ReplaceAll(self) -> None:
        """
        Replace all the occurence of a selected object by the current object.

        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        """
        Cell : Vector2 = self.GetCellClicked()
        if Cell.x == -1 and Cell.y == -1 or not self.CanPlace:
            return None
        
        Input : list = []
        ChangedCells : list = []
    
        ObjectToReplace : str = self.MazeArray[int(Cell.y)][int(Cell.x)]

        for column in range(len(self.MazeArray)):
            for line in range(len(self.MazeArray[column])):
                if self.MazeArray[column][line] == ObjectToReplace:
                    self.MazeArray[column][line] = self.CurrentObject
                    ChangedCells.append(Vector2(column, line))

        self.CanPlace = False

        Input.append(ObjectToReplace)
        Input.append(self.CurrentObject)
        Input.append(ChangedCells)
        self.InputStack.append(Input)
        return None
    
    def ReverseLastAction(self) -> None:
        """
        Reverse the last action made by the user.

        :return: None

        Extras: - Input are stored like this [PreviousObject, NewObject, [Coordinates1, Coordinates2...]] \n
        PreviousObject and NewObject are string and the list of coordinates holds Vector2.
        """
        if self.InputStack == [] or not self.CanPlace:
            return None
        
        self.CanPlace = False

        Input : list = self.InputStack.pop()
        for coordinates in Input[2]:
            self.SetCell(coordinates, Input[0])
        self.ReversedInputStack.append(Input)
        return None
    
    def ReverseLastReversedAction(self) -> None:
        """
        Reverse the last reversed action made by the user.

        :return: None

        Extras: - Input are stored like this [PreviousObject, NewObject, [Coordinates1, Coordinates2...]] \n
        PreviousObject and NewObject are string and the list of coordinates holds Vector2.
        """
        if self.ReversedInputStack == [] or not self.CanPlace:
            return None
        
        self.CanPlace = False

        Input : list = self.ReversedInputStack.pop()
        for coordinates in Input[2]:
            self.SetCell(coordinates, Input[1])
        self.InputStack.append(Input)
        return None
    
    def TestMaze(self) -> bool:
        """
        Make a quick test of the maze by checking if there is one entry and one exit.

        :return: Whether or not the maze pass these 2 conditions
        :rtype: bool
        """
        EntryCount : int = 0
        ExitCount : int = 0

        for column in range(len(self.MazeArray)):
            for line in range(len(self.MazeArray[column])):
                if self.MazeArray[column][line] == self.EntryObject:
                    EntryCount += 1
                elif self.MazeArray[column][line] == self.ExitObject:
                    ExitCount += 1
        
        return EntryCount == 1 and ExitCount == 1   
    
    def TestAndFeedBack(self) -> None:
        """
        Test the maze and show a warning if the maze isn't valid.

        :return: None
        """
        Valid : bool = self.TestMaze()
        if Valid:
            self.ShowValidationTestPopUp = True
        else:
            self.ShowWarningTestPopUp = True
        return None
    
    def HideTestPopUp(self) -> None:
        """
        Hide both test pop ups.

        :return: None
        """
        self.ShowWarningTestPopUp = False
        self.ShowValidationTestPopUp = False
        return None
    
    def OpenMaze(self, FilePath : str = "") -> None:
        """
        Open a new maze from a relative path.

        :param FilePath: The relative path of the file
        :type FilePath: str
        :return: None

        Extras: - If the program can't open the file, the pop up will close. \n
        Extras: - The argument is only used when the user tries to open a maze before creating one.
        """
        if FilePath == "":
            Content : list = self.OpenFilePopUp.GetInputBoxesContent()
        else:
            Content : list = [FilePath]
        try:
            File = open(Content[0], "r")
            self.MazeArray.clear()
            MazeString = File.read()
            File.close()
            for line in MazeString.splitlines():
                self.MazeArray.append(list(line))
                
            MazeWidth : int = len(self.MazeArray[0])
            MazeHeight : int = len(self.MazeArray)

            self.SetMazeGridSize(MazeWidth, MazeHeight)
            self.ComputeMazeDimensions()
            self.ResetCam()

            self.ShowOpenFilePopUp = False
        except:
            self.ShowOpenFilePopUp = False
            return None
        
    def ShowOpenPopUp(self) -> None:
        """
        Show the open file menu.

        :return: None
        """
        self.ShowOpenFilePopUp = True
        return None
    
    def HideOpenPopUp(self) -> None:
        """
        Hide the pop up of the open file menu.

        :return: None
        """
        self.ShowOpenFilePopUp = False
        return None

    def ResetCam(self) -> None:
        """
        Reset the camera parameters and center it.

        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - get_screen_width() is a raylib method to get the width of the current raylib window. \n
        Extras: - get_screen_height() is a raylib method to get the width of the current raylib window.
        """
        ScreenWidth : int = get_screen_width()
        ScreenHeight : int = get_screen_height()

        self.Camera.offset = Vector2(ScreenWidth / 2, ScreenHeight / 2)
        self.Camera.rotation = 0
        self.Camera.target = Vector2((self.GridLenght * self.CellSize.x) / 2, (self.GridHeight * self.CellSize.y) / 2)
        self.Camera.zoom = 1
        self.MouseSensitivity = 1
        return None

    def ExecuteInput(self) -> None:
        """
        Check and Execute all potential keyboard and mouse related inputs.

        :return: None

        Extras: - get_mouse_position() is a raylib function that returns the x and y position of the mouse. \n
        Extras: - get_mouse_wheel_move() is a raylib function to get how much time the scroller was moved. \n

        Extras: - is_mouse_button_pressed() is a raylib function checking if a button of the mouse has been pressed. \n
        Extras: - is_mouse_button_down() is a raylib function checking if a button is held. \n
        Extras: - is_key_pressed() is a raylib function checking if a given key of the keyboard has been pressed. \n
        Extras: - is_key_down() is a raylib function checking if a given key of the keyboard is being held. \n

        Extras: - MouseButton.MOUSE_BUTTON_RIGHT is a raylib data that refers to the right mouse button. \n
        Extras: - KEY_MINUS is a raylib data that refers to the minus key on qwerty keyboard. \n
        Extras: - KEY_EQUAL is a raylib data that refers to the equal key on qwerty keyboard. \n
        Extras: - KEY_R is a raylib data that refers to the r key on qwerty keyboard. \n
        Extras: - KEY_S is a raylib data that refers to the s key on qwerty keyboard. \n
        Extras: - KEY_W is a raylib data that refers to the w key on qwerty keyboard. \n
        Extras: - KEY_Y is a raylib data that refers to the y key on qwerty keyboard. \n
        Extras: - KEY_O is a raylib data that refers to the o key on qwerty keyboard. \n
        Extras: - KEY_LEFT_CONTROL is a raylib function that refers to the left control on a keyboard. \n
        Extras: - KEY_RIGHT_CONTROL is a raylib function that refers to the right control on a keyboard. \n
        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        """
        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_RIGHT):
            self.RegisterMousePosition()

        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT):
            CurrentMousePosition : Vector2 = get_mouse_position()
            self.Camera.target = Vector2((self.MousePosition.x - CurrentMousePosition.x + self.MazeLenght / 2) * self.MouseSensitivity,
                                         (self.MousePosition.y - CurrentMousePosition.y + self.MazeHeight / 2) * self.MouseSensitivity)
        if get_mouse_wheel_move() > 0:
            self.Camera.zoom *= self.CameraZoomFactor
        elif get_mouse_wheel_move() < 0:
            self.Camera.zoom /= self.CameraZoomFactor

        if is_key_pressed(KEY_MINUS):
            self.MouseSensitivity -= self.MouseSensitivityIncrement
            if self.MouseSensitivity <= 0.1:
                self.MouseSensitivity = 0.1
        elif is_key_pressed(KEY_EQUAL):
            self.MouseSensitivity += self.MouseSensitivityIncrement

        if (is_key_down(KEY_LEFT_CONTROL) or is_key_down(KEY_RIGHT_CONTROL)) and is_key_pressed(KEY_S):
            self.Save()

        if (is_key_down(KEY_LEFT_CONTROL) or is_key_down(KEY_RIGHT_CONTROL)) and is_key_pressed(KEY_W):
            self.ReverseLastAction()

        if (is_key_down(KEY_LEFT_CONTROL) or is_key_down(KEY_RIGHT_CONTROL)) and is_key_pressed(KEY_Y):
            self.ReverseLastReversedAction()

        if (is_key_down(KEY_LEFT_CONTROL) or is_key_down(KEY_RIGHT_CONTROL)) and is_key_pressed(KEY_O):
            self.ShowOpenFilePopUp = True

        if is_key_pressed(KEY_R):
            self.ResetCam()
        return None

    def ExecuteActions(self) -> None:
        """
        Execute actions related to ui actions, such as replace all.

        :return: None

        Extras: - is_mouse_button_pressed() is a raylib function checking if a button of the mouse has been pressed. \n
        Extras: - MouseButton.MOUSE_BUTTON_LEFT is a raylib data that refers to the left mouse button \n
        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - get_mouse_position() is a raylib function returning a Vector2 holding the x and y position of the mouse. \n
        Extras: - get_screen_to_world_2d() is a raylib function to transform a screen position into a world position.
        """
        if not is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            return None
        
        WorldCoordinates : Vector2 = get_screen_to_world_2d(get_mouse_position(), self.Camera)

        if not self.IsMouseInsideMaze(WorldCoordinates) or not self.CanPlace:
            return None
        
        if self.CurrentAction == "ReplaceAll":
            self.ReplaceAll()
            self.CanPlace = False

        return None
    
    def DrawObject(self, Atlas : Texture, Source : Rectangle, Destination : Rectangle) -> None:
        """
        Used to draw a specific object.

        :param Atlas: The texture holding all of the game's texture
        :type Atlas: Texture
        :param Source: The location of the texture to draw inside the Atlas
        :type Source: Rectangle
        :param Destination: Where to draw the texture on the screen
        :type Destination: Rectangle
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height. \n
        Extras: - Texture is a raylib structure holding an image. \n
        Extras: - draw_texture_pro() is a raylib method to draw a texture with additional parameters. \n
        Extras: - In this project, Atlas refers to Sprites.png
        """
        Origin : Vector2 = Vector2(0, 0)
        Rotation : float = 0
        draw_texture_pro(Atlas, Source, Destination, Origin, Rotation, WHITE)
        return None

    def DrawHUD(self, Atlas : Texture) -> None:
        """
        Draw the user interface elements.

        :param Atlas: The atlas texture holding all the sprites of the game.
        :type Atlas: Texture
        :return: None

        Extras: - In this project Atlas is Sprites.png. \n
        Extras: - Texture is raylib structure holding an image.
        """
        self.HUD.Draw(Atlas)
        if self.ShowValidationTestPopUp:
            self.ValidationTestPopUp.Draw(Atlas)
        elif self.ShowWarningTestPopUp:
            self.WarningTestPopUp.Draw(Atlas)
        elif self.ShowOpenFilePopUp:
            self.OpenFilePopUp.Draw(Atlas)
        return None

    def Draw(self, Atlas : Texture) -> None:
        """
        Draw the maze with the right textures.

        :param Atlas: The texture holding all of the game's texture
        :type Atlas: Texture
        :return: None

        Extras: - Rectangle is a raylib structure with 4 values, x, y, width, height. \n
        Extras: - Texture is a raylib structure holding an image. \n
        Extras: - In this project, Atlas refers to Sprites.png
        """
        for column in range(len(self.MazeArray)):
            for line in range(len(self.MazeArray[column])):
                DestRec : Rectangle = Rectangle(self.CellSize.x * line, self.CellSize.y * column, self.CellSize.x, self.CellSize.y)
                if self.MazeArray[column][line] == self.GroundObject:
                    self.DrawObject(Atlas, self.GroundTexture, DestRec)

                elif self.MazeArray[column][line] == self.WallObject:
                    self.DrawObject(Atlas, self.WallTexture, DestRec)

                elif self.MazeArray[column][line] == self.EntryObject:
                    self.DrawObject(Atlas, self.EntryTexture, DestRec)

                elif self.MazeArray[column][line] == self.ExitObject:
                    self.DrawObject(Atlas, self.ExitTexture, DestRec)
        return None
    
    def UpdateMaze(self) -> None:
        """
        Update the maze by checking what the user placed.

        :return: None

        Extras: - is_mouse_button_down() is a raylib function checking if a button of the mouse is being held. \n
        Extras: - MouseButton.MOUSE_BUTTON_LEFT is a raylib data that refers to the left mouse button.
        """
        if not is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT) and not is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT):
            return None
        
        Cell : Vector2 = self.GetCellClicked()

        if Cell.x == -1 and Cell.y == -1 or not self.CanPlace:
            return None

        Column : int = int(Cell.y)
        Line : int = int(Cell.x)

        Input : list = []
        ReplacedObject : str = self.MazeArray[Column][Line]

        if self.MazeArray[Column][Line] != self.CurrentObject:
            self.MazeArray[Column][Line] = self.CurrentObject
        NewObject : str = self.MazeArray[Column][Line]

        Input.append(ReplacedObject)
        Input.append(NewObject)
        Input.append([Vector2(Column, Line)])

        # Explanation of this horrible mess :
        # It first checks if teh list isn't empty to avoid crashes
        # Then it checks if first element of the new input is the same as the first element of the last registered input
        # Same for the 2nd element
        # Then, the 3rd element is a list of Vector2, but there is just 1 vector2
        # So it checks the first element of the list (the only Vector2) and check if the x and y coordinates are the same
        # In the end, if everything was right, it doesn't register the input because it is the exact same input
        if (self.InputStack != []) \
            and (Input[0] == self.InputStack[-1][0]) \
            and (Input[1] == self.InputStack[-1][1]) \
            and (Input[2][0].x == self.InputStack[-1][2][0].x) \
            and (self.InputStack[-1][2][0].y == Input[2][0].y):
            self.CanPlace = False
            return None
        self.InputStack.append(Input)
        self.CanPlace = False
        return None
    
    def Update(self) -> None:
        """
        Update the maze, by taking and executing the user input, updating the user interface accordingly \n
        and then updating the maze.

        :return: None
        """
        self.CanPlace = True
        if self.ShowValidationTestPopUp:
            self.CanPlace = False
            self.ValidationTestPopUp.Update()
        elif self.ShowWarningTestPopUp:
            self.CanPlace = False
            self.WarningTestPopUp.Update()
        elif self.ShowOpenFilePopUp:
            self.CanPlace = False
            self.OpenFilePopUp.Update()
        self.ExecuteInput()
        self.HUD.Update()
        self.ExecuteActions()
        self.UpdateMaze()
        return None
    
    def Scale(self, ScreenSize : Vector2) -> None:
        """
        Scale the editor screen to the given ScreenSize.

        :param ScreenSize: The width and height of the screen
        :type ScreenSize: Vector2
        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        self.HUD.ScaleMenu(ScreenSize)
        self.ValidationTestPopUp.ScaleMenu(ScreenSize)
        self.WarningTestPopUp.ScaleMenu(ScreenSize)
        self.OpenFilePopUp.ScaleMenu(ScreenSize)

        XFactor : float = ScreenSize.x / self.BaseScreenSize.x
        YFactor : float = ScreenSize.y / self.BaseScreenSize.y

        self.CellSize.x = self.CellSize.x * XFactor
        self.CellSize.y = self.CellSize.y * YFactor

        self.ComputeMazeDimensions()
        self.BaseScreenSize = ScreenSize
        return None
    
    def LoadTexturesLocation(self, SpriteData : dict) -> None:
        """
        Load the location of all the needed textures.

        :param SpriteData: The dictionary holding all the textures location in the Atlas
        :type SpriteData: dict
        :return: None
        """
        Sprites : dict = SpriteData["Tiles"]
        self.WallTexture = Sprites["Wall"]
        self.EntryTexture = Sprites["Entry"]
        self.ExitTexture = Sprites["Exit"]
        self.GroundTexture = Sprites["Ground"]
        return None
    
    def PrepareHUDAndTextures(self, UiData : dict, SpriteData : dict) -> None:
        """
        Prepare teh HUD menu by loading the sprites and the button informations.

        :param UiData: The dictionary containing each ui element information
        :type UiData: dict
        :param SpriteData: The dictionary containign the location of each sprite
        :type SpriteData: dict
        :return: None
        """
        self.HUD.Prepare(UiData, "EditorHUDMenu", SpriteData)
        self.ValidationTestPopUp.Prepare(UiData, "ValidationTestPopUp", SpriteData)
        self.WarningTestPopUp.Prepare(UiData, "WarningTestPopUp", SpriteData)
        self.OpenFilePopUp.Prepare(UiData, "OpenFilePopUp", SpriteData)
        self.LoadTexturesLocation(SpriteData)
        return None
    
    def BindBackButton(self, Function) -> None:
        """
        Bind the exit button's function.

        :param Function: The function that the back button will call
        :type Function: function
        :return: None

        Extras: - The function must have no arguments and return None. \n
        Extras: - Call this before Prepare().
        """
        self.BackFunction = Function
        return None

    def Prepare(self) -> None:
        """
        Call all the methods that need to be called once.

        :return: None
        """
        self.HUD.BindAll(self.BackFunction, self.TakeWallObject, self.TakeEntryObject, self.TakeExitObject, self.TakeGroundObject,
                         self.ReverseLastAction, self.ReverseLastReversedAction, self.SetReplaceAll, self.Save, self.TestAndFeedBack, self.ShowOpenPopUp)
        self.ValidationTestPopUp.BindAll(self.HideTestPopUp)
        self.WarningTestPopUp.BindAll(self.HideTestPopUp)
        self.OpenFilePopUp.BindAll(self.OpenMaze, self.HideOpenPopUp)
        self.ComputeMazeDimensions()
        self.ResetCam()
        return None