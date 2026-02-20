from pyray import *

class EditorScreen:
    def __init__(self) -> None:
        """
        Create an EditorScreen object, all values are defaulted to 0 or None.

        :return: None

        Extras: - Camera2D is a raylib struct to have a 2D camera (viewport).
        """
        self.Camera : Camera2D = Camera2D()

        self.GridLenght : int = 0
        self.GridHeight : int = 0
        self.CellSize : int = 20

        self.CameraSpeed : int = 50
        self.CameraZoom : float = 0.1
        self.CameraMinZoom : float = 0.5
        return None
    def CenterCam(self) -> None:
        ScreenWidth : int = get_screen_width()
        ScreenHeight : int = get_screen_height()

        self.Camera.offset = Vector2(ScreenWidth / 2, ScreenHeight / 2)
        self.Camera.rotation = 0
        self.Camera.target = Vector2((self.GridLenght * self.CellSize) / 2, (self.GridHeight * self.CellSize) / 2)
        self.Camera.zoom = 1
        return None
    
    def ExecuteInput(self) -> None:
        if is_key_pressed(KEY_LEFT):
            self.Camera.offset.x -= self.CameraSpeed

        if is_key_pressed(KEY_RIGHT):
            self.Camera.offset.x += self.CameraSpeed

        if is_key_pressed(KEY_UP):
            self.Camera.offset.y -= self.CameraSpeed

        if is_key_pressed(KEY_DOWN):
            self.Camera.offset.y += self.CameraSpeed

        if is_key_pressed(KEY_MINUS):
            self.Camera.zoom -= self.CameraZoom
            if self.Camera.zoom < self.CameraMinZoom:
                self.Camera.zoom = self.CameraMinZoom

        if is_key_pressed(KEY_EQUAL):
            self.Camera.zoom += self.CameraZoom

        if is_key_pressed(KEY_R):
            self.CenterCam()
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
        for i in range(self.GridLenght):
            for j in range(self.GridHeight):
                draw_rectangle_lines(self.CellSize * i, self.CellSize * j, self.CellSize, self.CellSize, BLACK)
        return None
    
    def Update(self) -> None:
        self.ExecuteInput()
        return None

init_window(1200, 720, "Creating a maze")

cam : EditorScreen = EditorScreen()
cam.SetMazeGridSize(100, 100)
cam.CenterCam()

while not window_should_close():
    cam.Update()
    begin_drawing()
    clear_background(DARKBLUE)
    begin_mode_2d(cam.Camera)

    cam.Draw()

    end_mode_2d()
    end_drawing()

close_window()

# On the work : 
# - Smooth scaling
# - Mouse Movement
# - Placeable props


# Sources :
# - Camera2D overview : https://youtu.be/zkjDU3zmk40