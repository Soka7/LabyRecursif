from pyray import *
from math import log, exp

from Ui.Menus import Menu
from Data import UiData, SpritesData

class EditorScreen:
    def __init__(self) -> None:
        """
        Create an EditorScreen object, all values are defaulted to 0 or None.

        :return: None

        Extras: - Camera2D is a raylib struct to have a 2D camera (viewport). \n
        Extras: - Vector2 is a raylib structure holding a x and a y position.
        """
        self.Camera : Camera2D = Camera2D()                                 # Camera used to show the maze
        self.CurrentObject : str = " "                                      # The current object held by the user
        self.MazeArray : list = []                                          # The array containing the maze

        self.WallObject : str = "W"                                         # Character used to represents wall
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
        self.CellSize : int = 32                                            # The size of each cell

        self.HUD : Menu = Menu(0, 6, 0, 0, 0)                               # The user interface, 6 icon buttons

        self.MousePosition : Vector2 = Vector2(0, 0)                        # Mouse position when the user right clicked
        self.MouseSensitivity : float = 1                                   # Mouse sensitivity when dragging the camera
        self.MouseSensitivityIncrement : float = 0.1                        # By how much the sensitivity increment / decrement when changed

        self.CurrentAction : str = ""                                       # The action the user is going to do
        self.CanPlace : bool = False                                        # Make sure only action is placed each frame
        return None
    
    def RegisterMousePosition(self) -> None:
        """
        Store the the current mouse position.
        
        :return: None

        Extras: - get_mouse_position() is a raylib function returning a Vector2 holding the x and y position of the mouse.
        """
        self.MousePosition = get_mouse_position()
        return None
    
    def Prepare(self, UiData : dict, SpriteData : dict) -> None:
        """
        Call all the methods that need to be called once.

        :param UiData: The dictionary containing each ui element information
        :type UiData: dict
        :param SpriteData: The dictionary containign the location of each sprite
        :type SpriteData: dict
        :return: None
        """
        self.HUD.Prepare(UiData, "EditorHUDMenu", SpriteData)
        self.LoadTexturesLocation(SpriteData)
        self.HUD.BindAll(self.TakeWallObject, self.TakeEntryObject, self.TakeExitObject, self.TakeGroundObject, self.SetReplaceAll, self.Save)
        self.CreateMazeArray()
        self.ComputeMazeDimensions()
        self.ResetCam()
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
    
    def CreateMazeArray(self) -> None:
        """
        Create an array of self.Lenght by self.Height to be the maze.

        :return: None
        """
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
        self.MazeLenght = self.GridLenght * self.CellSize
        self.MazeHeight = self.GridHeight * self.CellSize
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
        return None

    def TakeGroundObject(self) -> None:
        """
        Take the Ground object ( ) as the current object.

        :return: None
        """
        self.CurrentObject = self.GroundObject
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
        self.Camera.target = Vector2((self.GridLenght * self.CellSize) / 2, (self.GridHeight * self.CellSize) / 2)
        self.Camera.zoom = 1
        self.MouseSensitivity = 1
        return None

    def ExecuteInput(self) -> None:
        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_RIGHT):
            self.RegisterMousePosition()

        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT):
            CurrentMousePosition : Vector2 = get_mouse_position()
            self.Camera.target = Vector2((self.MousePosition.x - CurrentMousePosition.x + self.MazeLenght / 2) * self.MouseSensitivity,
                                         (self.MousePosition.y - CurrentMousePosition.y + self.MazeHeight / 2) * self.MouseSensitivity)
        if get_mouse_wheel_move() > 0:
            self.Camera.zoom = exp(log(self.Camera.zoom, 8) + (float(get_mouse_wheel_move())*0.35))
        elif get_mouse_wheel_move() < 0:
            self.Camera.zoom = exp(log(self.Camera.zoom, 8) + (float(get_mouse_wheel_move())*0.05))

        if is_key_pressed(KEY_MINUS):
            self.MouseSensitivity -= self.MouseSensitivityIncrement
        elif is_key_pressed(KEY_EQUAL):
            self.MouseSensitivity += self.MouseSensitivityIncrement

        if is_key_pressed(KEY_R):
            self.ResetCam()
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
        
        Cell : Vector2 = Vector2(WorldCoordinates.x // self.CellSize, WorldCoordinates.y // self.CellSize)
        return Cell

    def UpdateMaze(self) -> None:
        """
        Update the maze by checking what the user placed.

        :return: None

        Extras: - is_mouse_button_down() is a raylib function checking if a button of the mouse is being held. \n
        Extras: - MouseButton.MOUSE_BUTTON_LEFT is a raylib data that refers to the left mouse button.
        """
        if not is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            return None
        
        Cell : Vector2 = self.GetCellClicked()

        if Cell.x == -1 and Cell.y == -1 or not self.CanPlace:
            return None

        Column : int = int(Cell.y)
        Line : int = int(Cell.x)

        if self.MazeArray[Column][Line] != self.CurrentObject:
            self.MazeArray[Column][Line] = self.CurrentObject
        else:
            self.MazeArray[Column][Line] = self.GroundObject
        self.CanPlace = False
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
                DestRec : Rectangle = Rectangle(self.CellSize * line, self.CellSize * column, self.CellSize, self.CellSize)
                if self.MazeArray[column][line] == self.GroundObject:
                    self.DrawObject(Atlas, self.GroundTexture, DestRec)

                elif self.MazeArray[column][line] == self.WallObject:
                    self.DrawObject(Atlas, self.WallTexture, DestRec)

                elif self.MazeArray[column][line] == self.EntryObject:
                    self.DrawObject(Atlas, self.EntryTexture, DestRec)

                elif self.MazeArray[column][line] == self.ExitObject:
                    self.DrawObject(Atlas, self.ExitTexture, DestRec)
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
        return None
    
    def Update(self) -> None:
        """
        Update the maze, by taking and executing the user input, updating the user interface accordingly \n
        and then updating the maze.

        :return: None
        """
        self.CanPlace = True
        self.ExecuteInput()
        self.HUD.Update()
        self.ExecuteActions()
        self.UpdateMaze()
        return None
    
    def Save(self) -> None:
        """
        Save the maze in a txt file.

        :return: None
        """
        File = open("Mazes/Maze.txt", "w")
        for column in self.MazeArray:
            FileLine : str = ""
            for line in column:
                FileLine += line
            FileLine += "\n"
            File.write(FileLine)
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
        
        ObjectToReplace : str = self.MazeArray[int(Cell.y)][int(Cell.x)]

        for column in range(len(self.MazeArray)):
            for line in range(len(self.MazeArray[column])):
                if self.MazeArray[column][line] == ObjectToReplace:
                    self.MazeArray[column][line] = self.CurrentObject
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
        return None


init_window(1200, 720, "Creating a maze")

Background : Color = Color(128, 128, 128, 255)
Atlas : Texture = load_texture("Textures/Sprites.png")

cam : EditorScreen = EditorScreen()
cam.SetMazeGridSize(10, 20)
cam.Prepare(UiData, SpritesData)

while not window_should_close():
    cam.Update()
    begin_drawing()
    clear_background(Background)
    begin_mode_2d(cam.Camera)
    cam.Draw(Atlas)
    end_mode_2d()
    cam.DrawHUD(Atlas)
    end_drawing()

close_window()

# On the work : 
# - Better editor tools (ctrl z, ctrl y, holding mouse button to draw line) Make a button for it as well
# - Integrating teh maze to the menu
# - Importing a maze

# Sources :
# - Camera2D overview : https://youtu.be/zkjDU3zmk40
# - Code example and additional details : https://www.raylib.com/examples/core/loader.html?name=core_2d_camera
# - Software for pixel art : PixiEditor
# - Help for the saving system : https://www.w3schools.com/python/python_file_write.asp