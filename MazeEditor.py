from pyray import *

from Ui.Menus import Menu
from Data import UiData, SpritesData

class EditorScreen:
    def __init__(self) -> None:
        """
        Create an EditorScreen object, all values are defaulted to 0 or None.

        :return: None

        Extras: - Camera2D is a raylib struct to have a 2D camera (viewport).
        """
        self.Camera : Camera2D = Camera2D()                                 # Camera used to show the maze
        self.CurrentObject : str = " "                                      # The current object held by the user
        self.MazeArray : list = []                                          # The array containing the maze

        self.GridLenght : int = 0                                           # The number of cells on one line of the maze
        self.GridHeight : int = 0                                           # The number of cells on one column of the maze
        self.CellSize : int = 20                                            # The size of each cell
        self.MazeLenght : int = 0                                           # The lenght of the maze in pixels
        self.MazeHeight : int = 0                                           # The height of the maze in pixels

        self.CameraSpeed : int = 50                                         # The speed at which the camera moves
        self.CameraZoomIncrement : float = 0.1                              # The zoom by which the camera zoom increment / decrements
        self.CameraMinZoom : float = 0.5                                    # The minimum zoom of the camera

        self.HUD : Menu = Menu(4, 0, 0, 0)                                  # The user interface, 4 buttons
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
        self.HUD.BindAll(self.TakeWallObject, self.TakeEntryObject, self.TakeExitObject, self.TakeEmptyObject)
        self.CreateMazeArray()
        self.ComputeMazeDimensions()
        self.CenterCam()
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
        Calculate the lenght and height of the maze.

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
        self.CurrentObject = "X"
        return None

    def TakeEntryObject(self) -> None:
        """
        Take the entry object (E) as the current object.

        :return: None
        """
        self.CurrentObject = "E"
        return None

    def TakeExitObject(self) -> None:
        """
        Take the exit object (S) as the current object.

        :return: None
        """
        self.CurrentObject = "S"
        return None

    def TakeEmptyObject(self) -> None:
        """
        Take the empty object ( ) as the current object.

        :return: None
        """
        self.CurrentObject = " "
        return None
    
    def CenterCam(self) -> None:
        """
        Center the camera on the screen.

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
        return None
    
    def ExecuteInput(self) -> None:
        if is_key_pressed(KEY_LEFT):
            self.Camera.target.x -= self.CameraSpeed

        if is_key_pressed(KEY_RIGHT):
            self.Camera.target.x += self.CameraSpeed

        if is_key_pressed(KEY_UP):
            self.Camera.target.y -= self.CameraSpeed

        if is_key_pressed(KEY_DOWN):
            self.Camera.target.y += self.CameraSpeed

        if is_key_pressed(KEY_MINUS):
            self.Camera.zoom -= self.CameraZoomIncrement
            if self.Camera.zoom < self.CameraMinZoom:
                self.Camera.zoom = self.CameraMinZoom

        if is_key_pressed(KEY_EQUAL):
            self.Camera.zoom += self.CameraZoomIncrement

        if is_key_pressed(KEY_R):
            self.CenterCam()
        return None

    def UpdateMaze(self) -> None:
        """
        Update the maze by checking what the user placed.

        :return: None

        Extras: - Vector2 is a raylib structure holding a x and a y position. \n
        Extras: - is_mouse_button_down() is a raylib function checking if a button of the mouse is being held. \n
        Extras: - MouseButton.MOUSE_BUTTON_LEFT is a raylib data that refers to the left mouse button. \n
        Extras: - get_screen_to_world_2d() is a raylib function to convert a position on the screen to a position on the world. \n
        Extras: - get_mouse_position() is a raylib function to get the coordinates of the mouse.
        """
        if not is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            return None
        
        WorldCoordinates : Vector2 = get_screen_to_world_2d(get_mouse_position(), self.Camera)

        if WorldCoordinates.x < 0 or WorldCoordinates.x > self.MazeLenght:
            return None
        if WorldCoordinates.y < 0 or WorldCoordinates.y > self.MazeHeight:
            return None
        
        ChangedCell : Vector2 = Vector2(WorldCoordinates.x / self.CellSize, WorldCoordinates.y / self.CellSize)
        Column : int = int(ChangedCell.y)
        Line : int = int(ChangedCell.x)
        self.MazeArray[Column][Line] = self.CurrentObject
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

    def Draw(self) -> None:
        for column in range(len(self.MazeArray)):
            for line in range(len(self.MazeArray[column])):
                if self.MazeArray[column][line] == " ":
                    draw_rectangle_lines(self.CellSize * line, self.CellSize * column, self.CellSize, self.CellSize, BLACK)
                elif self.MazeArray[column][line] == "X":
                    draw_rectangle(self.CellSize * line, self.CellSize * column, self.CellSize, self.CellSize, RED)
                elif self.MazeArray[column][line] == "E":
                    draw_rectangle(self.CellSize * line, self.CellSize * column, self.CellSize, self.CellSize, PURPLE)
                elif self.MazeArray[column][line] == "S":
                    draw_rectangle(self.CellSize * line, self.CellSize * column, self.CellSize, self.CellSize, GREEN)
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
        self.ExecuteInput()
        self.HUD.Update()
        self.UpdateMaze()
        return None

init_window(1200, 720, "Creating a maze")

Atlas : Texture = load_texture("Textures/Sprites.png")

cam : EditorScreen = EditorScreen()
cam.SetMazeGridSize(20, 20)
cam.Prepare(UiData, SpritesData)

while not window_should_close():
    cam.Update()
    begin_drawing()
    clear_background(DARKBLUE)
    begin_mode_2d(cam.Camera)
    cam.Draw()
    end_mode_2d()
    cam.DrawHUD(Atlas)
    end_drawing()

close_window()

# On the work : 
# - Smooth scaling
# - Mouse Movement
# - Better editor tools (ctrl z, ctrl y, holding mouse button to draw line)
# - Exporting the maze


# Sources :
# - Camera2D overview : https://youtu.be/zkjDU3zmk40
# - Code example and additional details : https://www.raylib.com/examples/core/loader.html?name=core_2d_camera